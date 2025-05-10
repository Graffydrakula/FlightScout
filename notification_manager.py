import smtplib
from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("SMTP_PASSWORD")
        self.my_number = os.environ.get("MY_NUMBER")
        self.ACCOUNT_SID = os.environ.get("TWILIO_SID")
        self.TWILIO_ENDPOINT = os.environ.get("TWILIO_ENDPOINT")
        self.TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
        self.TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

    def send_sms(self, price, from_iata, to_iata, from_time, until_time, stops):
        nr_stops = ""
        if stops > 0:
            nr_stops = f"with {stops} stop(s)"

        massage = (f"Subject:LOW PRICE ON FLIGHT! \n\nLow price alert! Only £{price} to fly "
                   f"from {from_iata} to {to_iata},{nr_stops} departing on {from_time} and returning on {until_time}.")

        client = Client(self.ACCOUNT_SID, self.TWILIO_TOKEN)
        sms = client.messages.create(
            from_= self.TWILIO_NUMBER,
            body= massage,
            to= self.my_number,
        )
        print(sms.sid)

    def send_emails(self, price, from_iata, to_iata, from_time, until_time, stops, users):
        email_list = users
        if email_list is None:
            return

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)

            nr_stops = ""
            if stops > 0:
                nr_stops = f"with {stops} stop(s)"

            massage = (f"Subject:LOW PRICE ON FLIGHT! \n\nLow price alert! Only {price} British pounds to fly "
                       f"from {from_iata} to {to_iata},{nr_stops} departing on {from_time} and returning on {until_time}.")
            massage = massage.encode('ascii', 'ignore').decode('ascii')

            for email in email_list:
                connection.sendmail(from_addr=self.my_email, to_addrs=email, msg=massage)

