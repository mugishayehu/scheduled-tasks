# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
my_email = os.environ.get("my_email")
password = os.environ.get("password")

data = pandas.read_csv("./birthdays.csv")

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)
bd_row = data[(data.month==today_month) & (data.day==today_day)]

if not bd_row.empty:
    for index, row in bd_row.iterrows():
        person_born = row["name"]
        person_email = row["email"]
        birthday = (row["month"], row["day"])
    letter_list = ["letter_1.txt", "letter_2.txt","letter_3.txt" ]
    random_letter = random.choice(letter_list)
    
    if today_tuple == birthday:
        with open(f"./letter_templates/{random_letter}") as file_folder:
            file = file_folder.read()
            data_file = file.replace("[NAME]", person_born)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email ,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=person_email,
                                msg=f"subject:Happy Birthday\n\n {data_file}")


