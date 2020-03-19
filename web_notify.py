import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Amazfit-Lite-3ATM-Smart-Watch/dp/B07WQWDYJ7/ref=sr_1_19?dchild=1&keywords=smart+watches&qid=1584593486&sr=8-19'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').text

    price = soup.find(id='priceblock_ourprice').text
    converted_price = price[2:7]
    converted_price = converted_price.replace(',','')
    converted_price = float(converted_price)

    if(converted_price<3000):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price>3000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gaddammahesh342@gmail.com','kkppupovgqumhkjb')

    subject = 'Price fell down!'

    body = 'check the amazon link https://www.amazon.in/Amazfit-Lite-3ATM-Smart-Watch/dp/B07WQWDYJ7/ref=sr_1_19?dchild=1&keywords=smart+watches&qid=1584593486&sr=8-19'

    msg = f"subject : {subject}\n\n{body}"

    server.sendmail(
        'maheshstoner@gmail.com'
        'gaddammahesh342@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

check_price()
