from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date

url = os.environ.get('link')
c = Calendar(urlopen(url).read().decode('utf-8'))
e = list(c.timeline)
vandaag = str(date.today())

print(vandaag)

for x in e:
    if vandaag in str(x._begin):
        print(x.name)
        print(x._begin)
    else:
        continue