import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = '[YOUR MAIL]'
E_GMAIL = "[YOUR APP PASSWORD]"
A_PASSWORD = "[YOUR APP PASSWORD]"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if row.month == today_tuple[0] and row.day == today_tuple[1]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as lt:
            msg = lt.read()
            birthday_letter = msg.replace('[NAME]', f"{row.names}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=A_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{row.email}",
                msg=f"Subject:Birthday Greeting!\n\n{birthday_letter}")
