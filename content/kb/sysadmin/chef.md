+++
title = "Chef"
description = "Notes about Chef"
+++

# Common Chef code bits

To reference Chef Infra Client's cache directory, use this:

```
Chef::Config[:file_cache_path]
```

# Clearing out old Chef nodes

If you're using Chef with cloud infrastructure that doesn't properly clean up old nodes,
you can run the following occasionally to clear them out:

```bash
#!/bin/bash
for node in $(knife search node "ohai_time:[* TO $(date +%s -d '30 days ago')]" -i); do
  yes|knife client delete $node
  yes|knife node delete $node
done
```

This script produces a list of nodes (one per line, name only) with an `ohai_time` of greater than or equal to 30 days ago. The `ohai_time` is when the node last checked in with Chef Infra Server. It then deletes the client and node metadata from the server for that node.

You might need to change the '30 days ago' timeframe to better suit your own environment.

# Automating the update of Chef Infra Client in environments with internal CA

When you're in an environment that has an internal certificate authority, you'll need to add that material
to Chef. The following Chef code will automate that as part of a base cookbook `my_base_cookbook` default recipe.

Note that this requires two external cookbooks prior to Chef Infra Client 16.5: `chef-client` and `chef_client_updater`.
Chef Infra Client 16.5 and later includes the `chef-client` functionality.

```ruby
node.default['chef_client']['chef_license'] = 'accept'
node.default['chef_client']['ca_cert_path'] = '/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem' // default for RHEL-compatible Linux

if platform_family?('windows')
  new_cert_file = 'C:\\chef\\cacert.pem'
  node.default['my_base_cookbook']['chef_client']['post_install_action'] = 'exec' // Windows needs 'exec', not 'kill'
  node.default['chef_client']['ca_cert_path'] = new_cert_file

  cookbook_file new_cert_file do
    source 'certs.pem' // this is the standard cacerts.pem chain with the addition of the internal CA certificate
    sensitive true
  end

  env 'SSL_CERT_FILE' do
    value new_cert_file
  end
end

include_recipe 'chef-client'

chef_client_updater 'Install latest Chef Infra Client' do
  version '16' // or whatever version
  post_install_action node['my_base_cookbook']['chef_client']['post_install_action']
end
```
