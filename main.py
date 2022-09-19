from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os

url = os.environ.get('link')
c = Calendar(urlopen(url).read().decode('utf-8'))
e = list(c.timeline)

print(e[0]._begin)