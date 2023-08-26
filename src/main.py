#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='static')

@app.route("/ip")
def get_ip():
    return request.remote_addr + '\n'

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
