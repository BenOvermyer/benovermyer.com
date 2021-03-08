+++
title = 'Fixing the Ansible 2.1 Temporary File Permissions Issue'
date = 2016-06-02
+++
In Ansible 2.1 and later, Ansible will not allow the creation of world-readable temporary files. It does this for a good reason, but it’s a change from how it was before. If you’re experiencing this problem, you’ll see an error when trying to become_user other than root, and it’ll look like this:

    fatal: [12.34.567.8]: FAILED! => {"failed": true, "msg": "Failed to set permissions on the temporary files Ansible needs to create when becoming an unprivileged user. For information on working around this, see https://docs.ansible.com/ansible/become.html#becoming-an-unprivileged-user"}
    

The documentation offers solutions. The one that worked for me was this: add the installation (and enablement) of ACL as part of your common tasks for a given playbook. Everything else will then work behind the scenes to make sure those temporary files are handled securely and silently.