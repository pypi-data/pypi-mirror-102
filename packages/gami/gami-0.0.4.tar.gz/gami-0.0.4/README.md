# gami

[![pytest](https://github.com/WesRoach/gami/workflows/pytest/badge.svg)](https://github.com/WesRoach/gami/actions?query=workflow%3Apytest)
[![Linting](https://github.com/WesRoach/gami/workflows/Linting/badge.svg)](https://github.com/WesRoach/gami/actions?query=workflow%3ALinting)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/WesRoach/gami/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Define data structure and produce fake data.

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/WesRoach/gami)

## Introduction

Gami is a framework for defining DataFrame structures. Gami makes it easy to define what your data looks like and share that information between multiple applications.

- Create variables
  - Define variable type
  - Define allowed values for variable
- Assign variables to DataFrames, called Entities
- Create Entities by referencing existing data
- Decompose existing data into allowed sets of values for variables
- A lot of this is handled already by `featuretools`

## Usage

```python
import gami

sales = gami.entity(
    {
        "id": str,
        "name": str,
    }
)
```
