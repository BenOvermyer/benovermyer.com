+++
title = 'Tutorial: Dealing with Disk Space Errors in Linux'
date = 2015-12-10
+++
If you're seeing errors on a server (say, npm complaining about an ENOSPC error, or apt failing to install something) that suggest the hard disk is full, use this guide to resolve the issue.

# Troubleshooting

> All of the following commands assume you are logged in as a sudo user on a Linux machine. Some of the commands, like `df -hT`, won't work exactly as advertised on something like, say, Solaris.

## Checking disk space

First, check the amount of available disk space.

    df -hT
    

If one of the available drives (such as `/dev/xvda1`) shows as 100% full, then you'll need to clear some space. The first place to look is `/var/log/`, especially if nginx is writing log files to disk. Clear out all old logs (anything with a .gz file extension is fair game for deletion). If that doesn't free up enough space, the next place to check is the application directory for whatever app is on the server. If there are more than 3 releases on the server, you can safely delete the oldest ones (until you have at least 2 remaining). You can also remove all the files in `/tmp/`, although that should be a last resort.

## Checking inode usage

If you've confirmed that the hard drive isn't full (or cleared enough space that it isn't), and you're still seeing “disk is full” type errors, then you almost certainly have too few inodes available on the server. This means, basically, that there are too many files on the server.

### Checking inode usage

Run the following command to check inode usage:

    df -i
    

You'll see something like the following:

    Filesystem     Inodes IUsed IFree IUse% Mounted on
    udev             121K   409  120K    1% /dev
    tmpfs            125K   479  124K    1% /run
    /dev/vda1        1.9M  237K  1.7M   13% /
    tmpfs            125K     2  125K    1% /dev/shm
    tmpfs            125K     3  125K    1% /run/lock
    tmpfs            125K    15  125K    1% /sys/fs/cgroup
    tmpfs            125K     4  125K    1% /run/user/1000
    

The `IUse%` column is the one you're interested in. If `IUse%` is at or near 100%, then you have an inode usage problem.

### Delete old kernels

Often, you can free up a ton of inodes if you delete old kernels. This is done with a pretty simple command:

    sudo apt-get autoremove -y
    

Try that first. If that doesn't remove the old kernels, [this page](http://markmcb.com/2013/02/04/cleanup-unused-linux-kernels-in-ubuntu/) may help.

### Script to check for directories with lots of files

This script will help find directories with large numbers of files. Put the following into a file `list-files.sh` in your home directory:

    #!/bin/bash
    # count_em - count files in all subdirectories under current directory.
    echo 'echo $(ls -a "$1" | wc -l) $1' >/tmp/count_em_$
    chmod 700 /tmp/count_em_$
    find . -mount -type d -print0 | xargs -0 -n1 /tmp/count_em_$ | sort -n
    

Then make the file executable:

    chmod +x ./list-files.sh
    

Finally, go to the root directory on the server and run the script:

    cd /
    ~/list-files.sh
    

It may take a couple minutes to run, but it will present you with a list of all the directories with a number of files next to each, sorted in ascending order of number of files. Take a look at each of the high ones; that might give you an idea of what you need to clean up.

### Some notes about good files to delete

Log files are safe to delete. So are old releases. Also check the `/tmp/` directory; it can often be a hiding place for tons of files.
