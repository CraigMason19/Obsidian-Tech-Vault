Add-ons allow extra functionality to added [[Blender]]. 

Good places to look are Gumroad & [Blender Market](https://blendermarket.com)

[[#Useful Plugins]]

[[#Creating Custom Addons]]
	Links
	- [Add-on Tutorial](https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html)
	Notes
	- [[#Process]]
	- [[#Register / Unregister]]
	- [[#Poll]]

---
## Useful Plugins

Extra Meshes

BLAM - Camera perspective setup

Gaffer - Lighting

Magic UV - Texturing

TexTools - Texturing

Looptools

PR Isocam

Blenderkit

Measureit

Archipack

Archimesh

[RePrimitive](https://github.com/eXzacT/RePrimitive)
- Allows modification of primitives after creation



Slice Modifier
- Non-destructively add geometry for flexing models (e.g. **Bend**) when Sub-D would be totally inappropriate.
- [The Slice Modifier - A Ground-Breaking Change To How We Flex Models in Blender](https://www.youtube.com/watch?v=ZjXOnUV9F_8&list=WL&index=42&pp=gAQBiAQB)
- https://superhivemarket.com/products/slice-it/?ref=834


[DECODED's Mesh Cleaner](https://decoded.gumroad.com/l/meshcleaner)


---
## Creating Custom Addons

**NOTE:** To resolver errors in **VSCODE**, Pylance etc. Can pip install fake-bpy-module-latest 
### Process
- Create the script in a custom blender scene, make sure it all works as expected

Prototype: Start by prototyping the feature that will give you the most immediate benefit in your work.

Test: Once you have a working version, test it with your own Blender projects to ensure it works as expected.

Package and Market: Once the plugin is ready, you can bundle it and upload it to Gumroad, Blender Market, or even distribute it through GitHub. Make sure to include demo videos, screenshots, and a clear explanation of the plugin's features.


### Register / Unregister

- **Running the script manually** (from Blender’s Text Editor) → `register()` is called due to `if __name__ == "__main__":`
- **Installing the add-on** → `register()` is **not** called yet
- **Enabling the add-on** (in Blender's preferences) → Blender automatically calls `register()`
- **Disabling the add-on** → Blender calls `unregister()`
- Can register multiple classes

```python
classes = [OBJECT_OT_example_operator, VIEW3D_PT_example_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
```
### Poll

- A synonym for query
- Checks if the operator can run. It asks, "Is the context valid?" before enabling the operator.
- If your operator has conditions for when it should be available, just add a poll method to filter when it can run.

- Ensuring an object is selected (`context.selected_objects`)
- Checking if you're in a specific mode (e.g., Edit Mode)
- Verifying the active object type (e.g., only run on meshes)
- Limiting execution to specific contexts (e.g., only in the 3D View)

