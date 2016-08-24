#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def count_words_from_file(filename):
    # reads file to a lines array
    with open(filename) as f:
        lines = f.readlines()

    # joins the lines into one string
    text = ' '.join(lines)

    # removes breaklines
    text = text.replace('\n', '')

    # remove punctuations to avoid keys like '.' or ','
    for item in [
        '.', '!', ',', '?', "'", '"', ':', '-', '(', ')',
        '`', ';', '[', ']', '*', '_',
    ]:
        text = text.replace(item, ' ')

    # Removes any over-spaced text
    while True:
        new_text = text.replace('  ', ' ')
        if text == new_text:
            break
        else:
            text = new_text

    # trim
    new_text = new_text.strip()

    all_words = new_text.split(' ')

    # counts the words
    counters = {}
    for item in all_words:
        item = item.lower()
        if item not in counters:
            counters[item] = 0
        counters[item] += 1

    return counters


def print_words(filename):
    counters = count_words_from_file(filename)

    # organizes the output
    keys = list(counters.keys())
    keys.sort()

    # prints the output
    for item in keys:
        print('%s %s' % (item, counters[item]))


def print_top(filename):
    counters = count_words_from_file(filename)

    # get top values
    inverted_counters = {}
    for item in counters:
        inverted_counters[counters[item]] = item

    # organizes the output
    keys = list(inverted_counters.keys())
    keys.sort()
    keys.reverse()
    keys = keys[:20]

    # prints the output
    for item in keys:
        print('%s %s' % (inverted_counters[item], item))


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
