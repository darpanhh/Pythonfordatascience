from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/job-search?keywords=python&location=&experience=',verify=False).text
print(html_text)