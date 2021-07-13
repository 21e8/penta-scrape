import re
from bs4 import BeautifulSoup
import requests
import json
from pathlib import Path
import os

def getFilepath(id):
  return os.getcwd() + "/out/medium/" + str(id) + ".json"

def get_text(el):
  return el.get_text()

def loadJson(name):
  f = open(name)
  if bool(f):
    return json.load(f)


def writeFile(name, content):
  f = open(name, 'w')
  f.write(content)
  f.close()

def scrape_medium(url):
  headers = {'User-Agent': 'Mozilla/5.0', 'Content-Language': 'en-US'}
  page = requests.get(url, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  name = getFilepath(id)

  if Path(name).exists():
    return loadJson(name)

  text = list(map(get_text, soup.findAll('p', id=re.compile(r'[^\s]{4}'))))

  writeFile(name, text)

  return json.dumps(text)

