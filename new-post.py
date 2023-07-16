#!/usr/bin/env python3

import os
import argparse

# This script generates a new post file from the user's title input and the current date
# The file is saved as index.md in the content/blog directory in a directory of the same name as the title
# It contains the title, date, and an empty description field

# Get the title from the user based on an argparse argument
parser = argparse.ArgumentParser(description='Create a new post file')
parser.add_argument('-t', '--title', metavar='title', type=str, help='the title of the post')
args = parser.parse_args()
title = args.title

# Get the current date
date = os.popen('date +%Y-%m-%d').read().strip()

# Create a directory name from the title by replacing spaces with dashes, replacing symbols with nothing, and making it lowercase
directory = title.lower().replace(' ', '-').replace('\'', '').replace('\"', '').replace('?', '').replace('!', '').replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('/', '').replace('\\', '').replace('&', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('*', '').replace('+', '').replace('=', '').replace('_', '').replace('|', '').replace('~', '').replace('`', '')

# Create the directory
os.system('mkdir -p content/blog/' + directory)

# Set up the template for the file contents using a multiline string
template = '''+++
title = "{title}"
date = {date}
description = ""
+++

'''

# Write the template to the file
with open('content/blog/' + directory + '/index.md', 'w') as f:
    f.write(template.format(title=title, date=date))
