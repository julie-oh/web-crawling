from time import sleep
import random
import os
import json
import datetime
import csv
import pandas as pd
from get_low_price import get_low_price
from emailer import send_mail

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main():
    seoul_timezone = datetime.timezone(datetime.timedelta(hours=9))
    date = datetime.datetime.now(tz=seoul_timezone).strftime('%Y-%m-%d %H:%M')
    csv_file = 'low_price_list.csv'
    re = []

    # read configuration
    with open('config.json', 'r') as jsonf:
        config = json.load(jsonf)  # dict

    cred = credentials.Certificate(config['db_api_key'])
    firebase_admin.initialize_app(cred, {
        'databaseURL': config['db_address']
    })

    sales = db.reference(config['db_ref'])
    get_db = sales.get()

    for i in get_db:
        re.append(get_low_price(get_db[i]['url'],date))

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

    make_excel()

    if len(diff_dic) > 0:
        print('Sending mail:')
        # read email-related configuration from file
        send_mail(config['to'], diff_dic, config['id'], config['pwd'])


def make_excel():
    df_new = pd.read_csv('./low_price_list.csv')
    writer = pd.ExcelWriter('low_price.xlsx')
    df_new.to_excel(writer, index=False)
    writer.save()


if __name__ == '__main__':
    while True:
        main()
        sleep(random.randrange(2000, 3600))
