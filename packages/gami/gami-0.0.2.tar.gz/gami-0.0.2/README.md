# gami

Data definition specification and generation.

## Introduction

Gami is a framework for defining data structures. Gami makes it easy to define what your data looks like and share that information between multiple applications.

- Create variables
  - Define variable type
  - Define allowed values for variable
- Assign variables to DataFrames, called Entities
- Create Entities by referencing existing data
- Decompose existing data into allowed sets of values for variables
- A lot of this is handled already by `featuretools`

## Usage

import gami

sales = gami.entity(
  {
    "id": str,
    "name": str,
  }
 )
