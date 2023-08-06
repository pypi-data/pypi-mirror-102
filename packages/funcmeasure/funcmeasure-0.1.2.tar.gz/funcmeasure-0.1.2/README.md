# funcmeasure

![PyPI - package version](https://img.shields.io/pypi/v/funcmeasure?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/funcmeasure?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/funcmeasure?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/funcmeasure?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_funcmeasure?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_funcmeasure?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_funcmeasure?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_funcmeasure?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_funcmeasure?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_funcmeasure?label=repo%20license&style=flat-square)

## Description

Measure and compare function execution times

## Install

~~~~bash
pip install funcmeasure
# or
pip3 install funcmeasure
~~~~

## Usage

~~~~python
from funcmeasure import measure, FunctionStats, TableFormat

def f1():
    5**2

def f2():
    5**2**10

def f3():
    5**2**2**2

# stats = measure([f1, (f2, 'second'), f3], times=1000)
# or
stats = measure(
    {
        f1: None,
        f2: 'second',
        f3: None
    },
    times=1000
)

# prints
#
# Ran 3 functions. 1000 times each.
#
# ╒════╤════════╤════════════╤══════════════╤═════════════╤══════════════╤═════════════╕
# │    │   Name │   Avg (ms) │   Total (ms) │   Best (ms) │   Worst (ms) │   Benchmark │
# ╞════╪════════╪════════════╪══════════════╪═════════════╪══════════════╪═════════════╡
# │  0 │     f3 │   0.002123 │     2.122589 │    0.001892 │     0.007872 │             │
# ├────┼────────┼────────────┼──────────────┼─────────────┼──────────────┼─────────────┤
# │  1 │     f1 │   0.002282 │     2.281747 │    0.001952 │     0.062483 │      ~1.07x │
# ├────┼────────┼────────────┼──────────────┼─────────────┼──────────────┼─────────────┤
# │  2 │ second │   0.004946 │     4.946447 │    0.004395 │     0.053278 │      ~2.33x │
# ╘════╧════════╧════════════╧══════════════╧═════════════╧══════════════╧═════════════╛
~~~~

## Dependencies

[jsoncodable](https://pypi.org/project/jsoncodable), [tabulate](https://pypi.org/project/tabulate)