---
title: "System Notes"
date: 2019-10-25T07:45:43-05:00
draft: false
description: "Notes about system administration or management."
---
## Adding a root certificate to Ubuntu

1. `sudo mkdir /usr/local/share/ca-certificates` if it doesn't already exist
2. If you have a PEM file instead of a CRT, `openssl x509 -in mypem.pem -inform PEM -out mycrt.crt`
3. `sudo mv mycrt.crt /usr/share/local/share/ca-certificates/mycrt.crt`
4. `sudo update-ca-certificates`

Note that applications that have their own CA certificate stores will need to be updated also. Firefox
is one such example, as is Chef.
