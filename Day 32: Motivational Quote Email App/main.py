# look at the current date and time.
# if it happens to be specific day, then email ourself a random motivational quote from quotes.txt

import smtplib
import datetime as dt
import random

MY_EMAIL = ""  # [identity of email account]@[identity of email provider]
PASSWORD = ""

day_of_week = dt.datetime.now().weekday()
print(day_of_week)

if day_of_week == 0:    # monday starts at 0
    with open("quotes.txt", mode="r") as quotes_data:
        quotes_list = quotes_data.readlines()
        random_quote = random.choice(quotes_list)
    # new SMTP object that's a way to connect to our email providers SMTP email server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # specify location of the email providers smtp
        connection.starttls()  # a way to secure connection to our email server by encrypting message
        connection.login(user=MY_EMAIL, password=PASSWORD)  # log in by providing a username and password
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="",
                            msg=f"Subject:#Motivational Mondays\n\n{random_quote}\n#Motivational Mondays")  # send email

