- **MAJOR (**`1.x.x`**)** → **Big changes** that break compatibility (e.g., refactoring core logic, changing function signatures, removing features).
- **MINOR (**`x.1.x`**)** → **New features** that don’t break existing functionality (e.g., adding a new class or function).
- **PATCH (**`x.x.1`**)** → **Bug fixes** that don’t add new functionality (e.g., fixing validation, performance improvements).


Not necessarily—you only need to **bump the version when it makes sense** based on the type of change.

Here's a practical way to think about it:

- **Small fixes or tweaks** → You don’t have to bump immediately. Group them together and do a **patch bump (**`x.x.1 → x.x.2`**)** when ready.
    
- **Adding new functionality** → Bump **minor version (**`x.1.x → x.2.x`**)** when a meaningful feature is added.
    
- **Major changes that break compatibility** → Definitely bump **major (**`1.x.x → 2.x.x`**)** before pushing.



python
bumpversion