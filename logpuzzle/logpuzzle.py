#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    result = []

    # the filename seems NOT to be the host
    # this url points to a valid code.google location
    # https://groups.google.com/forum/#!topic/python-gcu-forum/CUhd-VQKAaY
    base = 'http://code.google.com/edu/languages/google-python-class/images/puzzle/'

    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            found_text_location = line.find('/images/puzzle/')
            if found_text_location < 0:
                continue

            start = found_text_location + 15
            end = line.find('HTTP') - 1

            result.append('%s%s' % (base, line[start:end]))

    # removes duplicates
    result = list(set(result))

    # increasing order
    result.sort()

    return result


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    img_names = []

    for img_url in img_urls:
        file_name = img_url.split('/')[-1]
        if file_name.startswith('p-'):
            file_name = '%s' % (file_name[7:])

        path = '%s/%s' % (dest_dir, file_name)
        img_names.append(file_name)
        print('downloading %s' % img_url)
        urllib.request.urlretrieve(img_url, path)

    img_names.sort()

    with open('%s/%s' % (dest_dir, 'index.html'), 'w') as f:
        for name in img_names:
            f.write('<img src=%s>' % name)


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
