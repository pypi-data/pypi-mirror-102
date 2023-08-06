# Democritus Algorithms (a.k.a. d8s-algorithms)

[![PyPI](https://img.shields.io/pypi/v/d8s-algorithms.svg)](https://pypi.python.org/pypi/d8s-algorithms)
[![CI](https://github.com/democritus-project/d8s-algorithms/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-algorithms/actions)
[![Lint](https://github.com/democritus-project/d8s-algorithms/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-algorithms/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-algorithms/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-algorithms)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with algorithms.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Installation

```
pip install d8s-algorithms
```

## Functions

  - ```python
    def amb(validation_function: Callable[..., bool], *args: Any) -> Iterable[Any]:
        """."""
    ```
  - ```python
    def depth_first_traverse(
        data: Any,
        get_children_function: Callable[[Any], Optional[Iterable]],
        *,
        collect_items_function: Optional[Callable[[Any], Any]] = None
    ) -> Iterable[Any]:
        """Traverse the data in a depth-first manner.
    
    The get_children_function specifies how children will be identified from each node of the data.
    The collect_items_function, if provided, allows you to collect items from the data by...
     returning them from the collect_items_function."""
    ```
  - ```python
    def breadth_first_traverse(
        data: Any,
        get_children_function: Callable[[Any], Optional[Iterable]],
        *,
        collect_items_function: Optional[Callable[[Any], Any]] = None
    ) -> Iterable[Any]:
        """Traverse the data in a breadth-first manner.
    
    The get_children_function specifies how children will be identified from each node of the data.
    The collect_items_function, if provided, allows you to collect items from the data by...
     returning them from the collect_items_function."""
    ```
  - ```python
    def genetic_algorithm_run(
        data: Iterable[Any],
        scoring_function: Callable[[Any], Union[int, float]],
        selection_function: Callable[[Dict[Any, Union[int, float]]], Iterable[Any]],
        mutation_function: Callable[[Iterable[Any]], Iterable[Any]],
        max_epochs: int,
    ) -> Dict[Any, Union[int, float]]:
        """."""
    ```
  - ```python
    def genetic_algorithm_best_mutation_function(
        starting_values: Iterable[Any],
        generations: int,
        scoring_function: Callable[[Any], Union[int, float]],
        mutation_functions: List[Callable[[Any], Any]],
    ):
        """Find the best mutation function.
    
    The best function is the one which produces values from the starting values...
     that score the highest (as measured by the scoring_function) after generations."""
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