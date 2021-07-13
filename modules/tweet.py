import http.server
import socketserver
import json
import os
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pathlib import Path

def getFilepath(id):
  return os.getcwd() + "/out/tweets/" + str(id) + ".json"

def loadJson(name):
  f = open(name)
  if bool(f):
    return json.load(f)

def scrape(name, id):
  os.system("snscrape --jsonl twitter-search 'since_id:" + str(int(id) - 1)  + " max_id:" + id + " filter:safe' > " + name)


def scrape_tweet(url):
  if url.endswith('/'):
    n = len(url) - 1
    url = url[:n]
  
  segments = url.split('/')
  id = segments[len(segments) - 1]

  print(id)

  name = getFilepath(id)
  if Path(name).exists():
    return loadJson(name)

  scrape(name, id)
  return loadJson(name)


