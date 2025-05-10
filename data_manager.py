import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT_PRICES = os.environ.get("SHEETY_ENDPOINT_PRICES")
        self.SHEETY_ENDPOINT_USERS = os.environ.get("SHEETY_ENDPOINT_USERS")
        self.SHEETY_TOKEN_HEADER = {"Authorization": f"Bearer {os.environ.get("SHEETY_FLIGHT_TOKEN")}"}
        self.sheety_data_prices = []
        self.sheety_data_users = []

    def get_destination_data(self):
        sheety_get_request = requests.get(
            url=self.SHEETY_ENDPOINT_PRICES, headers=self.SHEETY_TOKEN_HEADER)
        self.sheety_data_prices = sheety_get_request.json()['prices']
        return self.sheety_data_prices

    def update_destination_codes(self):
        for city in self.sheety_data_prices:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{self.SHEETY_ENDPOINT_PRICES}/{city['id']}",json=new_data,
                headers=self.SHEETY_TOKEN_HEADER)
            print("updating Google Sheets...")

    def get_customer_emails(self):
        sheety_get_request = requests.get(
            url=self.SHEETY_ENDPOINT_USERS, headers=self.SHEETY_TOKEN_HEADER)
        self.sheety_data_users = sheety_get_request.json()['users']
        return self.sheety_data_users
