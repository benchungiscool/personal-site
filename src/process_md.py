#!/usr/bin/env python3
from markdown import markdown
from os import listdir
import os
import re

targetdir = "./md"
directory = targetdir

# Lambda functions related to finding markdown files
isMarkdownFile = lambda filename: filename[-3:] == '.md'
getFilePath = lambda filename: str(targetdir + "/" + filename)

# Get all the markdown files in a directory
def markdownindir():
    return [filename for filename in listdir(targetdir) if isMarkdownFile(filename)]

def formatpost(index, title, body):
    return f"""
    <div class="post" _="on click show #post{index}">
        <h1>{title}</h1>
    </div>
    <div class="post" id="post{index}" _="on load hide me then on click hide me">
    {body}
    </div>
    """

# Get the content of all the markdown files in our target directory, rendered into html
def getallmd():
    ret = ""
    for index, filename in enumerate(markdownindir()):
        with open(getFilePath(filename), "r") as fc:
            contents = fc.read()
        htmlcontents = markdown(contents).split("\n")
        title = htmlcontents[0]
        body = "".join(htmlcontents[1:])
        ret += f"""
        <div class="post" id="title{index}primary" _="on click show #post{index} then hide me then show #title{index}">
            {title}
        </div>
        <div class="post" id="title{index}" _="on load hide me then on click hide #post{index} then hide me then show #title{index}primary">
            {title}
        </div>
        <div class="post" _="on load hide me" id="post{index}">
            {body}
        </div>
        """
    return ret

def writetofile():
    renderedposts = getallmd()
    filepath = "src/static/posts.html"
    if os.path.exists(filepath):
        os.remove(filepath)
    with open(filepath, "w") as fc:
        fc.write(renderedposts)

