import urllib.request
from bs4 import BeautifulSoup

def get_low_price(url):
    with urllib.request.urlopen(url) as response:
        # read decoded html code
        html = response.read().decode('utf-8')

        # parse html
        soup = BeautifulSoup(html, 'html.parser')

        # retrieve low price in html
        re = soup.find_all('span', class_="low_price")

        # type casting and replace to int
        re2 = re[0].find('em', class_='num').string
        re2 = int(re2.replace(',', ''))

        return re2