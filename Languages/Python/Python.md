#language

Uses [[Typing#Duck Typing]]

[Python Package Index](https://pypi.org) - Finds packages to install

Contents
- [[#Mixin]]
- [[#Virtual Environments]]
- [[#args & kwargs]]
- [[#Modules / Packages]]
- [[#Type Hinting]]

---
## Mixin

A class that provides additional functionality to other classes without necessarily being part of the inheritance hierarchy.

A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

1. You want to provide a lot of optional features for a class.
2. You want to use one particular feature in a lot of different classes.

```Python
class SimpleRepr(object):
    """ A mixin implementing a simple __repr__ to show all attributes of a class """
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

class Example(SimpleRepr):
    def __init__(self, a, b, c=None):
        self.a, self.b, self.c = a, b, c

e = Example(5, 10) 
print(e) # <Example {'a': 5, 'b': 10, 'c': None}>        
```

---
## Virtual Environments

[Setup Guide]([https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/))

Virtual environments isolate a project from the global python install.
 
This is allows you to add and test packages / versions without conflicting with the global install.

- Can also open the command palette in VSCode (F1) and create an environment
- Need to make sure we have the venv version of python selected. In VSCode press F1 and look for python interpreter. Locate python in .venv Scripts

```
// Creation in cmd prompt
cd desktop
mkdir [Project_Name] (OR create a new folder and cd into it)
python -m venv .venv

// open with VSCode
code .

// In a terminal window
cd .venv\Scripts
./activate
// should say (.env) before location in terminal

// OR, in a powershell terminal
.\.venv\Scripts\Activate.ps1
```

### Requirements

python uses a file called ```requirements.txt``` to store which  packages need to be installed.

```
// Save all dependancies
pip freeze > requirements.txt
```

To install
pip install -r requirements.txt

### Fixes

```
“Defaulting to user installation because normal site-packages is not writeable.”

Have to run **VSCODE** as Administrator
```


```
If there is a problem.

Run windows powershell as administrator

>>> Get-ExecutionPolicy (checks if it is restricted)

>>> set-executionpolicy remotesigned
```


```
if pip list fails… → Fatal error in launcher: Unable to create process using

>>> python -m pip install --upgrade pip
```

---
## args & kwargs

**NOTE**: args & kwargs are used by convention but could be anything.

```python
def order_pizza(size, *toppings, **details):
    print(f"{size} pizza")
    
    print("Toppings...")
    for topping in toppings:
        print(f"- {topping}")
        
    print("Extra details...")
    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("Large", "Pepperoni", "Mushrooms", "Ham", tip=5, delivery=True)
```

```
Large pizza
Toppings...
- Pepperoni
- Mushrooms
- Ham
Extra details...
- tip: 5
- delivery: True
```

---
## Modules / Packages

- **Module**
	A single `.py` file containing Python functions, classes, or variables. Essentially, any Python script is a module.
- **Package**
	A collection of modules organized into a directory with an `__init__.py` file (which can be empty or contain initialization code). This helps Python treat the directory as a package.
- **Library**
	A broader term, often referring to a collection of packages and modules that provide specific functionality. For example, NumPy or Pandas are libraries containing multiple modules and packages.

Got it! Since it's a separate GitHub project, you'll just need to make sure your Python environment can find it when you use it in another project. A couple of ways to do that:

### Installation

Install a package from disk
`pip install path/to/your/package`

Install from GitHub
`pip install git+https://github.com/CraigMason19/music_theory`

Use without installation. Modify sys.path temporarily
```python
import sys
sys.path.append("path/to/your/package")
import my_package
```

---
## Type Hinting

Python can have type hinting to make code editors provide intellisense, context, and provide warnings.

**NOTE:** Although you get a warning, it will still run. Python doesn't care but code editors will

In VSCode
- Pylance
	- settings > type checking mode > basic (or whatever)

```python
from typing import Final, Iterable, Sequence, TypeAlias, NewType, Union

x: int = 'hello' 
print(x) # hello

# Unions
num_or_str: Union[str, int] = 10
num_or_str_2: int | str = 20

# Functions
# NOTE: Although Python return none by default, it is good practice to specify the return type when using annotations
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# Lists
elements: list[str] = ["apple", "banana", "cherry"]

# Constants
# NOTE: Not actually constant, can be changed but will give a warning
ONE_MILLION: Final[int] = 10**6
print(ONE_MILLION)

# Iterables
def list_elements(elements: Iterable[str]) -> None:
    for i, e in enumerate(elements, start=1):
        print(i, e, sep=': ')

# TypeAlias
OptionalString: TypeAlias = str | None

a: OptionalString = "A"
b: OptionalString = None

print(a, b) # A None  

# In Python 3.12
type OptionalNumber = int | float | None
```

---
