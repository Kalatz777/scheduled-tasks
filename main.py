##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os

# 1. Update the birthdays.csv
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
month = today.month
day = today.day
# today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:

for (index,row) in data.iterrows():
    if row.month == month and row.day == day:
        with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            contents = letter.read()
            new_letter = contents.replace("[NAME]", f"{row["name"]}")

        with smtplib.SMTP("smtp.gmail.com", 587) as email_connection:
            email_connection.starttls()
            email_connection.login(user=MY_EMAIL, password=PASSWORD)
            email_connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n{new_letter}"
            )

