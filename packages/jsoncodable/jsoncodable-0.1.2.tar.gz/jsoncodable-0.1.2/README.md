# jsoncodable

![PyPI - package version](https://img.shields.io/pypi/v/jsoncodable?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/jsoncodable?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/jsoncodable?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/jsoncodable?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_jsoncodable?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_jsoncodable?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_jsoncodable?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_jsoncodable?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_jsoncodable?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_jsoncodable?label=repo%20license&style=flat-square)

## Description

Easily create object from any dict/jsonstr/jsonfile and dict/jsonstr/jsonfile from any object

From v0.1.0 it is based on [jsonpickle](https://github.com/jsonpickle/jsonpickle)

## Install

~~~~bash
pip install jsoncodable
# or
pip3 install jsoncodable
~~~~

## Usage

~~~~python
from jsoncodable import JSONCodable

class BirthDay(JSONCodable):
    def __init__(
        self,
        month: int,
        day: int
    ):
        self.month = month
        self.day = day

class Person(JSONCodable):
    def __init__(
        self,
        name: str,
        birth_month: int,
        birth_day: int
    ):
        self.name = name
        self.birth_day = BirthDay(birth_month, birth_day)

person = Person(
    name='John',
    birth_month=7,
    birth_day=7
)


person.jsonprint()

# prints
#
# {
#     "name": "John",
#     "birth_day": {
#         "month": 7,
#         "day": 7
#     }
# }


Person.load(person.json).jsonprint()

# prints
#
# {
#     "name": "John",
#     "birth_day": {
#         "month": 7,
#         "day": 7
#     }
# }
~~~~

## Dependencies

[jsonpickle](https://pypi.org/project/jsonpickle), [noraise](https://pypi.org/project/noraise)