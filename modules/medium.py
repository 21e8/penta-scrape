import re
from bs4 import BeautifulSoup
import requests
import json

def get_text(el):
  return el.get_text()

def scrape_medium(url):
  headers = {'User-Agent': 'Mozilla/5.0', 'Content-Language': 'en-US'}
  page = requests.get(url, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  text = list(map(get_text, soup.findAll('p', id=re.compile(r'[^\s]{4}'))))

  return json.dumps(text)

