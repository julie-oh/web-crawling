from time import sleep
import random
import os
import json
import datetime
import csv
from get_low_price import get_low_price
from emailer import send_mail


def main():
    seoul_timezone = datetime.timezone(datetime.timedelta(hours=9))
    date = datetime.datetime.now(tz=seoul_timezone).strftime('%Y-%m-%d %H:%M')
    csv_file = 'low_price_list.csv'
    re = []

    with open('./url_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
           re.append(get_low_price(line.strip(), date))

    is_exists = os.path.exists('./low_price_list.csv')
    previous_dic = {}
    diff_dic = {}

    if is_exists:
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row['product_name']
                previous_dic[key] = row

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['date','product_name', 'low_price', 'product_link']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in re:
            writer.writerow(item)
            product_name = item['product_name']

            if product_name in previous_dic:
                pre_price = previous_dic[product_name]['low_price']
                if int(pre_price) > int(item['low_price']):
                    diff_dic[product_name] = item
                    diff_dic[product_name]['previous_price'] = pre_price

    if len(diff_dic) > 0:
        print('Sending mail:')
        # read email-related configuration from file
        with open('email.json', 'r') as jsonf:
            email_config = json.load(jsonf)  # dict
        send_mail(email_config['to'], diff_dic, email_config['id'], email_config['pwd'])


if __name__ == '__main__':
    while True:
        main()
        sleep(random.randrange(2000, 3600))
