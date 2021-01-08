---
title: "System Administration Notes"
date: 2019-10-25T07:45:43-05:00
draft: false
description: "Notes about system administration or management."
---

## Examining an SSL certificate

To verify a web server's certificate:

```
openssl s_client -connect <domain name>:443
```

There is more information available on [Bruce's blog post about verifying certificates](https://rbwilson.ca/how-to-verify-certificates-with-openssl/).

## Adding a root certificate to Ubuntu

1. `sudo mkdir /usr/share/local/ca-certificates` if it doesn't already exist
2. If you have a PEM file instead of a CRT, `openssl x509 -in mypem.pem -inform PEM -out mycrt.crt`
3. `sudo mv mycrt.crt /usr/share/local/ca-certificates/mycrt.crt`
4. `sudo update-ca-certificates`

Note that applications that have their own CA certificate stores will need to be updated also. Firefox
is one such example, as is Chef.

For Chef, do the following after the above:

```
echo "export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt" > /etc/profile.d/add_ssl_cert_file_for_chef.sh
```

## Adding a root certificate to RHEL

1. Place the root certificate here: `/etc/pki/ca-trust/source/anchors/my-cert.crt`
2. `sudo update-ca-trust`

For Chef, do the following after the above:

```
echo "export SSL_CERT_FILE=/etc/pki/tls/certs/ca-bundle.crt" > /etc/profile.d/add_ssl_cert_file_for_chef.sh
```

## Clearing out old Chef nodes

If you're using Chef with cloud infrastructure that doesn't properly clean up old nodes,
you can run the following occasionally to clear them out:

```
#!/bin/bash
for node in $(knife search node "ohai_time:[* TO $(date +%s -d '30 days ago')]" -i); do
  yes|knife client delete $node
  yes|knife node delete $node
done
```

This script produces a list of nodes (one per line, name only) with an `ohai_time` of greater than or equal to 30 days ago. The `ohai_time` is when the node last checked in with Chef Infra Server. It then deletes the client and node metadata from the server for that node.

You might need to change the '30 days ago' timeframe to better suit your own environment.

## Automating the update of Chef Infra Client in environments with internal CA

When you're in an environment that has an internal certificate authority, you'll need to add that material
to Chef. The following Chef code will automate that as part of a base cookbook `my_base_cookbook` default recipe.

Note that this requires two external cookbooks prior to Chef Infra Client 16.5: `chef-client` and `chef_client_updater`.
Chef Infra Client 16.5 and later includes the `chef-client` functionality.

```
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

## Building Docker images on an internal-only GitLab

Let's say you have an instance of GitLab set up on an internal domain name with a certificate signed by an internal root certificate authority. Let's also say that you want to set up Docker-in-Docker builds on a GitLab Runner for that instance.

Your GitLab runner config must have `privileged = true` for the executor, and it must be of the `docker` type.

The `.gitlab-ci.yml` file for your project should look something like this:

```
image: docker:19.03.13

services:
  - name: my-internal-registry.internaldomain:5050/my-team/my-internal-dind-image:latest
    alias: docker
    entrypoint: ["env", "-u", "DOCKER_HOST"]
    command: ["dockerd-entrypoint.sh"]

variables:
  DOCKER_HOST: tcp://docker:2376
  DOCKER_TLS_CERTDIR: "/certs"

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

build:
  stage: build
  script:
    - VERSION_TAG=`cat VERSION`
    - docker build --tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA --tag $CI_REGISTRY_IMAGE:latest --tag $CI_REGISTRY_IMAGE:$VERSION_TAG .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:$VERSION_TAG
    - docker push $CI_REGISTRY_IMAGE:latest
```

