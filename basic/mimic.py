#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
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

    # empty string is what comes before the first word
    dic = {
        '': [all_words[0]]
    }

    last_item = len(all_words) - 1
    for index, item in enumerate(all_words):
        if index < last_item:
            if item not in dic:
                dic[item] = []
            dic[item].append(all_words[index + 1])

    return dic


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    words = []
    line_break = 0
    for item in range(200):
        if word not in mimic_dict:
            word = ''
        word = random.choice(mimic_dict[word])
        words.append(word)
        line_break += len(word)

        if line_break >= 70:
            line_break = 0
            words.append('\n')

    text = ' '.join(words)
    text = text.replace('\n ', '\n')
    print(text)


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
