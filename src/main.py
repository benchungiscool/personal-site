#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, send_from_directory
from src.process_md import writetofile

app = Flask(__name__, template_folder='static')
writetofile()

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
