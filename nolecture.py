#!/usr/bin/env python
''' nolecture.py -- A workshop builder
Usage:
    nolecture.py [-hv]
    nolecture.py <file.json>

Positional Arguments:
    <file.json>         A yaml file containing the workshop to build

Options:
    -h --help           Print this screen and exit
    -v --version        Print the version of nolecture.py
'''

from docopt import docopt
from os.path import isfile
import json
from jinja2 import Template

arguments = docopt(__doc__, version='nolecture.py version 0.0.1')

# Get all cells from notebooks in <file.json>
cells = []
if isfile(arguments["<file.json>"]):
    with open(arguments["<file.json>"], "r") as f:
        include_content = json.load(f)
    for from_dir in include_content["content"]:
        for content_dir, ipynb_files in from_dir.items():
            for ipynb_file in ipynb_files:
                ipynb_file_path = "content/{}/{}.ipynb".format(content_dir, ipynb_file)
                if isfile(ipynb_file_path):
                    with open(ipynb_file_path, "r") as f:
                        model = json.load(f)
                        cells.append(model["cells"])
                else:
                    raise NameError("{} is not a file".format(ipynb_file_path))
else:
    raise NameError("{} is not a file".format(arguments["<file.json>"]))

# Build a JSON string to put into template
content = ""
for outer in cells:
    for inner in outer:
        content += "{},\n".format(json.dumps(inner))

# Read the template
with open("skel.jinja2") as f:
    template = Template(f.read())

# Generate the JSON output inserting the string into Template
# -> print the pretty printed json
output = json.loads(template.render(content=content.strip()[0:-1]))
print(json.dumps(output, indent=2))
