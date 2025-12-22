[Git - Website](https://git-scm.com)

- The most popular source control. 
- Free & Open Source.

Monitors and tracks changes across your files locally. It monitors what was changed, when it was changed and by whom.

Not to be confused with [[GitHub]]. Which is a hosting service.

[[#Commands]]

[[#Workflow]]
- [[#Push, Fetch & Pull]]
- [[#Branching]]
- [[#Stashing]]
- [[#Pull request (PR)]]
- [[#Forking]]
- [[#Collaborators]]
- 
[[#Basic Workflow For Collaboration]]

---
## Commands

**NOTE:** When you are in the log window (log, diff etc...) you can escape back to the terminal using `:q`

| Command                                     | Description                                                                                            |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| git -v<br>git --version                     | Displays the Git version. Also useful to check  if it's installed                                      |
| git init                                    | Initialise a working directory. Creates a hidden `.git` folder                                         |
| git clone [link]                            | Pulls the `remote` repository onto your local machine                                                  |
| git status                                  | Shows what changes have been made to our working directory                                             |
| git log                                     | Show commit history                                                                                    |
| git log --oneline                           | Show a condensed commit history                                                                        |
| git diff [ID 1] [ID 2]                      | Show differences between commits                                                                       |
|                                             |                                                                                                        |
| git add -A<br>git add --all                 | Add all changes in the `repository` to the staging area.                                               |
| git add .                                   | Add all changes in the `current directory` to the staging area.                                        |
| git add *                                   | Add only new or modified items (not deleted ones)                                                      |
| git reset                                   | Remove files from the staging area.                                                                    |
| git add [filename]                          | Add only that file to the staging area.                                                                |
|                                             |                                                                                                        |
| git commit -m "[message]"                   | Commit the staged changes with an appropriate description of what's changed.                           |
| git reset HEAD~                             | Reverse the commit and go back to the commit before                                                    |
| git reset --hard                            | Reverse the commit and brick back deleted files.                                                       |
| git restore [file]                          | Restore `unstaged` files back to how they were at start of current commit (before things were changed) |
| git restore --staged [file]                 | Restore `staged` files back to how they were at start of current commit (before things were changed)   |
|                                             |                                                                                                        |
| git branch                                  | Show all branches (asterisk shows where you are)                                                       |
| git branch [name]                           | Creates a new branch                                                                                   |
| git checkout [name]                         | Switch branches                                                                                        |
| git checkout [commit ID]                    | Switch to a specific commit                                                                            |
| git merge [destination branch] -m [message] | Merge current branch into the destination branch                                                       |

---
## Workflow

The main workflow is divided into two. Local & Remote.

- work change files
- Stage which ones i want to commit, The staging area is an intermediate to step to make swure we want to proceed.
- changes are made locally, not remotely
- commit when you are sure jof the changes you want to makef

still local until you push to remote




add
commit
push


---
### Push, Fetch & Pull

#### Push (->)
send local changes to the remote

origin is the remote repository
git push origin main 


git push origin [branch name]

#### Fetch (<-)
bring remote changes to local, but not merging them

see if we are behind any changes
git fetch

#### Pull (<-)
bring remote changes to local and merge them immediately
fetch + merge
git pull

---
### Branching

**Note:** Now called `main` used to be `master`

This allows you to create a whole new development path, to work on features etc.... Once this branch is finished it can be reincorporated back into the `main` branch

---
### Stashing

git stash
suppose im working on a new branch, unstaged and I need to look at another branch. but i want to keep all my work. I can stash it for later
temporarilt set aside unfinished work, switch to another branch to do something
git stash

then you can change branches
use 
git stash pop
git stash apply
git stash list


git revert
adds a new commit cancelling out the changes of the last commit
brings project back to it's previous state
:wq to quit (write quit)

---
### Pull request (PR)

**NOTE:** On [[GitHub]] you can allow `collaborators`. This means that they can add changes to the repository (even private ones) directly.

A way to contribute to someone else repository
A request to bring in a set of changes into a code base. 
Also used to bring code from a branch you are working on into another branch.

Someone allowed to accept changes can than review the merge (look for bugs or conflicts) and either accept or reject them.

It's important to review and test your code before asking for it to be committed
always follow any contribution rules on the original repo




**Linking Fork to Upstream**

- On the forked repo (granda’s PC), add your main repo as the upstream remote:
    
    bash
    
    ```
    git remote add upstream https://github.com/YourUsername/YourRepo.git
    ```
    
- This lets you pull updates from your main repo into the fork.
- git fetch upstream
git merge upstream/main






---
### Forking 
forking a repo on git hub adds a forked copy of the repo to your account. contains a link to the `upstream` (original) repo.

this forked copy is the origin.

this means you can them clone it to your pc to make changes

git push origin (the repo on github)

Allows you to create a clone of someone else's repository, this allows you to modify the contents and open a pull request, 


---
## Basic Workflow For Collaboration

https://www.youtube.com/watch?v=jRLGobWwA3Y&list=WL&index=62
[CoderDave - How to Review a Pull Request in GitHub the RIGHT Way](https://www.youtube.com/watch?v=lSnbOtw4izI&list=WL&index=62)




### Example

Person **(A)** creates a repository and another person **(B)** want to contribute to it.

**A**'s `repo` is the `upstream` `repo`
**B**'s `repo` is the `origin` `repo`

Setup:
- **B** `forks` the `repo` to their own account
	```git get	```
- **B** `clones` the `repo` to their own machine & IDE

Changes:
- **B** `fetches` or `pulls` changes into the local copy. Pull from origin → keeps your fork in sync with itself. Fetch from upstream → keeps your fork aligned with the main repo, but you decide when/how to merge.
- B rebases?
- **B** makes any changes as they see fit
- **B** once happy with their changes
	- Pushes local commits to the `forked` `repo`
	- Opens a `PR (pull request)` 
	- asd
	- asd

Acceptance:
	- **A** then decides if this code is correct and acceptable and checks merge conflicts. can decided whats merged
	- 



