#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    year = '%s' % filename[4:8]
    with open(filename, 'r') as f:
        lines = f.readlines()

    name_list = []
    name_dict = {}

    for line in lines:
        if not line.startswith('<tr align="right"><td>'):
            continue

        # strip extra texts
        # from.....
        # <tr align="right"><td>985</td><td>Tavon</td><td>Kimber</td>
        # to.....
        # 985</td><td>Tavon</td><td>Kimber
        line = line[22:-6]

        # get text between </td><td>
        # ['985', 'Tavon', 'Kimber']
        values = line.split('</td><td>')

        # keep both names for sorting
        name_list.append(values[1])
        name_list.append(values[2])

        # save position for both names
        name_dict[values[1]] = values[0]
        name_dict[values[2]] = values[0]

    # sort names
    name_list.sort()

    # first item is the year
    result = [year]

    # other items are the name/position
    for item in name_list:
        result.append('%s %s' % (item, name_dict[item]))

    return result


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    for item in args:
        the_list = extract_names(item)

        if summary:
            with open('baby_output.txt', 'a') as f:
                # save the list as its terminal representation
                f.write(the_list.__str__())
                f.write('\n')
        else:
            print(the_list)


if __name__ == '__main__':
    main()
