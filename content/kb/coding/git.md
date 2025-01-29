+++
title = "Git"
description = "A collection of notes on using Git."
+++

# Git Cheat Sheet

## Basic Commands

- `git init` - Initialize a new Git repository in the current directory.
- `git clone <url>` - Clone a repository from a remote URL.
- `git add <file>` - Add a file to the staging area.
- `git commit -m "<message>"` - Commit changes to the repository.
- `git status` - Show the status of the working directory and staging area.
- `git log` - Show the commit history of the repository.
- `git diff` - Show the differences between the working directory and the staging area.
- `git diff --staged` - Show the differences between the staging area and the repository.
- `git diff <commit>` - Show the differences between the working directory and a specific commit.
- `git diff <commit1> <commit2>` - Show the differences between two commits.
- `git checkout <commit>` - Move the HEAD pointer to a specific commit.
- `git reset HEAD <file>` - Unstage a file from the staging area.
- `git reset --soft <commit>` - Reset the HEAD pointer to a specific commit, keeping changes in the working directory.
- `git reset --mixed <commit>` - Reset the HEAD pointer to a specific commit, unstaging changes.
- `git reset --hard <commit>` - Reset the HEAD pointer to a specific commit, discarding changes.
- `git branch` - List all branches in the repository.
- `git branch <name>` - Create a new branch.
- `git checkout <branch>` - Switch to a different branch.
- `git merge <branch>` - Merge changes from a different branch.
- `git rebase <branch>` - Rebase changes from a different branch.
- `git remote` - List all remote repositories.
- `git remote add <name> <url>` - Add a new remote repository.
- `git push <remote> <branch>` - Push changes to a remote repository.
- `git pull <remote> <branch>` - Pull changes from a remote repository.
- `git fetch <remote>` - Fetch changes from a remote repository.
- `git tag <name>` - Create a new tag.
- `git tag -a <name> -m "<message>"` - Create a new annotated tag.
- `git tag -d <name>` - Delete a tag.
- `git tag -l` - List all tags.
- `git show <tag>` - Show the details of a tag.
- `git stash` - Stash changes in the working directory.
- `git stash list` - List all stashes.
- `git stash apply` - Apply the most recent stash.
- `git stash pop` - Apply and remove the most recent stash.
- `git stash drop` - Remove the most recent stash.
- `git stash clear` - Remove all stashes.
- `git clean -n` - Show files that are not being tracked.
- `git clean -f` - Remove files that are not being tracked.
- `git clean -i` - Interactively remove files that are not being tracked.

## Scenarios

The following are some common scenarios I've run into.

### Breaking up a big feature branch

Let's say we have a feature branch that has grown too large and we want to break it up into smaller, more manageable pieces. Here's how we can do that:

1. Create a new branch from the feature branch.
2. Use `git rebase -i` to interactively rebase the new branch.
3. Squash commits together to create a single commit for each new feature.
4. Push the new branch to the remote repository.

Alternatively, we can use cherry picking to transfer individual commits to new branches.

For example, to move the last three commits from `feature` to `feature-part-1`:

```bash
git checkout feature-part-1
git cherry-pick feature~2
git cherry-pick feature~1
git cherry-pick feature
```

### Undoing a commit

If we need to undo a commit, we can use `git reset` to move the HEAD pointer to a previous commit. There are three options for resetting:

- `git reset --soft <commit>` - Reset the HEAD pointer to a specific commit, keeping changes in the working directory.
- `git reset --mixed <commit>` - Reset the HEAD pointer to a specific commit, unstaging changes.
- `git reset --hard <commit>` - Reset the HEAD pointer to a specific commit, discarding changes.

For example, to undo the last commit:

```bash
git reset --soft HEAD~1
```

### Tagging a release

When we're ready to tag a release, we can use `git tag` to create a new tag. An annotated tag includes a message, while a lightweight tag does not.

For example, to create an annotated tag for version 1.0:

```bash
git tag -a v1.0 -m "Version 1.0"
```
