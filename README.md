# GIT & GitHub

## What is GIT?
GIT is a VCS (Version Control System). It used to track code and changes to it. GIT is Open Source and was written Linus Torvalds (the creator of the Linux Kernel). GIT is decentralized meaning it needs no internet access for most of it operations and each user hosts a complete copy of the codebase. 

## How does it work?
GIT uses a DAG (Direct Acyclic Graph) to track code. Each node in the graph is called a **commit** and it's a complete snapshot of the codebase. In this graph commits always point to their parents (or predecessors).

## Commands

### `git init`
This command starts a new, empty repository. This will have the effect of creating a hidden folder called `.git` which will have all the necessary files for tracking. It's never necessary to access or change contents of this folder.

### `git status`
This command shows the current status of the working directory. It does not have a side effect it just shows the current status. 

### `git log`
Logs the history of the repo (the commit list).

### `git add [FILES]`
Adds files from the working directory to the staging area. FILES is a list of space-separated files to move to the staging area. Using the `.` wildcard will add **all** files to the staging area.

### `git commit`
Makes a commit and adds it to the tip of the current branch. This will add a new node in our history. Commits usually have a **commit message** which is a short summary of the changes being done.
#### Shortcut switches
##### Add commit message inline
To add the commit message in the same command use the `-m` switch followed by the commit message between double quotes:
```bash
git commit -m "This is the commit message."
```

##### git add all modified files and commit
This command auto adds all **already** changed files to the staging area and creates the commit 
```bash
git commit -a
```