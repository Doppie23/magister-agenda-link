from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date

url = os.environ.get('link')
c = Calendar(urlopen(url).read().decode('utf-8'))
e = list(c.timeline)
vandaag = date.today()

print(vandaag)

print(e[0].name)
print(e[0]._begin)

print(e[4].name)
print(e[4]._begin)