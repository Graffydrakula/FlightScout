# FlightScout ✈️

FlightScout is a simple Python project that helps you find cheap flight tickets.  
It checks prices for different destinations and notifies you when there is a good deal.  
It uses **Amadeus API** for flight data and **Google Sheets** (via Sheety API) as your destination list.

---

## 📌 Features

- Get destination data from a Google Sheet
- Find flight deals using Amadeus API
- Send notification when ticket price is lower than your target
- Work with IATA codes, travel dates, and flight offers
- Easy-to-read code, divided into modules

---

## 🛠️ Technologies Used

- Python 3
- `requests`, `datetime`
- [Amadeus Flight Offers API](https://developers.amadeus.com/)
- [Sheety API](https://sheety.co/) for Google Sheets
- [Optional] Twilio or email for notifications

---

## 📁 Project Structure

FlightScout/
├── main.py # Main script to run the app
├── data_manager.py # Gets and updates data from Google Sheet
├── flight_search.py # Connects to Amadeus API and searches flights
├── flight_data.py # Handles flight offer data
├── notification_manager.py # Sends messages if good prices are found
├── requirements.txt # List of needed Python packages

---

## 📊 Google Sheet Structure

The project uses Google Sheet as a database. Each row shows one destination:

| Column Name   | Description                                 |
|---------------|---------------------------------------------|
| City          | Destination city name                       |
| IATA Code     | 3-letter airport code (e.g., PAR for Paris) |
| Lowest Price  | Maximum price you want to pay for a ticket  |

You can change this sheet to control what flights the app checks.

---

## 🚀 How to Run the Project

1. Clone this repo or download the files.
2. Create a virtual environment (optional but recommended):

python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Add your credentials (Amadeus API, Sheety, etc.) — see below.
5. Run the program:

python main.py

---

## 🔐 Environment Variables

Create a `.env` file or export variables manually:

AMADEUS_API_KEY=your_key
AMADEUS_API_SECRET=your_secret
SHEETY_TOKEN=your_token
SHEETY_ENDPOINT=https://api.sheety.co/...
ORIGIN_CITY_IATA=your_city


❗ Never share your real `.env` file on GitHub.

---

## 📦 Possible Improvements

- Add error handling (for example, when API limit is reached)
- Write tests with `unittest` or `pytest`
- Use `logging` instead of `print()`
- Add a web version (using Flask or FastAPI)

---

## 📧 Contact

If you have questions or want to collaborate, feel free to contact me:

- 📧 Email: ivan.s.davydenko@gmail.com  
- 💼 LinkedIn: [linkedin.com/in/ivan-s-davydenko](https://linkedin.com/in/ivan-s-davydenko)

---

### ✅ Status

📂 This project is finished and ready to be shown in portfolio.  
🧠 Built with learning and growth in mind.



