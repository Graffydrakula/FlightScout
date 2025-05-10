import requests
import os


API_KEY = os.environ.get("AMADEUS_API_KEY")
API_SECRET = os.environ.get("AMADEUS_API_SECRET")
TOKEN_ENDPOINT ="https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_ENDPOINT= "https://test.api.amadeus.com/v1/reference-data/locations/cities"
SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):

        self.amadeus_headers = {}
        self.get_token()

    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.

        city_parameters = {"keyword": city_name.upper(), "max": 1}
        city_request = requests.get(url=CITY_ENDPOINT, headers=self.amadeus_headers, params=city_parameters)
        iata_code = city_request.json()['data'][0]['iataCode']
        print("... looking for IATA code ")

        return iata_code

    def get_token(self):
        # Get access token
        token_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        token_data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        token_request = requests.post(url=TOKEN_ENDPOINT, headers=token_header, data=token_data)
        if token_request.status_code == 200:
            access_token = token_request.json().get("access_token")
            self.amadeus_headers = {"Authorization": f"Bearer {access_token}"}
            print("*token was created*")
        else:
            raise Exception(token_request.json().get("error_description"))

    def get_flights(self, origin_code, destination_code, departure_date, return_date, is_direct=True):
        flights_data = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }

        flight_request = requests.get(url=SEARCH_ENDPOINT, headers=self.amadeus_headers, params=flights_data)
        print("searching...")

        if flight_request.status_code != 200:
            print(f"ERROR, status code: {flight_request.status_code}")
            print("There is no flights or Bad request, check the error text below.")
            print(f"{flight_request.json()['errors'][0]['detail']}")

            return None
        return flight_request.json()['data']

