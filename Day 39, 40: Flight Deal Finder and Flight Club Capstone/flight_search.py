import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv("./.env")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def return_code(self, city_name):
        locations_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        tequila_locations_params = {
            "term": city_name,
            "location_types": "city"
        }

        tequila_locations_headers = {
            "apikey": TEQUILA_API_KEY,
        }

        tequila_locations_response = requests.get(url=locations_endpoint,
                                                  params=tequila_locations_params,
                                                  headers=tequila_locations_headers)

        result = (tequila_locations_response.json())
        code = result["locations"][0]["code"]
        return code

    def search_flights(self, origin_city_code, destination_city_code, tomorrow_date, six_months_from_tomorrow):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        tequila_search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": tomorrow_date.strftime("%d/%m/%Y"),
            "dateTo": six_months_from_tomorrow.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,  # returns the one cheapest flight to every city covered by the to parameter
            "max_stopovers": 0, # direct flights only
            "curr": "CAD"
        }
        tequila_search_headers = {
            "apikey": TEQUILA_API_KEY,
        }
        tequila_get_response = requests.get(url=search_endpoint, params=tequila_search_params,
                                            headers=tequila_search_headers)
        # print(tequila_get_response.text)
        try:
            result = tequila_get_response.json()["data"][0]
            print(result)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        # pass resulting data into FlightData
        flight_data = FlightData(
            price=result["price"],
            origin_city=result["route"][0]["cityFrom"],
            origin_airport=result["route"][0]["flyFrom"],
            destination_city=result["route"][0]["cityTo"],
            destination_airport=result["route"][0]["flyTo"],
            out_date=result["route"][0]["local_departure"].split("T")[0],   # initial trip date
            return_date=result["route"][1]["local_departure"].split("T")[0]  # return trip date
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data