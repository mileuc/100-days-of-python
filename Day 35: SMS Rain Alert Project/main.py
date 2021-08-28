import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LAT = 0
LON = 0
API_KEY = ""
account_sid = ""
auth_token = ""

weather_parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",  # exclude parts of the weather data as comma-delimited list w/o spaces
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"])

# run script every morning at 7AM, check the weather for 12 hours, and send a text if it will rain today
# get a hold of the weather condition, typically provided through an ID (hourly.weather.id, from reading the docs)
# https://openweathermap.org/weather-conditions
# if ID is less than 700, we need an umbrella
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"] # index 0 = first weather condition, if there are multiple
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # use twilio API to send text messages or phone calls or have a virtual phone number in any country
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(account_sid, auth_token, http_client=proxy_client)  # set up Twilio client using sid and token
    # create message that will be sent to us
    message = client.messages.create(
                         body="It's going to rain today. Remember to bring an ☂",
                         from_='',
                         to=''  # the # used to sign up to Twilio, which is listed as a verified caller ID
                     )
    print(message.status)  # just to make sure it was sent successfully
