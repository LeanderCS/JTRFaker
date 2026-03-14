# JTRFaker

[![](https://img.shields.io/pypi/v/jtrfaker?style=flat-square&label=version)](https://pypi.org/project/jtrfaker/)
[![](https://img.shields.io/pypi/pyversions/jtrfaker)](https://pypi.org/project/jtrfaker/)
[![](https://img.shields.io/github/license/LeanderCS/jtrfaker)](https://github.com/LeanderCS/jtrfaker/blob/main/LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/LeanderCS/jtrfaker/test.yaml?branch=main&style=flat-square&label=tests)](https://github.com/LeanderCS/jtrfaker/actions)
[![](https://static.pepy.tech/badge/jtrfaker/month)](https://pypi.org/project/jtrfaker/)
[![](https://static.pepy.tech/badge/jtrfaker)](https://pypi.org/project/jtrfaker/)

The `JTRFaker` package is a utility that is focused on generating fake data for testing and
development purposes. It leverages the power of the Faker library to create realistic yet
random data that can be used to populate your database during `development` or for
`testing` your application's functionality.

## Installation

```bash
pip install JTRFaker
```

## Usage

The usage varies depending on the type of data you want to generate. The following are the
different types of data that can be generated using the `JTRFaker` module:

1. [`ModelFaker`](src/ModelFaker/README.md) - Database entries based on sqlalchemy models with lots of different options.
