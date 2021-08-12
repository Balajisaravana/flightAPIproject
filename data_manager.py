import requests


Sheety_link = "Generate your Sheet"



class DataManager:
            def __init__(self):
               self.data_frame = {}


            def get_a_data(self):
                response = requests.get(url=Sheety_link)
                data = response.json()
                self.data_frame = data["prices"]

                return self.data_frame

            def posting_data(self):
                for city in self.data_frame:
                    new_data = {
                        "price": {
                            "iataCode": city["iataCode"]
                        }
                    }

                    response_data = requests.put(url=f"{Sheety_link}/{city['id']}", json=new_data)
                    print(response_data.text)




