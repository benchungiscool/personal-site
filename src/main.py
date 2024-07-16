#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, send_from_directory, send_file
from src.process_md import writetofile, getallmd

app = Flask(__name__, template_folder='static')
environment = "prod" if os.getenv("PWD") != "/static" else "dev"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/tst")
def postbody():
    return """
    <p>A big part of my role in DevOps is creating and maintaining CI/CD pipelines with tools like jenkins and gh-actions.I wanted to experiment with this myself and create a pipeline for changes to the main branch of the repo of this site, as part of my ongoingcommitment to spend more time on backend than frontend.</p><p>To this end, I created a simple CD script using github actions, which pulls down my latest changes and then redeploy my docker containers for thesite itself, and my nginx. This means that I don't have to ssh into my server to make changes to this site, and can test updates to the site on mylocal before pushing.</p>
    """

@app.route("/posts")
def posts():
    if prod:
        return send_file("./static/posts.html")
    return getallmd()

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
