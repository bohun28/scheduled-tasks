import pandas as pd
import datetime as dt
import random
import smtplib
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

with open(file = "birthdays.csv") as file:
    birthdays = pd.read_csv(file)

today = dt.datetime.today()

for index, row in birthdays.iterrows():
    if today.month is row["month"] and today.day is row["day"]:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        letters = ["letter_1", "letter_2", "letter_3"]

        letter = random.choice(letters)

        with open(file = f"letter_templates/{letter}.txt") as file:
            letter_template = file.read()
            letter_to_send = letter_template.replace("[NAME]", row["name"])

        # 4. Send the letter generated in step 3 to that person's email address.

        SENDER = os.environ.get("SENDER")
        PASSWORD = os.environ.get("PASSWORD")

        RECEIVER = os.environ.get("RECEIVER")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER,
                to_addrs=RECEIVER,
                msg=f"Subject:Happy Birthday {row['name']}\n\n{letter_to_send}"
            )
