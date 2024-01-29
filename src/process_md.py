#!/usr/bin/env python3
from markdown import markdown
from os import listdir

targetdir = "./md"

isMarkdownFile = lambda filename: filename[-3:] == '.md'
getFilePath = lambda filename: str(targetdir + "/" + filename)

# Get the names of all the markdowns in the markdown directory
def markdownindir():
    return [filename for filename in listdir(targetdir) if isMarkdownFile(filename)]

# Get the content of all the markdown files in our target directory, rendered into html
def getallmd():
    ret = ""
    for filename in markdownindir():
        with open(getFilePath(filename), "r") as fc:
            contents = fc.read()
        htmlcontents = markdown(contents)
        ret += "<div class='post'>\n"
        ret += htmlcontents
        ret += "\n</div>\n\n"
    return ret

if __name__ == "__main__":
    print(getallmd())
