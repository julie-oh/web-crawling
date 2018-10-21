import time
import smtplib
from email.message import EmailMessage


FROM = 'crawler@milimeal.com'


def send_mail(to: str, itemprice_list, mail_id: str, mail_pwd: str):
    msg = EmailMessage()
    msg['To'] = to
    msg['From'] = FROM

    # make message body
    message_str = ''
    for item, price in itemprice_list:
        message_str += '{} - {}\n'.format(item, price)
    msg.set_content(message_str)

    msg['Subject'] = 'Lowest price at : ' + time.strftime('%Y-%m-%d %H:%m:%s', time.gmtime())

    print(msg)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(mail_id, mail_pwd)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':  # public static void main(String[] args) {
    send_mail('kaehops@gmail.com', [('lipstick', 123100), ('handcream', 9000)], mail_id=None, mail_pwd=None)
