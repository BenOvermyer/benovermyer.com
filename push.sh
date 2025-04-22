#!/usr/bin/env bash

zola build
mc cp --recursive public/* scaleway/benovermyer.com/
