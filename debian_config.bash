#!/bin/bash -e

read -p 'e-mail address, git: ' git_email
git config --global user.email "${git_email}"

