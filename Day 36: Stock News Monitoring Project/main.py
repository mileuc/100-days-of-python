import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("./.env")

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER_NUM = os.getenv("SENDER_NUM")
RECIPIENT_NUM = os.getenv("RECIPIENT_NUM")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "qInTitle": COMPANY_NAME,  # q searches title and content, qInTitle searches for just the title
    "apikey": NEWS_API_KEY
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_api_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_api_response.json()
# print(stock_data["Time Series (Daily)"])
# stock_data["Time Series (Daily)"].items() turns each key-value into a 2-element tuple
daily_closing_prices = [value["4. close"] for (key, value) in stock_data["Time Series (Daily)"].items()]
yesterday_closing_price = float(daily_closing_prices[1])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = float(daily_closing_prices[2])
print(yesterday_closing_price, day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_diff = yesterday_closing_price - day_before_yesterday_closing_price
if price_diff >= 0:
    arrow = "🔺"
else:
    arrow = "🔻"

abs_price_diff = abs(price_diff)
print(abs_price_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_price_diff = (abs_price_diff / yesterday_closing_price) * 100
rounded_percentage_diff = round(percentage_price_diff, 1)
print(percentage_price_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_price_diff > 4:   # use a smaller number to test this, if necessary
    # print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    latest_3_articles = articles[:3]
    # print(len(latest_3_articles))

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    latest_3_title_and_descriptions = [(article["title"], article["description"]) for article in latest_3_articles]
    # alternate way:
    # formatted_article = [f"{STOCK_NAME}: {arrow}{rounded_percentage_diff}% \nHeadline: {article['title']}\nBrief: {article['description']} for article in latest_3_articles]
    print(latest_3_title_and_descriptions)

    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)  # set up Twilio client using sid and token
    # create message that will be sent to us
    for article in latest_3_title_and_descriptions:
        title = article[0]
        description = article[1]

        message = client.messages.create(
            body=f'{STOCK_NAME}: {arrow}{rounded_percentage_diff}% \nHeadline: {title}\nBrief: {description}',
            from_=SENDER_NUM,
            to=RECIPIENT_NUM
        )

        print(message.status)  # just to make sure it was sent successfully


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

