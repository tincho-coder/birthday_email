##################### Extra Hard Starting Project ######################
import os
import pandas as pd
import smtplib
import datetime as dt
import random

# AFTER (secrets stored securely in GitHub)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv
with open("birthdays.csv") as birthdays_file:
    birthdays = pd.read_csv(birthdays_file)

birthday1 = {"name" : ["Juan Martin"], "email" : ["juanmmoron@gmail.com"], "year": 1986, "month": 9, "day": 18}
birthday2 = {"name" : ["Juan Martin"], "email" : ["juanpythoneando@gmail.com"], "year": 1986, "month": 6, "day": 8}

birthdays = pd.concat([pd.DataFrame(birthday1), pd.DataFrame(birthday2), birthdays],ignore_index=True)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.date.today()
if not (birthdays[(birthdays.day == today.day) & (birthdays.month == today.month)]).count(axis=1).empty :
    birthday_of_the_day = birthdays[(birthdays.day == today.day) & (birthdays.month == today.month)]
    for each in birthday_of_the_day.name:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter = letter.read()
            birthday_letter = letter.replace('[NAME]', str(birthday_of_the_day.name.iloc[0]))
            birthday_letter = birthday_letter.replace('Angela', "Juan")
            print(birthday_letter)
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_of_the_day.email,msg=f"Subject:Happy Birthday {str(birthday_of_the_day.name.iloc[0])} \n\n"
                                                                      f"{birthday_letter}")
else:
    print("No birthdays today")
