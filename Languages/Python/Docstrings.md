[[Python]]

[Google Style Guide - Comments & Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)


[[#Overview]]
- [[#Display]]

[[#pydoc.py]]

[[#Package Level]]
[[#Module Level]]
[[#Class Level]]
[[#Function / Method Level]]

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
