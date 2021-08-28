"""
when you browser tries to load up a page in Amazon, it also passes a bunch of other information.
e.g. Which browser you're using, which computer you have etc.
These additional pieces of information is passed along in the request Headers.
You can see your browser headers by going to this website:
http://myhttpheader.com/

HINT 1: You'll need to pass along some headers in order for the request to return the actual website HTML.
At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.
"""
# make a Python bot that checks the URL/price of an Amazon item you want, every day at a certain time
from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("./.env")
MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
ITEM_URL = "https://www.amazon.ca/Messy-Kitchen-Deliciously-Fabulously-Copiously/dp/1682619389/ref=sr_1_1?crid=35ATWOEGRFMAF&dchild=1&keywords=renee+paquette+cookbook&qid=1623986108&sprefix=renee+p%2Caps%2C218&sr=8-1"
TARGET_PRICE = 30.00    # pick a higher price for testing eg. 40.00

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=ITEM_URL, headers=header)
webpage_html = response.text
# print(webpage_html)

soup = BeautifulSoup(webpage_html, "lxml")
# print(soup.prettify())

price_tag = soup.find(name="span", class_="a-size-base a-color-price a-color-price")
price_text = price_tag.getText().replace("$", "")
price = float(price_text)
# print(price)

product_name_tag = soup.find(name="span", id="productTitle")
product_name = product_name_tag.getText()
# print(product_name)

# send an email alert if the Amazon item price has dropped past a certain price
if price <= TARGET_PRICE:
    message = f"Subject: Amazon Price Alert!\n\n{product_name}is now ${price}!\nBuy now in the link below!\n{ITEM_URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=message)

