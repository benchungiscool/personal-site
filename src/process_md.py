#!/usr/bin/env python3
from markdown import markdown
from os import listdir, environ
import os
import re
from copy import deepcopy

targetdir = "./md"
directory = targetdir

# Lambda functions related to finding markdown files
isMarkdownFile = lambda filename: filename[-3:] == '.md'
getFilePath = lambda filename: str(targetdir + "/" + filename)
format_codeblocks = lambda markdown: markdown.replace("</pre>\n<p></code></p>", "</pre></code>")

# Get all the markdown files in a directory
def markdownindir():
    return [filename for filename in listdir(targetdir) if isMarkdownFile(filename)]

def format_post_body(post_body):
    ret = deepcopy(post_body)

    # Replace all backticks with codeblocks
    ret = ret.replace("```", "<pre><code>")

    # Get the indexes of every second <pre><code>
    indexes = []
    start = 0
    count = 0
    while start < len(ret):
        index = ret.find("<pre><code>", start)
        if index == -1:
            break
        indexes.append(index)
        start = index + 1
        count += 1
    codeblock_indices = [
        # Odds and evens are reversed in zero-indexed lists
        item for index, item in enumerate(indexes) if index % 2 != 0
    ]

    offset = 0
    for index in codeblock_indices:
        index = index + offset
        ret = ret[:index] + ret[index] + "/" + ret[index+1:index+6] + "/" + ret[index+6:]
        offset += 2

    return ret

# Get the content of all the markdown files in our target directory, rendered into html
def getallmd():
    ret = ""
    for index, filename in enumerate(markdownindir()):
        with open(getFilePath(filename), "r") as fc:
            contents = fc.read()
            contents = format_post_body(contents)
        htmlcontents = markdown(contents).replace("</pre>\n<p></code></p>", "</pre></code>").split("\n")
        title = htmlcontents[0]
        body = "\n".join(htmlcontents[1:])
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
    ret += """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js"></script>
    <script>
     hljs.highlightAll();
    </script>
    """
    return ret

def writetofile():
    renderedposts = getallmd()
    filepath = "src/static/posts.html"
    if os.path.exists(filepath):
        os.remove(filepath)
    with open(filepath, "w") as fc:
        fc.write(renderedposts)


