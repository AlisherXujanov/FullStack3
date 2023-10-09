import requests
from bs4 import BeautifulSoup

new_york_times = requests.get('https://www.nytimes.com/')
html_doc = BeautifulSoup(new_york_times.text, 'html.parser')
print(html_doc.prettify())
