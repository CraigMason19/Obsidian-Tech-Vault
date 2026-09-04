
[[#Keyboard Shortcuts]]
[[#Windows Commands]]

[[#File context menu]]
[[#mklink]]

---
## Keyboard Shortcuts

[Windows Keyboard shortcuts](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)

| Command                         | Result             |
| ------------------------------- | ------------------ |
| Show Desktop / Restore Programs | WINDOWS + D        |
| Switch Program                  | ALT + TAB          |
| Minimize                        | CTRL + DOWN_ARROW  |
| Maximize                        | CTRL + UP_ARROW    |
| Open Volume Panel               | CTRL + WINDOWS + V |

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
## mklink

```
Windows thinks it’s still on C:, but the data actually lives elsewhere.
mklink /J "C:\ProgramData\Arobas Music\Soundbanks" "D:\Guitar Pro 8\Soundbanks"



C:\Users\Craig>mklink /J "C:\ProgramData\Arobas Music\Soundbanks" "D:\Guitar Pro 8\Soundbanks"
Junction created for C:\ProgramData\Arobas Music\Soundbanks <<===>> D:\Guitar Pro 8\Soundbanks
```
