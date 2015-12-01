#!/usr/bin/env python
import os

for filename in os.listdir("dot"):
    target = "~/." + filename
    target = os.path.expanduser(target)
    src = os.path.realpath("dot/" + filename)
    if os.path.exists(target):
        print "target", target, "already exists"
    elif not os.path.exists(src):
        print "Error src doen't exist:", src
    else:
        print "Creating target:", target, " from source: ", src
        try:
            os.symlink(src, target)
        except OSError as e:
            print e, target, src

# Install vundle if not existant
if not  os.path.exists(os.path.expanduser("~/.vim/bundle/vundle/")):
    os.system("git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle")
else:
    print "Vundle already installed"
