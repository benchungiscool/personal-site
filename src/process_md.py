#!/usr/bin/env python3
from markdown import markdown
from os import listdir
import os

targetdir = "./md"
directory = targetdir

# Lambda functions related to finding markdown files
isMarkdownFile = lambda filename: filename[-3:] == '.md'
getFilePath = lambda filename: str(targetdir + "/" + filename)

# Lambda functions related to tagging markdown files
isTagged = lambda filename: filename.split("_")[0].isnumeric()
scrapeTags = lambda markdownfiles: [int(filename.split("_")[0]) for filename in filter(isTagged, markdownfiles)]

# Get tags
def gettags():
    if scrapeTags(markdownindir()):
        return scrapeTags(markdownindir())
    return [0]

# Get all the markdown files in a directory
def markdownindir():
    return [filename for filename in listdir(targetdir) if isMarkdownFile(filename)]

def addtags():
    to_tag = filter(lambda filename: not isTagged(filename), markdownindir())
    max_tag = max(gettags())
    for filename in to_tag:
        max_tag += 1
        os.rename(getFilePath(filename), getFilePath(str(max_tag) + "_" + filename))

# Get the content of all the markdown files in our target directory, rendered into html
def getallmd():
    ret = ""
    addtags()
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
    with open("src/static/posts.html", "w") as fc:
        fc.write(renderedposts)

