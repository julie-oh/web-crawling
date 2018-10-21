import urllib.request
from bs4 import BeautifulSoup
import datetime

def get_low_price(url, date):
    with urllib.request.urlopen(url) as response:
        # read decoded html code
        html = response.read().decode('utf-8')

        # parse html
        soup = BeautifulSoup(html, 'html.parser')

        # retrieve low price and product name in html
        get_low_pric_area = soup.find_all('span', class_="low_price")
        get_product_name_area = soup.find_all('div', class_="h_area")

        # type casting and replace to int from low_price and product_name
        low_price = get_low_pric_area[0].find('em', class_='num').string
        low_price = int(low_price.replace(',', ''))
        product_name = get_product_name_area[0].find('h2').string.strip()

        dic = {'date': date, 'product_name': product_name, 'low_price': low_price, 'product_link': url}

        return dic

# if __name__ == '__main__':
#     get_low_price()