#! /usr/bin/env bash
for dir in ./*/
do
  cd ${dir}
  git status >/dev/null 2>&1
  git config pull.rebase true
  # check if exit status of above was 0, indicating we're in a git repo
  [ $(echo $?) -eq 0 ] && echo "Updating ${dir%*/}..." && git pull
  cd ..
done