import time
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

import constant

FROM = constant.mail_from

def send_mail(to: str, itemprice_list: dict, mail_id: str, mail_pwd: str):
    msg = MIMEMultipart()
    msg['To'] = to
    msg['From'] = FROM
    msg['Date'] = formatdate(localtime=True)

    # make message body
    message_str = ''
    for product_name, item in itemprice_list.items():
        message_str += 'product: {}\n'.format(product_name)
        message_str += '\tPrice change : {} -> {}\n'.format(item['previous_price'], item['low_price'])
        message_str += '\tLink : {}\n'.format(item['product_link'])
        message_str += '\tDateTime : {}\n'.format(item['date'])
        message_str += ('=' * 20 + '\n')  # delimiter
    msg.attach(MIMEText(message_str))

    msg['Subject'] = 'Lowest price at : ' + time.strftime('%Y-%m-%d %H:%m:%s', time.gmtime())

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open('low_price.xlsx', 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="low_price.xlsx"')
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(mail_id, mail_pwd)
    s.sendmail(FROM, to, msg.as_string())
    s.quit()