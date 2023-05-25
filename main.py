import smtplib
import datetime as dt
import pandas as pd

mymail="fake4work@rambler.ru"
tosend="pipo2000@mail.ru"

date=str(dt.date.today()).split("-")
datasearch=str(date[2]+"."+date[1])






data=pd.read_csv("dase.csv")
library=data.to_dict("index")
for key,value in library.items():
    if value["Data"][0:5]==datasearch:
        with smtplib.SMTP_SSL("smtp.rambler.ru", 465) as connect:
            connect.login(user=mymail, password="Arj1com2@")
            connect.sendmail(mymail, value["email"], msg="Subject:YO\n\nYa tut testami zanimaus")










