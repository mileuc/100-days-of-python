"""
Part 1: Find Flight Deals
Have a Google sheet which keeps track of locations we want to visit and their lowest prices, with a price
cutoff specified.
Then feed this data into a flight search API which will run every day searching through the locations and
looking for the cheapest flight in the next six months.
When a flight is found that is actually cheaper than the predefined price, then that date and price will be
sent to our phone via the Twilio SMS module.

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
achieve the program requirements.

Part 2: Turn project into a full-product where we can sign up users to use our service
"""

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "YYC"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# take all the records in the Google Sheet and place them in a variable
sheet_data = data_manager.acquire_records()

# check if each record in sheet_data contains a value for the "iataCode" column
# if empty, pass the city name in sheet_data FlightSearch class and return the IATA code
# use the response from the FlightSearch class to update the record

for record in sheet_data:
    if record["iataCode"] == "":
        record["iataCode"] = flight_search.return_code(record["city"])  # fill empty iataCode fields
# print(sheet_data)

# update Google Sheet records with updated sheet_data records
data_manager.update_records(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_tomorrow = tomorrow + timedelta(weeks=24)
# print(tomorrow, six_months_from_tomorrow)

# use Flight Search API to check for cheapest flights from tomorrow to 6 months later for all cities in Google Sheet
for record in sheet_data:
    flight = flight_search.search_flights(ORIGIN_CITY_CODE, record["iataCode"], tomorrow, six_months_from_tomorrow)
    # if price is lower than the lowest price listed in Google Sheet, then send SMS with the Twilio API
    # SMS should have IATA codes for departure and destination airports, departure and destination city, flight price/dates
    if flight.price < record["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                    f" to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to "
                    f"{flight.return_date}.",
        )
# print(sheet_data)


