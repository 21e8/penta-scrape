from flask import Flask, request, jsonify
from modules.tweet import scrape_tweet
from modules.reddit import scrape_reddit
from modules.medium import scrape_medium

app = Flask(__name__)

@app.route('/tweet', methods=['POST'])
def tweet():
  url = request.form.get('url')
  response = jsonify(scrape_tweet(url))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/medium', methods=['POST'])
def medium():
  url = request.form.get('url')
  response = jsonify(scrape_medium(url))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/reddit', methods=['POST'])
def reddit():
  url = request.form.get('url')
  response = jsonify(scrape_reddit(url))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response