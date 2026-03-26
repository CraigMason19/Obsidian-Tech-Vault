#software #Development 

A free [[Git]] GUI client for windows and mac. 

Allows you to interact with [[Git]] through a user interface.

[[#Create a new Project]]
[[#Restoring a project]]

[[#Fixes]]
- [[#FIX - Can't log in to push onto GitHub]]
- [[#FIX - Source tree not starting in windows 10]]


---
## Create a new Project

Create a new project in GitHub & add a Readme

In Sourcetree
- File -> New / Clone
- Remote -> refresh -> choose project -> clone
- Select A EMPTY folder to clone into
- Create .gitignore if needed
- Stage all and type, Initial commit

---
## Restoring a project

When my hard drive failed I had to restore a project, possible due to GitHub. 

In source tree, Just clone the project into an empty folder. 

Some reconstruction (e.g virtual environments, packages, etc...) may be required. This is why having frozen requirements and good readme's is important. 

---
## Fixes
---
### FIX - Can't log in to push onto [[GitHub]]

1. Tools -> Options -> Authentication
2. Click "Edit" on Your Account
3. Click "Refresh OAuth Token"

---
### FIX - Source tree not starting in windows 10

1. Navigate to C:\\Users\\_**UserName**_\\AppData\\Local\\Atlassian
2. Under there, you will see SourceTree.exe_Url__**RandomGuid**_
3. Delete all of those style folders so you are only left with one folder called SourceTree
4. Start SourceTree, and it will rebuild that settings file.

----

