# Kata Range Pair Programming
This assignment consists of making the Kata Range programming using TDD and Python, while implementing the Pair Programming paradigm. This application also includes a demo application located in [this](https://github.com/pamendez/Range-Kata-App) repository that consumes the pip package that contains the Range component without the unit testing using the [Pytest](https://docs.pytest.org/en/7.1.x/) testing framework.

## Table of contents
1. [About](#1-about)
2. [Requirements](#2-requirements)
3. [Authors](#3-authors)

## 1. About
This repository contains a component that follows [this](https://codingdojo.org/kata/Range/) kata, which contains the following operations:

* intergerContainsRange: Checks whether a range contains certain elements of a set.
* containsRange: Checks whether a range is contained in another range.
* getAllPoints: Gets all the points in a specified range.
* endPoints: Gets the endpoints, or limits, in a range.
* overlapsRange: Checks whether a part of the range is inside another range.
* Equals: Checks whether two ranges are the same.

## 2. Requirements
After cloning or downloading the repository, in order to install the component, make sure you install the following programs:

* Python 3.10.1 or greater, found [here](https://www.python.org/downloads/).
* pip 21.2.4 or greater, which comes with most Python installs, found [here](https://pypi.org/project/pip/). 

Because the component is a simple class library, no interface to access the class methods was made for this project. However, if you want to run the unit tests, execute the following commands:

```
pytest krange_test.py
```

## 3. Authors
| # | Name | Id |
| ---- | ---- | ---- |
| 1 | Pedro Arturo Mendez Cruz | 1088438
| 2 | Jean Michael Cuadrado | 1076992
| 3 | Belkis Yazmin Vasquez Peña | 1085273
