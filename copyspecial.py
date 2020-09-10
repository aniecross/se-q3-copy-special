#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """Anie Cross with help from instructor demo recordings,
Group-B discussion topics, google.com search, docs.python.org,
stackoverflow.com, google-python-class"""

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    list = []
    paths = os.listdir(dirname)
    for file_name in paths:
        match = re.search(r'__(\w+)__', file_name)
        if match:
            list.append(os.path.abspath(os.path.join(dirname, file_name)))
    return list


def copy_to(path_list, dest_dir):
    """Given a list of files copies to a new directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        file_name = os.path.basename(path)
        current_path = os.path.dirname(path)
        new_path = os.path.join(current_path, dest_dir, file_name)
        shutil.copy(path, new_path)


def zip_to(path_list, dest_zip):
    file_list = ''
    for path in path_list:
        file_list += path + " "
    try:
        subprocess.call(['zip', '-j', dest_zip] + path_list)
    except OSError as e:
        print(e)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions

    if not ns:
        sys.exit(1)

    if ns.todir:
        copy_to(get_special_paths(ns.from_dir), ns.todir)

    elif ns.tozip:
        zip_to(get_special_paths(ns.from_dir), ns.tozip)
    else:
        path_list = get_special_paths(ns.from_dir)
        for path in path_list:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
