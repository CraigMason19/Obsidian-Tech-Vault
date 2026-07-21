
[[#File context menu]]
[[#Windows Commands]]
[[#mklink]]

---
## File context menu

Both ways require opening `Regedit`

## Create new file

- Navigate to Computer\\HKEY_CLASSES_ROOT\\(whatever file extension you want)
- Right click on the extension key > New > Key
- Name the new key `ShellNew`
- Inside the `ShellNew` key, add a new string value
- Name the string value `NullFile`
## Remove file

- Navigate to Computer\\HKEY_CLASSES_ROOT\\(whatever file extension you want)
- Change `ShellNew` → `ShellNew_disabled` 
	- This means you can remove disabled and it will reappear

---
## Windows Commands

[Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)

### Opening cmd and powershell

You type `cmd` or `powershell` in the folders address bar to open a window at that location.

### Make Directories & Folders

```
cd desktop

mkdir foo

cd foo

notepad bar.md
```

---
## mklink

```
Windows thinks it’s still on C:, but the data actually lives elsewhere.
mklink /J "C:\ProgramData\Arobas Music\Soundbanks" "D:\Guitar Pro 8\Soundbanks"



C:\Users\Craig>mklink /J "C:\ProgramData\Arobas Music\Soundbanks" "D:\Guitar Pro 8\Soundbanks"
Junction created for C:\ProgramData\Arobas Music\Soundbanks <<===>> D:\Guitar Pro 8\Soundbanks
```
