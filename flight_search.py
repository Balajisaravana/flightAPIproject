import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = GET UR API



class FlightSearch:




        def get_destination_code(self, city_name):
           link_point = f"{TEQUILA_ENDPOINT}/locations/query"
           headers ={
               "apikey":TEQUILA_API_KEY
           }
           query = {
               "term": city_name,
               "location_types": "city"
           }

           response = requests.get(url=link_point,headers=headers,params=query)
           value =  response.json()["locations"]
           code = value[0]["code"]
           return code

        def check_flight(self, arriving_code, departure_code, from_date, to_date):

            headers = {
                "apikey": "7sGEgxpJoXKSPM67AQXZt_oy4sgEkpTV"
            }
            query = {
                "fly_from": arriving_code,
                "fly_to": departure_code,
                "date_from": from_date.strftime("%d/%m/%y"),
                "date_to": to_date.strftime("%d/%m/%y"),
                # "return_from":23/7/2021,
                # "return_to":1/8/2021,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"

            }

            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )

            try:
                data = response.json()["price"][0]
                print(data)


            except IndexError:
                print(f"the following {departure_code} not found")
                return None

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
