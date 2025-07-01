+++
title = "Using Git"
description = "Notes on how to use git"
+++

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
