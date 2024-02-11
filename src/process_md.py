#!/usr/bin/env python3
from markdown import markdown
from os import listdir
import os

targetdir = "./md"
directory = targetdir

# Lambda functions related to finding markdown files
isMarkdownFile = lambda filename: filename[-3:] == '.md'
getFilePath = lambda filename: str(targetdir + "/" + filename)

# Get all the markdown files in a directory
def markdownindir():
    return [filename for filename in listdir(targetdir) if isMarkdownFile(filename)]

# Get the content of all the markdown files in our target directory, rendered into html
def getallmd():
    ret = ""
    for filename in markdownindir():
        with open(getFilePath(filename), "r") as fc:
            contents = fc.read()
        htmlcontents = markdown(contents)
        ret += f"""
        <div class='post'>
            {htmlcontents}
        </div>"""
    return ret

def writetofile():
    renderedposts = getallmd()
    filepath = "src/static/posts.html"
    if os.path.exists(filepath):
        os.remove(filepath)
    with open(filepath, "w") as fc:
        fc.write(renderedposts)

