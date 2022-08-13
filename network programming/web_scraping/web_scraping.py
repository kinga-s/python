# Kinga Syta Web scraping

import requests
from bs4 import BeautifulSoup
import sys

page_url = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"
page = requests.get(page_url)

if page.status_code != 200:
    print("Cannot connect to this website. Server status:", page.status_code)
    sys.exit(1)

if 'text/html' not in page.headers.get('Content-Type'):
    print("Type is not text/html.")
    sys.exit(1)

if bytes('Kursy walut', "utf-8") not in page.content:
    print("This is not a website that contains exchange rates.")
    sys.exit(1)

soup = BeautifulSoup(page.text, features="html.parser")

try:
    table_content = soup.select('tr td')
except:
    print("There is no table on this website.")
    exit(1)

i = 0
for element in table_content:
    if "USD" in element.text:
        break
    i += 1

if i < len(table_content):
    dollar = table_content[i + 1].text.strip()
    try:
        dollar = float(table_content[i + 1].text.strip().replace(",", "."))
    except:
        print("Dollar exchange rate cannot be converted to a float.")
        exit(1)
    if 0 < dollar < 10:
        print("Successfully downloaded dollar's exchange rate:", dollar, "zł")
    else:
        print("Downloaded some float data, but it surely isn't dollar's exchange rate.")
        sys.exit(1)

else:
    print("Dollar's exchange rate wasn't found on the site.")
    sys.exit(1)

sys.exit(0)
