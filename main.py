from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date, timedelta, datetime

url = os.environ.get('link')
c = Calendar(urlopen(url).read().decode('utf-8'))
e = list(c.timeline)

def anderedag(dagenverschil=None):
    vandaag = str(date.today())
    if dagenverschil == None:
        dag = vandaag
    else:
        vandaag = datetime.strptime(vandaag, "%Y-%M-%d") + timedelta(days=dagenverschil)
        dag = vandaag.strftime("%Y-%M-%d")
    return dag

dag = anderedag()

for x in e:
    if dag in str(x._begin):
        print(x.name)
        datumtijd = str(x._begin).split('T')
        datum, tijd = datumtijd
        tijd = str(tijd).split('+')
        tijd, _ = tijd
        tijdzone_correctie = datetime.strptime(tijd, "%H:%M:%S") + timedelta(hours=2)
        tijd = tijdzone_correctie.strftime("%H:%M:%S")
        print(tijd)
    else:
        continue