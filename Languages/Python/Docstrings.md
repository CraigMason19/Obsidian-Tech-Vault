[[Python]]

[Google Style Guide - Comments & Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

---

[[#Overview]]
- [[#Display]]

[[#pydoc.py]]

Custom notes
- [[#Package Level]]
- [[#Module Level]]
- [[#Class Level]]
- [[#Function / Method Level]]

[[#Official Python Examples]]
- [[#Official Python Examples#pickle module]]
- [[#Official Python Examples#counter module]]

---
## Overview

Docstrings are a string in a class / module / function / method explaining how it works.
- Explains to others how your code works
- Explains how other's code works
- Helps you remember what a function does going back to own code
### Display

docstrings can be displayed via the inbuilt `help` and `__doc__`

```python
def add(a, b):
	"""
	Adds two numbers
	
	returns the result
	"""
    ...

# Prints to console
>>> help(add)
	
Help on function add in module __main__:
	
add(a, b)
    Adds two numbers

# Returns a string
>>> print(add.__doc__)
	
Adds two numbers
	
returns the result
```

---
## pydoc.py

Python's built-in documentation tool.

Display all docstrings in a file
```
python -m pydoc python_file
```

Open docstring info in your browser
**NOTE:**  the browser index is built from Python's module search paths (`sys.path`)
```
python -m pydoc -b
```

Generate an HTML file of the docstrings
```
python -m pydoc -w python_file
```

---
## Package Level

Things to include
- A brief overview of the package
- A brief overview of the modules

```python
"""
music
-----

Provides tools for working with musical notes, chords,
and scales.

Modules:
    notes: 
	    Defines musical notes and related operations.
    chords: 
	    Defines musical chords and chord types.
    scales: 
	    Defines musical scales and their intervals.
"""
```

---
## Module Level

**~={red}NOTE=~:** Ignore `_` or `__`

Things to include
- Filename
- Description
- Example (if needed)
- Globals
- Classes
- Functions

```python
"""
place_values.py
---------------

Provides tools for decomposing positive integers into their
individual place-value components.

Example:
	...

Globals:
    DEFAULT_BASE: 
        The default numerical base.
        
Classes:
    PlaceValues: 
        Represents an integer through its place values.

Functions:
    decompose_number: 
        Decomposes an integer into place values.
"""
```

---
## Class Level

**~={red}NOTE=~:** Ignore `_` or `__`

Things to include
- Description
- Example (if needed)
- Class Attributes
- Attributes / Instance Attributes
- Properties

```python
class PlaceValues:
    """
    Represent the digits of an non-negative integer by their place values.
    
    Numbers are split into thousand, hundred, ten, and unit digits.
    
    Example:
        >>> value = PlaceValues(1600)
        >>> value.thousands
        1
        >>> value.hundreds
        6
        >>> value.tens
        0
        >>> value.units
        0
        >>> value.decompose()
        [1000, 600, 0, 0]
        
    Attributes:
        number (int): 
            The integer to decompose into place-value digits.
            
    Properties:
        thousands (int): 
            The thousands digit.
        hundreds (int): 
            The hundreds digit.
        tens (int): 
            The tens digit.
        units (int): 
            The units digit.
    """
```

---
## Function / Method Level

Things to include
- Description
- Example (if needed)
- Args (*kwargs, is an Args)
- Raises
- Returns (Yields for generators)

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
## Official Python Examples

### pickle module

```python
"""Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(bytes) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

"""
```

### counter module

```python
'''This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

'''
```

Counter Class

```python
Dict subclass for counting hashable items. Sometimes called a bag
or multiset. Elements are stored as dictionary keys and their counts
are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15
>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0
>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9
>>> c.clear()                       # empty the counter
>>> c
Counter()
Note: If a count is set to zero or reduced to zero, it will remain
```