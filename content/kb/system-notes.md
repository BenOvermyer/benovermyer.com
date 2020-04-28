---
title: "System Notes"
date: 2019-10-25T07:45:43-05:00
draft: false
description: "Notes about system administration or management."
---
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
