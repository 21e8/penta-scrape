# https://www.reddit.com/r/Bitcoin/comments/2q90m9/coinbase_is_monitoring_your_transactions_poorly/
import re
from bs4 import BeautifulSoup
import requests
import os
import json
from pathlib import Path

def getFilepath(id):
  return os.getcwd() + "/out/reddit/" + str(id) + ".json"

def loadJson(name):
  f = open(name)
  if bool(f):
    return json.load(f)

def writeFile(name, content):
  f = open(name, 'w')
  f.write(content)
  f.close()


def scrape_reddit(url):
  headers = {'User-Agent': 'Mozilla/5.0', 'Content-Language': 'en-US'}
  page = requests.get(url, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  hashId = hash(url)
  name = getFilepath(hashId)

  if Path(name).exists():
    return loadJson(name)

  regex = re.compile('.*RichTextJSON-root.*')

  text = soup.find('div', { 'class': regex })

  dump = json.dumps(text.get_text())

  writeFile(name, dump)

  return dump

