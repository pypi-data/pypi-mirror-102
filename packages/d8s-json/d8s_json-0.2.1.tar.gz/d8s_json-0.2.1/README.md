# Democritus JSON

[![PyPI](https://img.shields.io/pypi/v/d8s-json.svg)](https://pypi.python.org/pypi/d8s-json)
[![CI](https://github.com/democritus-project/d8s-json/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-json/actions)
[![Lint](https://github.com/democritus-project/d8s-json/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-json/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-json/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-json)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with JSON.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def json_files(directory_path: str) -> List[str]:
        """Find all json files in the given directory_path."""
    ```
  - ```python
    def json_read(json_string: str):
        """."""
    ```
  - ```python
    def json_read_first_arg_string_decorator(func):
        """Load the first argument as JSON (if it is a string)."""
    ```
  - ```python
    def json_write(file_path, json_content, **kwargs):
        """Write the json_content to the file_path."""
    ```
  - ```python
    def json_prettify(json_object):
        """."""
    ```
  - ```python
    def json_pretty_print(json_string):
        """Pretty print the json so it is readable."""
    ```
  - ```python
    def json_search(json_data, value_to_find):
        """Find the value_to_find in the json_data."""
    ```
  - ```python
    def json_structure(json_data):
        """Print out the structure of the given json blob."""
    ```
  - ```python
    def json_path_dot_notation_to_bracket_notation(json_path_dot_notation: str) -> str:
        """Convert the given json path from dot notation to bracket notation (foo.bar -> ["foo"]["bar"])."""
    ```
  - ```python
    def json_path_bracket_notation_to_dot_notation(json_path_dot_notation: str) -> str:
        """Convert the given json path from bracket notation to dot notation (["foo"]["bar"] -> foo.bar)."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
