"""
Run a model.
"""
import json
import inspect
import os
import typing
import subprocess
import sys

from pexpect import split_command_line

import dslibrary
from dslibrary import ENV_DSLIBRARY_TOKEN
from dslibrary.front import DSLibraryException, ENV_DSLIBRARY_TARGET, ENV_DSLIBRARY_SPEC, METRICS_ALIAS
from dslibrary.metadata import Metadata


class ModelRunner(object):
    """
    Each instance sets up for one run of one model.
    """
    def __init__(self, uri: str=None, user: str=None, run_id: str=None, entry_point: str = "main", mlflow: (bool, dict)=None):
        """
        The constructor provides some context which is optional when directly invoking local code, and required
        when invoking code remotely.

        :param uri:             Unique identifier for the model.
        :param user:            Which user is running the model.
        :param run_id:          Run ID needs to be specified when running in MLFlow.
        :param entry_point:     Which entry point is being called.
        :param mlflow:          MLFlow-related settings.  True = send all to mlflow, {} = send some calls to mlflow.
        """
        self.uri = uri or ""
        self.user = user or ""
        self.run_id = run_id or ""
        self.entry_point = entry_point
        self.mlflow = mlflow if isinstance(mlflow, dict) else {"all": True} if mlflow is True else {}
        self.inputs = {}
        self.outputs = {}
        self.parameters = {}

    def _to_absolute(self, uri: str):
        """
        Convert local paths to absolute paths except when they match a certain pattern.  "~" signifies the
        model's root path and can be used to access built-in model data.
        """
        # TODO test this
        # blank > means no change to supplied name
        if not uri:
            return ""
        # no changes to URIs
        if ":" in uri:
            return uri
        if uri.startswith("~/"):
            # specifically point to files within the sandbox
            return "./" + uri[1:]
        if uri.startswith("/"):
            # already absolute
            return uri
        # convert to absolute path
        return os.path.abspath(uri)

    def set_input(self, name: str, uri: str="", **kwargs):
        """
        Specify where data will come from for a particular named input.
        :param name:    Name of input.
        :param uri:     A path to a local file, or the URI of remote data.  Or, a URI specifying a sql or nosql data
                        source.
        :param kwargs:  Additional parameters to support the various data sources, following fsspec for file-like
                        sources.
        """
        self.inputs[name] = {"uri": self._to_absolute(uri), **kwargs}
        return self

    def set_output(self, name: str, uri: str="", **kwargs):
        """
        Specify where data should go for a particular named output.

        A format can be chosen by specifying "format".
          csv or tab -- remaining arguments are sent to pandas.to_csv()
          json - remaining arguments are sent to pandas.to_json()
          etc.

        :param name:    Name of output.
        :param uri:     See set_input()
        :param kwargs:  See set_input()
        """
        self.outputs[name] = {"uri": self._to_absolute(uri), **kwargs}
        return self

    def set_parameter(self, name: str, value):
        """
        Specify a value for one of the parameters.
        """
        self.parameters[name] = value
        return self

    def set_parameters(self, params: dict):
        """
        Specify values for multiple parameters.
        """
        self.parameters.update(params)
        return self

    def send_metrics_to(self, uri: str=None, mlflow: bool=None, **kwargs):
        """
        Determine where metrics will be stored (for read and write).  Parameters are equivalent to set_output(), in
        that metrics can be sent to a particular location.

        :param uri:         A URI or filename.
        :param mlflow:      Specify True to have the model log its metrics through MLFlow.
        :param kwargs:      Additional arguments.
        """
        if mlflow is not None:
            self.mlflow["metrics"] = bool(mlflow)
        self.inputs[METRICS_ALIAS] = {"uri": uri, **kwargs}
        self.outputs[METRICS_ALIAS] = {"uri": uri, **kwargs}
        return self

    def _generate_spec(self):
        spec = {
            "uri": self.uri,
            "user": self.user,
            "run_id": self.run_id,
            "entry_point": self.entry_point,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "parameters": self.parameters
        }
        if self.mlflow:
            spec["mlflow"] = self.mlflow
        return spec

    def run_method(self, method: typing.Callable, path: str=None):
        """
        As long as 'method()' uses dslibrary.instance(), and all calls through this method are single threaded, you can
        use this method, and it is very efficient.
        """
        # map parameters to method signature
        call_kwargs = {}
        sig = inspect.signature(method)
        sig_kwargs = None
        remaining_params = dict(self.parameters)
        for p_name, param in sig.parameters.items():
            if param.kind == inspect.Parameter.VAR_KEYWORD:
                sig_kwargs = True
                continue
            if p_name in remaining_params:
                value = remaining_params.pop(p_name)
                if param.annotation and param.annotation is not inspect.Parameter.empty:
                    value = param.annotation(value)
                call_kwargs[p_name] = value
        if sig_kwargs:
            call_kwargs.update(remaining_params)
        run_env = self.prepare_run_env(local_path=path)
        # as long as the method lets us send a custom dslibrary instance we can do that
        if "dsl" in sig.parameters or "dslibrary" in sig.parameters:
            dsl = dslibrary.instance(run_env)
            call_kwargs["dsl" if "dsl" in sig.parameters else "dslibrary"] = dsl
            method(**call_kwargs)
        else:
            # otherwise we assume method() calls dslibrary.instance()
            # - this approach is not thread safe
            # TODO is this approach even worth supporting???
            orig_env = {ENV_DSLIBRARY_TARGET: os.environ.get(ENV_DSLIBRARY_TARGET), ENV_DSLIBRARY_SPEC: os.environ.get(ENV_DSLIBRARY_SPEC)}
            try:
                # store specification
                for k, v in run_env.items():
                    os.environ[k] = v or ""
                # the method makes calls to dslibrary, following rules set above
                method(**call_kwargs)
            finally:
                # restore environment
                for k, v in orig_env.items():
                    os.environ[k] = v or ""

    def run_local(self, path: str, extra_env: dict=None):
        """
        Execute a python, R or notebook based model in a subprocess.
        """
        # verify target exists, split apart path
        if not os.path.exists(path):
            raise DSLibraryException(f"Path not found: {path}")
        folder, fn = os.path.split(path)
        f_base, f_ext = os.path.splitext(fn)
        # if only a path is specified we can look up 'entry_point' and run its official command
        cmd = None
        if os.path.isdir(path):
            folder, fn = path, ""
            meta = Metadata.from_folder(path)
            entry_point = self.entry_point or "main"
            if entry_point not in meta.entry_points:
                raise DSLibraryException(f"Entry point {entry_point} not found in model at {path}")
            cmd_str = meta.entry_points[entry_point].command
            if not cmd_str:
                raise DSLibraryException(f"Entry point {entry_point} for {path} does not define a command")
            cmd = split_command_line(cmd_str)
        # if we're not using metadata we have to infer how to execute the code
        if not cmd:
            cmd = self.infer_command_from_path(path)
        # work out environment variables
        env = {
            **self.prepare_run_env(local_path=folder),
            **(extra_env or {})
        }
        # call the model
        result = subprocess.run(cmd, cwd=folder, env=env, check=True)
        # TODO report failures in a more elegant way

    @staticmethod
    def infer_command_from_path(path: str):
        """
        When we only know the name of a source file we have to work out how to execute it.

        Used by run_local().
        """
        _, fn = os.path.split(path)
        _, f_ext = os.path.splitext(fn)
        f_ext = f_ext.lower()
        # if we're not using metadata we have to infer how to execute the code
        if f_ext == ".py":
            cmd = [sys.executable, path]
        elif f_ext == ".r":
            cmd = ["RScript", path]
        elif f_ext == ".ipynb":
            cmd = ["nbconvert", "--to", "notebook", "--execute", "--inplace", path]
        else:
            raise DSLibraryException(f"unrecognized executable extension: {f_ext} in {fn}")
        return cmd

    def prepare_run_env(self, rest_url: str=None, shared_volume: str=None, local_path: str=None, rest_access_token: str=None) -> dict:
        """
        Prepare environment variables for a run which encapsulate all of the settings generated by calls to this
        class.  Data science code running anywhere, with these environment variables set, can use dslibrary to read
        and write all of its data without having to know any details about data location, credentials or format.

        Three approaches are provided:
          * rest_url and rest_access_token - fill this in to have the target code use a REST service for data access.
          * shared_volume - fill this in to use a shared volume (i.e. a sidecar) for data access.
          * local_path - this option causes all inputs and outputs to default to files in the indicated folder, and
              there is no delegation of data access, it is all performed by the process running the target code.

        In a high security scenario which isolates the data science code from the credentials and other data source
        details:
          * Send the ENV_DSLIBRARY_SPEC value to a secure service (a REST service indicated by rest_uri, or a sidecar
            sharing the volume 'shared_volume' with the target code).
          * Send the other environment variables to the target code.
          * The target code calls dslibrary methods, which communicate with the data service, and the data service
            performs all reads and writes based on the environment data it has been sent.

        The Kubernetes sidecar approach involves running a container alongside your target code's container, and having
        them both mount the same shared, ephemeral volume.  The appropriate environment variables are set for each, and
        voila, the target code is able to perform all its data access without having exposed any sensitive information.

        :param rest_url:            URL of REST service.
        :param shared_volume:       Path to shared volume.
        :param local_path:          Local path.
        :param rest_access_token:   Access token to secure communications.
        :return:  Environment variables to set, as a {}.
        """
        env = {}
        if shared_volume:
            env[ENV_DSLIBRARY_TARGET] = f"volume:{shared_volume}"
        elif rest_url:
            env[ENV_DSLIBRARY_TARGET] = rest_url
            if rest_access_token:
                env[ENV_DSLIBRARY_TOKEN] = rest_access_token
        elif local_path:
            env[ENV_DSLIBRARY_TARGET] = f"local:{local_path}"
        env[ENV_DSLIBRARY_SPEC] = json.dumps(self._generate_spec())
        return env

    def run_mlflow(self, model_uri: str):
        """
        Use mlflow.run() to execute an MLFlow model.

        The trick will be how to set the environment variables in the remote model such that the interception takes
        place and sends data back to us.  Could initially only be supported when running locally with an environment
        variable.
        """
        # TODO code me
        # TODO I don't see a way to have MLFlow deliver extra environment variables!
