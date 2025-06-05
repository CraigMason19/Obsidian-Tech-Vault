
## Add create new file to context menu

- Open Regedit
- Navigate to Computer\\HKEY_CLASSES_ROOT\\(whatever file extension you want)
- Right click on the extension key > New > Key
- Name the new key "ShellNew"
- Inside the ShellNew key, add a new string value
- Name the string value "NullFile"
- Change the NullFile's value to 1

That's it!

## Make Directories & Folders

```
cd desktop

mkdir foo

cd foo

notepad bar.md
```