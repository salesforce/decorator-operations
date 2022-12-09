# Decorator Operations

This project started from the need to have simple debounce and throttle annotations in Python.

The idea came from a [github discussion thread](https://gist.github.com/walkermatt/2871026).

Most of the annotations are an adapation of [RxJS operators](https://rxmarbles.com/). Feel free to contribute by adding a missing operator, or even a new one ! And / or opening issues about what you would like to see next.
 
## How to install

If you want to install this project, you may install it directly from this repository using pip:
```sh
pip install 'git+https://github.com/salesforce/decorator-operations'
```

Alternatively, you may clone this repo, `cd` into it, then run
```sh
pip install .
```
 
## Usage

Typical package usage will be:

```python
from decoratorOperations import annotation

@annotation(<parameter>)
def function(x,y,z):
    ...
```

### Available functions

#### Debounce
Decorator that will debounce a function so that it is called after wait_time seconds.
If it is called multiple times, will wait for the last call to be debounced and run only this one.
See the test_debounce.py file for examples.

```python
from decoratorOperations import debounce

@debounce(0.5)
def function(x,y,z):
    ...
```

#### Throttle

Decorator that will throttle a function so that it is called only once every wait_time seconds
If it is called multiple times, will run only the first time.
See the test_throttle.py file for examples.

```python
from decoratorOperations import throttle

@throttle(0.5)
def function(x,y,z):
    ...
```

#### Ignore
Decorator that will make a function call be ignored.

```python
from decoratorOperations import ignore

@ignore()
def function(x,y,z):
    ...
```

#### Filter
Decorator that will filter a function given its parameters and the lambda function specified.
See the test_filter.py file for examples

```python
from decoratorOperations import filter

@filter(lambda x, y, z: x > 2)
def function(x,y,z):
    ...
```

## Development
Run unit tests: pytest

Code must be formatted with black. You can reformat all code before submission with this command: `black .`


## Code of conduct

Salesforce open-source projects are committed to providing a friendly, safe, and welcoming environment for all. 

You may read more in the [Code of Conduct](./CODE_OF_CONDUCT.md).

The goal of this code of conduct is to specify a baseline standard of behavior so that people with different social values and communication styles can work together effectively, productively, and respectfully in our open source community. It also establishes a mechanism for reporting issues and resolving conflicts.

All questions and reports of abusive, harassing, or otherwise unacceptable behavior in a Salesforce open-source project may be reported by contacting the Salesforce Open Source Conduct Committee at ossconduct@salesforce.com.
