from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date, timedelta, datetime

url = os.environ.get('link')
c = Calendar(urlopen(url).read().decode('utf-8'))
e = list(c.timeline)
vandaag = str(date.today())

# print(vandaag)

for x in e:
    if vandaag in str(x._begin):
        print(x.name)
        datumtijd = map(str,str(x._begin).split('T'))
        datum, tijd = datumtijd
        tijd = map(str,str(tijd).split('+'))
        tijd, _ = tijd
        tijdzone_correctie = datetime.strptime(tijd, "%H:%M:%S") + timedelta(hours=2)
        tijd = tijdzone_correctie.strftime("%H:%M:%S")
        print(tijd)
    else:
        continue