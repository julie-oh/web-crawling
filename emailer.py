import time
import smtplib
from email.message import EmailMessage


FROM = 'crawler@milimeal.com'


def send_mail(to: str, itemprice_list: dict, mail_id: str, mail_pwd: str):
    msg = EmailMessage()
    msg['To'] = to
    msg['From'] = FROM

    # make message body
    message_str = ''
    for product_name, item in itemprice_list.items():
        message_str += 'product: {}\n'.format(product_name)
        message_str += '\tPrice change : {} -> {}\n'.format(item['previous_price'], item['low_price'])
        message_str += '\tLink : {}\n'.format(item['product_link'])
        message_str += '\tDateTime : {}\n'.format(item['date'])
        message_str += ('=' * 20 + '\n')  # delimiter
    msg.set_content(message_str)

    msg['Subject'] = 'Lowest price at : ' + time.strftime('%Y-%m-%d %H:%m:%s', time.gmtime())

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(mail_id, mail_pwd)
    s.send_message(msg)
    s.quit()
