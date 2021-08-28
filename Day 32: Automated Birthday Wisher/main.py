##################### Normal Starting Project ######################
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = ""  # [identity of email account]@[identity of email provider]
PASSWORD = ""

now = datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)

dataframe = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in dataframe.iterrows()}
# print(birthdays_dict)

if today in birthdays_dict:
    random_letter_number = random.randint(1, 3)
    file_path = f"./letter_templates/letter_{random_letter_number}.txt"
    birthday_person = birthdays_dict[today]
    recipient_email = birthday_person["email"]
    recipient_name = birthday_person["name"]
    # print(birthday_person)
    with open(file_path, mode="r") as template:
        letter_content = template.read()
        new_letter = letter_content.replace("[NAME]", recipient_name)

    # new SMTP object that's a way to connect to our email providers SMTP email server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # specify location of the email providers smtp
        connection.starttls()  # a way to secure connection to our email server by encrypting message
        connection.login(user=MY_EMAIL, password=PASSWORD)  # log in by providing a username and password
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=f"{recipient_email}",
                            msg=f"Subject:Happy Birthday {recipient_name}!\n\n{new_letter}")  # send email

