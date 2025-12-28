#!/usr/bin/env python3

import os
import argparse
from datetime import datetime
from pathlib import Path

# This script generates a new post file from the user's title input and the current date
# The file is saved as index.md in the content/blog/YYYY/MM/slug directory
# It contains the title, date, and an empty description field

# Get the title from the user based on an argparse argument
parser = argparse.ArgumentParser(description='Create a new post file')
parser.add_argument('-t', '--title', metavar='title', type=str, help='the title of the post', required=True)
args = parser.parse_args()
title = args.title

# Get the current date
now = datetime.now()
date_str = now.strftime('%Y-%m-%d')
year = now.strftime('%Y')
month = now.strftime('%m')

# Create a directory name from the title
slug = title.lower().replace(' ', '-').replace('\'', '').replace('\"', '').replace('?', '').replace('!', '').replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('/', '').replace('\\', '').replace('&', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('*', '').replace('+', '').replace('=', '').replace('_', '').replace('|', '').replace('~', '').replace('`', '')

BLOG_ROOT = Path("content/blog")
year_dir = BLOG_ROOT / year
month_dir = year_dir / month
post_dir = month_dir / slug

# Create directories
post_dir.mkdir(parents=True, exist_ok=True)

# Ensure _index.md exists for year
year_index = year_dir / "_index.md"
if not year_index.exists():
    with open(year_index, "w") as f:
        f.write(f'+++\ntitle = "{year}"\ntransparent = true\n+++\n')

# Ensure _index.md exists for month
month_index = month_dir / "_index.md"
if not month_index.exists():
    with open(month_index, "w") as f:
        f.write(f'+++\ntitle = "{year}-{month}"\ntransparent = true\n+++\n')

# Set up the template for the file contents using a multiline string
template = '''+++
title = "{title}"
date = {date}
description = ""
+++

'''

# Write the template to the file
post_file = post_dir / 'index.md'
if post_file.exists():
    print(f"Error: Post already exists at {post_file}")
else:
    with open(post_file, 'w') as f:
        f.write(template.format(title=title, date=date_str))
    print(f"Created new post at {post_file}")
