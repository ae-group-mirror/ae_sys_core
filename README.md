<!--
  THIS FILE IS EXCLUSIVELY MAINTAINED IN THE NAMESPACE ROOT PACKAGE. CHANGES HAVE TO BE DONE THERE.
  All changes will be deployed automatically to all the portions of this namespace package.
-->
# systems portion of ae namespace package

[![GitLabPipeline](https://img.shields.io/gitlab/pipeline/ae-group/ae_systems/master?logo=python)](
    https://gitlab.com/ae-group/ae_systems)
[![PyPIVersion](https://img.shields.io/pypi/v/ae_systems)](
    https://pypi.org/project/ae-systems/#history)

>The portions (modules and sub-packages) of the Application Environment for Python are within
the `ae` namespace and are providing helper methods and classes for to develop
full-featured applications with Python.

[![Coverage](https://ae-group.gitlab.io/ae_systems/coverage.svg)](
    https://ae-group.gitlab.io/ae_systems/coverage/ae_systems_py.html)
[![MyPyPrecision](https://ae-group.gitlab.io/ae_systems/mypy.svg)](
    https://ae-group.gitlab.io/ae_systems/lineprecision.txt)
[![PyLintScore](https://ae-group.gitlab.io/ae_systems/pylint.svg)](
    https://ae-group.gitlab.io/ae_systems/pylint.log)

[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_systems)](
    https://pypi.org/project/ae-systems/)
[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_systems)](
    https://pypi.org/project/ae-systems/)
[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_systems)](
    https://pypi.org/project/ae-systems/)
[![PyPIFormat](https://img.shields.io/pypi/format/ae_systems)](
    https://pypi.org/project/ae-systems/)
[![PyPIStatus](https://img.shields.io/pypi/status/ae_systems)](
    https://libraries.io/pypi/ae-systems)
[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_systems)](
    https://pypi.org/project/ae-systems/#files)


## installation

Execute the following command for to use the ae.systems module in your
application. It will install ae.systems into your python (virtual) environment:
 
```shell script
pip install ae-systems
```

If you instead want to contribute to this portion then first fork
[the ae-systems repository at GitLab](https://gitlab.com/ae-group/ae_systems "ae.systems code repository"),
then pull it to your machine and finally execute the following command in the root folder
of this repository (ae_systems):

```shell script
pip install -e .[dev]
```

The last command will install this module portion into your virtual environment, along with
the tools you need to develop and run tests or for to extend the portion documentation.
For to contribute only to the unit tests or the documentation of this portion replace
the setup extras key `dev` in the above command with `tests` or `docs` respectively.


## namespace portion documentation

More info on the features and usage of this portion are available at
[ReadTheDocs](https://ae.readthedocs.io/en/latest/_autosummary/ae.systems.html#module-ae.systems
"ae_systems documentation").

<!-- Common files version 0.0.34 deployed (with 0.0.34)
     to the ae_systems module version 0.0.11.
-->