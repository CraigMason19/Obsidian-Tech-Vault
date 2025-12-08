[Git Website](https://git-scm.com)

- The most popular source control. 
- Free & Open Source.

Monitors and tracks changes across your files locally. It monitors what was changed, when it was changed and by whom.

Not to be confused with [[GitHub]]. Which is a hosting service.

[[#Commands]]
[[#Workflow]]
[[#Branching]]

---
## Commands

| Command                                     | Description                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------- |
| git -v<br>git --version                     | Displays the Git version. Also useful to check  if it's installed            |
| git init                                    | Initialise a working directory. Creates a hidden `.git` folder               |
| git clone [link]                            | Pulls the `remote` repository onto your local machine                        |
| git status                                  | Shows what changes have been made to our working directory                   |
| git log                                     | Show commit history                                                          |
| git log --oneline                           | Show a condensed commit history                                              |
|                                             |                                                                              |
| git add -A<br>git add --all                 | Add all changes in the `repository` to the staging area.                     |
| git add .                                   | Add all changes in the `current directory` to the staging area.              |
| git add *                                   | Add only new or modified items (not deleted ones)                            |
| git reset                                   | Remove files from the staging area.                                          |
| git add [filename]                          | Add only that file to the staging area.                                      |
|                                             |                                                                              |
| git commit -m "[message]"                   | Commit the staged changes with an appropriate description of what's changed. |
| git reset HEAD~                             | Reverse the commit and go back to the commit before                          |
| git reset --hard                            | Reverse the commit and brick back deleted files.                             |
|                                             |                                                                              |
| git branch                                  | Show all branches (asterisk shows where you are)                             |
| git branch [name]                           | Creates a new branch                                                         |
| git checkout [name]                         | Switch branches                                                              |
| git merge [destination branch] -m [message] | Merge current branch into the destination branch                             |
|                                             |                                                                              |

---
## Workflow

The main workflow is divided into two. Local & Remote.

- work change files
- Stage which ones i want to commit, The staging area is an intermediate to step to make swure we want to proceed.
- changes are made locally, not remotely
- commit when you are sure jof the changes you want to makef

still local until you push to remote















CLI - Command Line Interface
cd desktop


create project on git hub with readme










## Branching

**Note:** Now called `main` used to be `master`

This allows you to create a whole new development path, to work on features etc.... Once this branch is finished it can be reincorporated back into the `main` branch











### pull
download changes from remote repo  to your local machie






