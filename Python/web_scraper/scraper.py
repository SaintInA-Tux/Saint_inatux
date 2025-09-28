"""Simple web scraper (example). Replace the URL and parsing logic to match the target site.
"""
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


HEADERS = {"User-Agent": "freelance-showcase-bot/1.0 (+https://github.com/yourusername)"}




def scrape_products(page_url):
r = requests.get(page_url, headers=HEADERS, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")


products = []
# Example selectors — change to match real site
for card in soup.select('.product')[:50]:
title = card.select_one('.title')
price = card.select_one('.price')
link = card.select_one('a')
products.append({
'title': title.get_text(strip=True) if title else 'N/A',
'price': price.get_text(strip=True) if price else 'N/A',
'url': urljoin(page_url, link['href']) if link and link.has_attr('href') else page_url,
})
return products




if __name__ == '__main__':
if len(sys.argv) < 2:
print('Usage: python scraper.py <page-url>')
sys.exit(1)
url = sys.argv[1]
items = scrape_products(url)
df = pd.DataFrame(items)
out = 'products.csv'
df.to_csv(out, index=False)
print(f'Saved {len(df)} items to {out}')
