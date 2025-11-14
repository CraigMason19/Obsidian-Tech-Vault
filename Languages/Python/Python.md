#language

Uses [[Typing#Duck Typing]]

[Python Package Index](https://pypi.org) - Finds packages to install

Contents
- [[#Mixin]]
- [[#Virtual Environments]]
- [[#args & kwargs]]
- [[#Modules / Packages]]
- [[#Type Hinting]]
- [[#Docstrings]]
- [[#F-Strings]]

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

// OR, 
// Activate venv in a powershell terminal
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

```
pip install git+https://github.com/CraigMason19/music_theory
```

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
## Docstrings

A string in a class / module / function / method explaining how it works
#### Module Level

```python
"""
Defines the KeyType enumeration for musical keys, representing either major or 
minor.

This module provides:
- An Enum class `KeyType` with two values: Major and Minor.
- Utility methods to list all key types, select a random key type, and retrieve
  the parallel (opposite) key.
- String representations for clean display and debugging.

Example:
    >>> from music_theory.key_type import KeyType
    >>> kt = KeyType.Major
    >>> print(f"Selected key: {kt}, Parallel: {kt.parallel}")
    Selected key: Major, Parallel: Minor
"""
```
#### Class Level

```python
""" A class representing a musical chord. 
    
Attributes:
	root:
		The Note the rest of the chord is built from.
	type:
		A ChordType. 
	notes:
		An array containing the root, 3rd(Major or Minor) & the fifth

Methods:
	__init__(self, root, chord_type):
		Constructs the chord.
	random(cls):
		A class method to return a random chord.
	__eq__(self, other):
		Compares two chords.
	notation(self):
		Returns the chord's notation without the Note.
	quality(self):
		An alias for notation. Returns the chord's notation without the Note.
	add9(self):
		Returns an array of the chord's notes with the added 9th
	add11(self):
		Returns an array of the chord's notes with the added 11th
	add13(self):
		Returns an array of the chord's notes with the added 13th
	__str__(self):
		Returns a string representation of the Chord.
	__repr__(self):
		Returns a string representation of the Chord.
"""
```
#### Function / method level

```python
def unique_notes_in_chord(*args):
"""
Collects all unique notes from the given Chords and returns them as a 
list, sorted by the the Notes enumeration value.

Example:
    >>> unique_notes_in_chords(
	...     Chord(Note.A, ChordType.Major),
	...     Chord(Note.A, ChordType.Minor)
	... )
	[Note.C, Note.Db, Note.E, Note.A]
	
	>>> from music_theory.key_type import KeyType
    >>> kt = KeyType.Major
    >>> print(f"Selected key: {kt}, Parallel: {kt.parallel}")
	Selected key: Major, Parallel: Minor

Args:
	*args (Chord): 
		One or more Chord objects to extract notes from.
		
	tuning (list[Note]):
		A list of notes representing each string of the instrument.
		
Raises:   FIRST"!!!!!!!!!!!! BEFORE RETURNS
	ValueError:
		If `fret` is a negative.	
		
Returns:
	list[Note]: 
		A list of unique Notes sorted by their value.
""" 



from typing import Self # 3.11
def __eq__(self, other: Self) -> bool:

```

---
## F-Strings

```python
# Decimal places & percentages
print(f'{3.141592:.2f}') # 3.14

print(f'{0.75:.2%}') # 75.00%
print(f'{0.75:.0%}') # 75%


# Leading zeros. 0001 0011 0111 1111
for _ in [1, 11, 111, 1111]:
    print(f'{_:04}')


# Thousands seperator
print(f'{1000000000000000000:_}')
print(f'{1000000000000000000:,}')


# Alignment
print(f'Result -> {"hello":<10}...') # 'Result -> hello     ...'
print(f'Result -> {"hello":^10}...') # 'Result ->   hello   ...'
print(f'Result -> {"hello":>10}...') # 'Result ->      hello...'

print(f'Result -> {"hello":_^10}...') # 'Result -> __hello___...'
```
### Dynamic Formatting

Can also dynamically control the formatting by using nested curly brackets

```python
precision = 4
print(f'{3.141592:.{precision}f}') # 3.1416
```
### Debugging

Can also be used for quickly debugging

```python
x, y = 'Hello', 'Craigy'

print(f'{x=} {y=}')     # x='Hello' y='Craigy'
print(f'{x = } {y = }') # x = 'Hello' y = 'Craigy'

print(f'{len(x)=} {len(y)=}') # len(x)=5 len(y)=6
```

---
