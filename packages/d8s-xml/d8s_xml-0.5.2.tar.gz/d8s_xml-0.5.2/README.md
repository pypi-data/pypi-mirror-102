# Democritus Xml

[![PyPI](https://img.shields.io/pypi/v/d8s-xml.svg)](https://pypi.python.org/pypi/d8s-xml)
[![CI](https://github.com/democritus-project/d8s-xml/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-xml/actions)
[![Lint](https://github.com/democritus-project/d8s-xml/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-xml/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-xml/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-xml)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with XML.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def xml_read(xml_path: str) -> Element:
        """Read the XML from the given path (which can be a URL, file path, or string) and return an xml Element tree."""
    ```
  - ```python
    def is_xml(possible_xml: str) -> bool:
        """."""
    ```
  - ```python
    def xml_as_string(xml_input: Element) -> str:
        """Convert the given xml_input to a string."""
    ```
  - ```python
    def xml_read_first_arg_string(func):
        """Return an XML element for first argument (if it is a string)."""
    ```
  - ```python
    def stringify_first_arg_xml_element(func):
        """If the first arg is an XML element, send its string representation into the function."""
    ```
  - ```python
    def xml_structure(xml_input: StringOrXmlElement) -> Dict[str, dict]:
        """."""
    ```
  - ```python
    def xml_to_json(xml_input: StringOrXmlElement) -> Dict[str, List[Dict[str, List[Dict[str, str]]]]]:
        """Convert the xml to json using https://gitlab.com/fhightower/html-to-json."""
    ```
  - ```python
    def xml_text(xml_input: StringOrXmlElement) -> str:
        """Convert the given xml_input to a string."""
    ```
  - ```python
    def xml_file_names(path: str) -> List[str]:
        """Find all xml files in the given directory."""
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
