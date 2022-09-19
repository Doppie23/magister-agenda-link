from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date, timedelta, datetime

class magister():
    def __init__(self):
        url = os.environ.get('link')
        self.c = Calendar(urlopen(url).read().decode('utf-8'))
        self.e = list(self.c.timeline)

    def anderedag(self, dagenverschil=None):
        self.dagenverschil = dagenverschil
        vandaag = str(date.today())
        if self.dagenverschil == None:
            dag = vandaag
        else:
            vandaag = datetime.strptime(vandaag, "%Y-%M-%d") + timedelta(days=self.dagenverschil)
            dag = vandaag.strftime("%Y-%M-%d")
        return dag

    def printdag(self, dagenverschil=None):
        self.dag = magister.anderedag(self, dagenverschil)
        for x in self.e:
            if self.dag in str(x._begin):
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

agenda = magister()
agenda.printdag() # kan tussen haakjes 1 zetten voor volgende dag en 2 voor dag erna etc...