#!/usr/bin/env bash

git init
git add *
git commit -m "init"

git remote add origin git@github.com:yuanjie-ai/xchat.git
git branch -M master
git push -u origin master -f
# git remote remove origin
