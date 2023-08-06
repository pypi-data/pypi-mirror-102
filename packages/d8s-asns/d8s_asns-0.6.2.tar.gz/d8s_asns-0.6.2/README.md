# Democritus Asns

[![PyPI](https://img.shields.io/pypi/v/d8s-asns.svg)](https://pypi.python.org/pypi/d8s-asns)
[![CI](https://github.com/democritus-project/d8s-asns/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-asns/actions)
[![Lint](https://github.com/democritus-project/d8s-asns/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-asns/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-asns/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-asns)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with asns.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def asn_standardize(as_number: str) -> Optional[str]:
        """Standardize the ASN format."""
    ```
  - ```python
    def standardize_asn_decorator(func):
        """Standardize the first argument as an ASN."""
    ```
  - ```python
    def asn_announced_prefixes(as_number: str) -> Iterable[str]:
        """."""
    ```
  - ```python
    def asn_adjacent_asns(as_number: str) -> Iterable[str]:
        """."""
    ```
  - ```python
    def asns_find(text: str) -> Iterable[str]:
        """Parse ASNs from the given text."""
    ```
  - ```python
    def asns() -> Iterable[Tuple[str, str]]:
        """Get a list of ASNs from http://bgp.potaroo.net/as1221/asnames.txt."""
    ```
  - ```python
    def asn_number(as_number: str) -> int:
        """Get the number value of the given ASN."""
    ```
  - ```python
    def asn_is_private(as_number: str) -> bool:
        """Check if the given ASN is private."""
    ```
  - ```python
    def asns_private_numbers() -> Iterable[int]:
        """Return the reserved (private) ASN numbers.
    
    Data is collected from:
    
    https://www.iana.org/assignments/iana-as-numbers-special-registry/iana-as-numbers-special-registry.xhtml
    
    This function only returns the private ASN numbers.
    The `asns_private_ranges` function returns more information about the private ASN ranges."""
    ```
  - ```python
    def asns_private_ranges() -> List[Dict[str, str]]:
        """Return the reserved (private) ASN ranges.
    
    Data is collected from:
    
    https://www.iana.org/assignments/iana-as-numbers-special-registry/iana-as-numbers-special-registry.xhtml"""
    ```
  - ```python
    def asn_name(as_number: str) -> Optional[str]:
        """Get the name of the given asn."""
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
