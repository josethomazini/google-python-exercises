#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


def get_special_paths(dir, file_names_dict):
    # returns a list of the absolute paths of the special files in the given directory
    result = []

    if dir == '.':
        dir = os.getcwd()

    for item in os.listdir(dir):
        if item in file_names_dict:
            print('Names must not be repeated across the directories')
            sys.exit(1)
        else:
            file_names_dict[item] = None

        if re.match(r'.*__\w+__.*', item):
            result.append('%s/%s' % (dir, item))

    return result


def copy_to(paths, dir):
    # given a list of paths, copies those files into the given directory
    if not os.path.exists(dir):
        os.makedirs(dir)

    for item in paths:
        shutil.copy2(item, dir)


def zip_to(paths, zippath):
    # given a list of paths, zip those files up into the given zipfile
    paths_sequence = ' '.join(paths)
    zip_command = 'zip -j %s %s' % (zippath, paths_sequence)

    print("Command I'm going to do: %s" % zip_command)
    subprocess.run(zip_command.split())


# +++your code here+++
# Write functions and modify main() to call them


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # unique name helper struct
    file_names_dict = {}

    # all paths
    paths = []

    for item in args:
        paths.extend(get_special_paths(item, file_names_dict))

    if todir:
        copy_to(paths, todir)

    if tozip:
        zip_to(paths, tozip)


if __name__ == "__main__":
    main()
