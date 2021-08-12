from data_manager import DataManager
from datetime import datetime,timedelta
from pprint import pprint
from flight_search import FlightSearch

flight_search = FlightSearch()

data_manager = DataManager()
sheet_data = data_manager.get_a_data()

current_loc = "MAA"
if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    pprint(f"sheet_data:\n {sheet_data}")

    data_manager.data_frame = sheet_data
    data_manager.posting_data()


time_go = datetime.now()+ timedelta(days=1)
time_leave = datetime.now() + timedelta(days=(30))

for destination in sheet_data:
   flight = flight_search.check_flight(
       arriving_code=current_loc,
       departure_code= destination["iataCode"],
       from_date= time_go,
       to_date= time_leave
   )




