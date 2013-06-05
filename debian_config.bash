#!/bin/bash -e

read -p 'e-mail address, git: ' git_email
git config --global user.email "${git_email}"

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
