import requests
from bs4 import BeautifulSoup
import smtplib
import time

def checkPrice() :
   URL = 'https://www.amazon.in/Tissot-T0674171105100-Wrist-Watch-Men/dp/B0051DA94I/ref=sr_1_4_sspa?keywords=wrist+watch&qid=1562519463&rnid=3576079031&s=watch&sr=1-4-spons&psc=1'
   headers = {"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

   page = requests.get(URL,headers=headers)

   soup = BeautifulSoup(page.content,'html.parser')

   title = soup.find(id="productTitle").get_text()
   price = soup.find(id="priceblock_ourprice").get_text()

   converted_price = price[2:4]

   if(converted_price < 22):
      send_mail()
 
   print(converted_price)
   print(title.strip())


def send_mail():
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.ehlo()

    server.login('your@email.com','yourpassword')

    subject='Price fell down!'
    body = 'check the price at https://www.amazon.in/Tissot-T0674171105100-Wrist-Watch-Men/dp/B0051DA94I/ref=sr_1_4_sspa?keywords=wrist+watch&qid=1562519463&rnid=3576079031&s=watch&sr=1-4-spons&psc=1 '
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
       'your@email.com',
       'another@email.com',
       msg
    )   

    print('Email has been sent!')
    server.quit()



while(True):
   checkPrice()
   time.sleep(60*60*10)





