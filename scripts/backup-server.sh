#!/bin/zsh
#set -eu
rsync -r olivier@agot.be:backups/ $HOME/backup/server-ovh/
