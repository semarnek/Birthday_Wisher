import pandas
import datetime
import smtplib


birthdays = pandas.read_csv("birthdays.csv")

recipents = []

monthx = datetime.datetime.now().month
dayx = datetime.datetime.now().day
date = (monthx, dayx)

month_l = {(value["month"], value["day"]):value for (key,value) in birthdays.iterrows()}


if date in month_l:
    name = month_l[date]["name"]
    send_mail = month_l[date]["email"]
    my_email = YOUR_EMAIL
    passw = YOUR_PASS
    letter = ""

    with open("letter_templates/letter_1.txt", "r+") as let:
        for line in let:
            letter = letter + line

        letter = letter.replace("[NAME]", name, 1)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passw)
        connection.sendmail(from_addr=my_email, to_addrs=send_mail,
                            msg=f"Subject: Heppi bortdey beybi\n\n{letter}")
