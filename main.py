from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from flight_data import cheapest_flight
from notification_manager import NotificationManager
import time

# ==================== Set up the Flight Search ====================


TOMORROW = datetime.datetime.now().date() + datetime.timedelta(days=1)
SIX_MONTH = datetime.datetime.now().date() + datetime.timedelta(days=(6*30))

data_manager = DataManager()
sheety_data_prices = data_manager.get_destination_data()
flight_search = FlightSearch()
notificator = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

# Find IATA codes
for row in sheety_data_prices:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.sheety_data_prices = sheety_data_prices
data_manager.update_destination_codes()
print("destination table was created...")

# ==================== Retrieve your customer emails ====================

sheety_data_users = data_manager.get_customer_emails()
customer_email_list = [row['whatIsYourEmail?'] for row in sheety_data_users]

# ==================== Search for Flights ====================

for destination in sheety_data_prices:
    print(f"Searching flights to {destination['city']}...")
    flight_data = flight_search.get_flights(
        origin_code=ORIGIN_CITY_IATA,
        destination_code=destination['iataCode'],
        departure_date=TOMORROW,
        return_date=SIX_MONTH,
    )

    if flight_data is None:
        flight_data = flight_search.get_flights(
            origin_code=ORIGIN_CITY_IATA,
            destination_code=destination['iataCode'],
            departure_date=TOMORROW,
            return_date=SIX_MONTH,
            is_direct=False,
        )


    cheapest_flight_info = cheapest_flight(flight_data)
    print(f"{destination['city']}: {cheapest_flight_info.price}.")
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight_info.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.get_flights(
            origin_code=ORIGIN_CITY_IATA,
            destination_code=destination['iataCode'],
            departure_date=TOMORROW,
            return_date=SIX_MONTH,
            is_direct=False,
        )
        cheapest_flight_info = cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight_info.price}")

    # ==================== Send Notifications and Emails  ====================

    if cheapest_flight_info.price != "N/A" and destination['lowestPrice'] >= float(cheapest_flight_info.price):
        print("Found something good! sending...")
        notificator.send_emails(
            price=cheapest_flight_info.price,
            from_iata=cheapest_flight_info.departure_airport_iata,
            to_iata=cheapest_flight_info.arrival_airport_iata,
            from_time=cheapest_flight_info.out_date,
            until_time=cheapest_flight_info.return_date,
            stops=cheapest_flight_info.stops,
            users=customer_email_list
        )
        print("Send.")


