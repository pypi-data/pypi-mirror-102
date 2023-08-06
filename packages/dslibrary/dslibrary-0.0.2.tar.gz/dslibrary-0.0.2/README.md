# DSLIBRARY

## Data Science Framework and Abstractions

This is a 'runtime' library for models and other data science code which "abstracts" all of the normal dependencies that
such code usually has.

For instance, data cleaning code reads the input data from somewhere and writes it somewhere.
Hardcoding the filenames is problematic, but by calling an abstract file stream opening method we can re-use the same
code when the files are on local disk, in an S3 bucket, or have different names.

One goal is to make the data science code ("model") as situation-agnostic as possible, as testable as possible, and as
reusable as possible.  Another is to simplify that code with a few helper functions that seem to almost always be
needed.

If you use dslibrary with no configuration it will revert to very straightforward behaviors that a person would expect
while doing local development.  But it can be configured to operate in a wide range of environments.

There are two supported ways to communicate with external sources of data:
  1) REST APIs: uses 'requests' to communicate with a REST API
  2) Shared volume: all communication goes through a filesystem volume (use a sidecar to manage the data)


## Q & A

Q: Why not just define data inputs and outputs as parameters?

A: The work being saved to load a dataframe from a given input source:
     * collect & parse command line arguments
     * obtain a file stream for whichever local or cloud based source is specified
     * choose a pandas read function based on the file format
     * supply additional parameters based on the specifics of that file format
  with dslibrary:
     * dsl.load_dataframe("my_input")
     * caller deals with changes to data location, file format, etc..


# COPYRIGHT

(c) Accenture 2021
