import csv
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, password, recipient_email, coin_name, symbol):
    subject = f'New Coin added to {coin_name} Ecosystem!'
    body = f'{symbol} has been added to {coin_name} Ecosystem'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, recipient_email, msg.as_string())

def check_and_send_emails():
    sender_email = 'gregfreefilms@gmail.com' 
    recipient_email = 'gregfreefilms@gmail.com'
    password = 'ieyhnnrruvmaslnu'  

    file_names = [
    "terra_final.csv",
    "solana_final.csv",
    "polygon_final.csv",
    "polkadot_final.csv",
    "osmosis_final.csv",
    "optimism_final.csv",
    "injective_final.csv",
    "fantom_final.csv",
    "ethereum_final.csv",
    "cosmos_final.csv",
    "cardano_final.csv",
    "avalanche_final.csv",
    "aptos_final.csv"]

    for file_name in file_names:
        coin = file_name.split('_')[0]
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                if any(row):  # Check if any field in the row has data
                    send_email(sender_email, password, recipient_email, coin.capitalize(), row[0])
                    break  # Assuming you want to send only one email per coin

if __name__ == '__main__':
    check_and_send_emails()
