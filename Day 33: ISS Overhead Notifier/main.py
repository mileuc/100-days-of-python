import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.048615
MY_LONG = -114.070847
MY_EMAIL = ""  # [identity of email account]@[identity of email provider]
PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Allow a margin of error for the ISS being overhead
    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # specify location of the email providers smtp
            connection.starttls()  # a way to secure connection to our email server by encrypting message
            connection.login(user=MY_EMAIL, password=PASSWORD)  # log in by providing a username and password
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Go Outside and Look Up!\n\nHey,\nGo outside and look up in the sky!\n"
                                    "You should see the ISS station outside!")




