import time as tm
import yagmail as gm
import pandas as pd
from news import NewsFeeds
import datetime as dt



def send_email ():
     """
     Sends Email through the user's address to all the people listed in the excel file
     """
     time = dt.datetime.now()
     today = time.strftime("%Y-%m-%d")
     yesterday = str(time - dt.timedelta(days = 1))
     news_feed = NewsFeeds(row['interest'], yesterday, today)
     email = gm.SMTP(user = "{Enter_Your_Mail_Address_Here}", password = "{Enter_Password_Here}")
     email.send(to = row['email'], subject = f"Your {row['interest']} news for today!",
                contents = f" Hi {row['name']} {row['surname']}!\n"
                           f"See what's on about {row['interest']}.\n\n"
                           f"{news_feed.get()}")


## While loop to send this automated mail every evening 
while True:
     if time.hour == 17 and time.minute == 0:
          df = pd.read_excel("files/people.xlsx")

          for index, row in df.iterrows():
               send_email()
     tm.sleep(60)




