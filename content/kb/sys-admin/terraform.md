+++
title = "Terraform"
description = "Notes about Terraform"
+++

# Upgrading ancient providers

Terraform code from before 0.13 used a different provider reference method. If you get errors like "Invalid legacy provider address" you can run the following to fix the state:

```bash
terraform state replace-provider \
-auto-approve \
"registry.terraform.io/-/aws" \
"hashicorp/aws"
```
