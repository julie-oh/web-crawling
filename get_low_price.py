import urllib.request
from bs4 import BeautifulSoup

def get_low_price(url):
    url = 'https://search.shopping.naver.com/detail/detail.nhn?nv_mid=12804648154&cat_id=50000391&frm=NVSHMDL&query=&NaPm=ct%3Djmwz6vdc%7Cci%3D2b003e3024fa1a918ef1b431f6f3cdceafc32fbd%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D253e7b00d1ab4680dab951fe67baa41eb224824b'
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

