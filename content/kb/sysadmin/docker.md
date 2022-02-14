+++
title = "Docker"
+++

# Building Docker images on an internal-only GitLab

Let's say you have an instance of GitLab set up on an internal domain name with a certificate signed by an internal root certificate authority. Let's also say that you want to set up Docker-in-Docker builds on a GitLab Runner for that instance.

Your GitLab runner config must have `privileged = true` for the executor, and it must be of the `docker` type.

The `.gitlab-ci.yml` file for your project should look something like this:

```yaml
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
