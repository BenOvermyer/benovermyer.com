+++
title = "Linux"
date = "2021-04-15"
+++

# Examining an SSL certificate

To verify a web server's certificate:

```
openssl s_client -connect <domain name>:443
```

There is more information available on [Bruce's blog post about verifying certificates](https://rbwilson.ca/how-to-verify-certificates-with-openssl/).

# Adding a root certificate to Ubuntu

1. `sudo mkdir /usr/share/local/ca-certificates` if it doesn't already exist
2. If you have a PEM file instead of a CRT, `openssl x509 -in mypem.pem -inform PEM -out mycrt.crt`
3. `sudo mv mycrt.crt /usr/share/local/ca-certificates/mycrt.crt`
4. `sudo update-ca-certificates`

Note that applications that have their own CA certificate stores will need to be updated also. Firefox
is one such example, as is Chef.

For Chef, do the following after the above:

```bash
echo "export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt" > /etc/profile.d/add_ssl_cert_file_for_chef.sh
```

# Adding a root certificate to RHEL

1. Place the root certificate here: `/etc/pki/ca-trust/source/anchors/my-cert.crt`
2. `sudo update-ca-trust`

For Chef, do the following after the above:

```bash
echo "export SSL_CERT_FILE=/etc/pki/tls/certs/ca-bundle.crt" > /etc/profile.d/add_ssl_cert_file_for_chef.sh
```
