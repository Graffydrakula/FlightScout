class FlightData:
    def __init__(self, price, dep_iata, arr_iata, out_date, return_date, stops):
        self.price = price
        self.departure_airport_iata = dep_iata
        self.arrival_airport_iata = arr_iata
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def cheapest_flight(destination_data):
    data = destination_data

    if data is None or not data:
        cheapest_offer = FlightData(
            price="N/A",
            dep_iata="N/A",
            arr_iata="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )
        return cheapest_offer

    nr_stops = int(len(data[0]['itineraries'][1]['segments'])) - 1

    cheapest_offer = FlightData(
        price=float(data[0]['price']['grandTotal']),
        dep_iata=data[0]['itineraries'][0]['segments'][0]['departure']['iataCode'],
        arr_iata=data[0]['itineraries'][0]['segments'][nr_stops]['arrival']['iataCode'],
        out_date=data[0]['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0],
        return_date=data[0]['itineraries'][1]['segments'][0]['arrival']['at'].split('T')[0],
        stops=nr_stops
    )

    for offer in data:
        if float(offer['price']['grandTotal']) < cheapest_offer.price:
            nr_stops = int(len(offer['itineraries'][1]['segments'])) - 1
            cheapest_offer.price = float(offer['price']['grandTotal'])
            cheapest_offer.dep_iata = offer['itineraries'][0]['segments'][0]['departure']['iataCode']
            cheapest_offer.arr_iata = offer['itineraries'][0]['segments'][nr_stops]['arrival']['iataCode']
            cheapest_offer.out_date = offer['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            cheapest_offer.return_date = offer['itineraries'][1]['segments'][0]['arrival']['at'].split('T')[0]
            cheapest_offer.stops = nr_stops

    return cheapest_offer