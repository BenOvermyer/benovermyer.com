+++
title = "Using Git"
description = "Notes on how to use git"
+++

## Fetching all paths changed since another branch

Let's say you want to get the paths of all files changed in your branch compared to the target branch.

```bash
git diff --name-only master
```

## Squashing all commits in a branch into one

Let's say you have a branch off of master, and you want to squash all the commits into one before pushing to the remote.

Run the following (after checking out your branch locally):

```bash
git reset --soft `git merge-base master HEAD`
git commit -m 'One big commit'
```

## Setting up a remote git repository

This is how to set up a remote git repository (a mirror) simply via ssh.

It assumes you have a server set up with SSH, and that you have sudo access to it.

1. On the remote server, create a `git` user (`sudo adduser git`).
2. Create a directory `/var/repos/git` owned by the `git` user.
3. Add your local public key to the `git` user's `.ssh/authorized_keys` file, so you can SSH as that user.
4. Assuming your local git repository is named `myrepo`, create a directory `/var/repos/git/myrepo.git` owned by the `git` user.
5. As the `git` user, in that new directory, run `git init --bare`.
6. Locally on your machine, go into your repo and run `git add remote myremotename git@myserver:/var/repos/git/myrepo.git`
7. Run `git push -u myremotename main` (or whatever your main branch is)

There, now you have a remote mirror on a server you control.
