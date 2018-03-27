"""
Generate a template for the given leetcode problem, for a specific language.
Current languages that are supported are:
    C++, C, Java, JavaScript, Python

Usage:
    $ python make_template <lang> <name of problem> ...
    Where each word in the name of the problem is separated by spaces.

Example:
    $ python make_template cc valid parenthesis
"""

###
### File Header Templates
###

general_template = """/*
 * Source: {}
 * Author: Paulo Lemus
 * Date  : {}
 * Info  : {}
 */

/*
{}
 */
"""

general_desc_head = ' * '


python_template = """# Source: {}
# Author: Paulo Lemus
# Date  : {}
# Info  : {}

{}
"""

python_desc_head = '# '


###
### File Naming Convention functions
###

def camel_case(words):
    return ''.join(map(str.title, words))

def snake_case(words):
    return '_'.join(map(str.lower, words))

def lisp_case(words):
    return '-'.join(map(str.lower, words))


# Languages that templates can be generated for
languages = {'cc', 'c', 'java', 'js', 'py'}

# templates to fill. Arguments: Source link, date, info, description
templates = {
    'cc': general_template,
    'c': general_template,
    'java': general_template,
    'js': general_template,
    'py': python_template
}

# Append these to the start of every line in the description.
description_heads = {
    'cc': general_desc_head,
    'c': general_desc_head,
    'java': general_desc_head,
    'js': general_desc_head,
    'py': python_desc_head
}

file_naming = {
    'cc': snake_case,
    'c': snake_case,
    'java': camel_case,
    'js': lisp_case,
    'py': snake_case
}

paths_from_root = {
    'cc': ['C++'],
    'c': ['C'],
    'java': ['Java', 'src', 'io', 'github', 'paulolemus', 'leetcode'],
    'js': ['JavaScript'],
    'py': ['Python']
}

# The string template for a leetcode link. Arg is lowercase, dash separated.
source_template = 'https://leetcode.com/problems/{}/description/'


import os
import sys
import re
import datetime
import requests

from bs4 import BeautifulSoup
from typing import List
from typing import Set
from typing import Tuple


def parse_args(languages: Set) -> Tuple[str, List[str]]:
    """Parse and return a tuple containing:
        The language string
        The name of the leetcode problem as a list
    """
    lang = sys.argv[1]
    problem = sys.argv[2:]

    if lang not in languages:
        raise ValueError('First argument must be a valid language')
    if len(problem) < 1:
        raise ValueError('Must provide a leetcode problem name')
    return lang, problem


def parse_description(soup) -> str:
    """
    Find and parse description in webpage.
    Note that the correct meta tag was found through trial and error.
    It could potentially change at any time.
    """
    metas = soup.find_all('meta')
    return metas[3]['content']


def parse_problem_number(soup) -> str:
    """
    Find and parse the problem number from the webpage.
    Note that because the JS does not execute, I have discovered through
    testing that the script containing the problem number is script 23.
    """
    prob_num_script = soup.find_all('script')[23]
    pattern = re.compile(r'\d+')
    prob_number = pattern.findall(prob_num_script.text)
    if len(prob_number) < 1:
        raise ValueError('Could not parse problem number from website.')
    return prob_number[0]


def format_description(description: str, desc_head: str) -> str:
    """Convert a plain text description to a description formatted as follows:
        * All lines are 80 char or less.
        * The end of a sentence ends a line.
        * All lines start with the desc_head.

    :param description: The text to format.
    :param desc_head: the header for each line in the description.
    :returns: The formatted string.
    """
    max_len = 80 - len(desc_head)
    lines = []

    # Make all lines max_len characters or less.
    for line in description.splitlines():
        while len(line) > max_len:
            lines.append(line[:max_len])
            line = line[max_len:]
        lines.append(line)

    lines = list(map(lambda line: desc_head + line + '\n', lines))
    lines[-1] = lines[-1].rstrip()
    return ''.join(lines)


if __name__ == '__main__':
    # Verify that language and name are valid.
    lang, prob_name = parse_args(languages)

    # Generate current date, format yyy-mm-dd
    date = datetime.datetime.now()
    date = '{}-{}-{}'.format(date.year, str(date.month).zfill(2), str(date.day).zfill(2))

    # Get and validate the leetcode page has downloaded.
    source_url = source_template.format('-'.join(prob_name))
    response = requests.get(source_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    #with open('tempfile.html.temp') as f:
    #    soup = BeautifulSoup(f.read(), 'html.parser')

    # Save the downloaded website in a temp file for testing.
    with open('tempfile.html.temp', 'w') as f:
        f.write(soup.prettify())

    description = parse_description(soup)
    description = format_description(description, description_heads[lang])
    prob_number = parse_problem_number(soup)

    # Create all important file header.
    file_name = '{}.{}'.format(file_naming[lang](prob_name), lang)
    file_header = templates[lang].format(source_url, date, '#'+prob_number, description)

    # Save the file in the correct place
    utildir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(utildir, os.pardir))
    file_dir = os.path.abspath(os.path.join(rootdir, *paths_from_root[lang]))
    abs_file_path = os.path.abspath(os.path.join(file_dir, file_name))

    with open(abs_file_path, 'w') as fout:
        fout.write(file_header)
