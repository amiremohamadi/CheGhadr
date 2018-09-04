"""I wrote it only to get product informations from digikala"""

from requests import get
from bs4 import BeautifulSoup

def info(url):
    """write product info in a dict and return it"""
    result = dict()
    page = get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    # find product name and price
    try:
        name = soup.find('meta', {'property': 'og:title'}).attrs.get('content')
        price = soup.find('meta', {'property': 'product:price:amount'}).attrs.get('content', 0)
        img = soup.find('meta', {'property': 'og:image'}).attrs.get('content')
        # add to dict
        result['name'], result['price'], result['img'] = name, price, img
    except: return False

    return result