
## Module



```
Start with a one-line summary of what the module does.

List key components (classes, functions, constants) and their purpose.

Mention intended use cases or systems it integrates with.

Include a short example if usage isn’t immediately obvious.

Avoid repeating class-level docstrings—focus on the module’s role in the larger system.
```
 
 e.g.

"""
Defines the KeyType enumeration for musical keys, distinguishing between Major and Minor modes.

This module provides:
- An Enum class `KeyType` with two values: Major and Minor.
- Utility methods to list all key types, select a random key type, and retrieve the parallel (opposite) key.
- String representations for clean display and debugging.

Intended for use in music theory applications, generative composition tools, or any system requiring tonal classification.

Example:
    from keytype import KeyType

    key = KeyType.random()
    print(f"Selected key: {key}, Parallel: {key.parallel}")
 """