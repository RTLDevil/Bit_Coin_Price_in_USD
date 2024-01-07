from pycoingecko import CoinGeckoAPI
import smtplib
import os
my_email = os.environ.get("Email")
App_password = os.environ.get("App_password")
def get_btc_price():
    cg = CoinGeckoAPI()
    try:
        # Get the current price of Bitcoin in USD
        data = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc_price = data['bitcoin']['usd']
        return btc_price
    except Exception as e:
        return f"Error: {e}"
def get_emails():
    with open("emails.txt", "r") as file:
        emails = file.read().splitlines()
    return emails
btc_price = get_btc_price()
emails = get_emails()
for email in emails:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=App_password)
    connection.sendmail(from_addr=my_email, to_addrs=email,
                        msg=f"SUBJECT: BTC PRICE \n\n This is Program Created By Malik Ali Draz to let all of you know's what is the current Price of the BTC in USD.\nCurrent BTC Price in USD: ${btc_price}.")
    connection.close()