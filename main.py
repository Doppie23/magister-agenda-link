from ics import Calendar
from urllib.request import urlopen
from dotenv import load_dotenv
load_dotenv()
import os
from datetime import date, timedelta, datetime

class magisteragenda():
    def __init__(self):
        url = os.environ.get('link')
        self.c = Calendar(urlopen(url).read().decode('utf-8'))
        self.e = list(self.c.timeline)
        self.vandaag = str(date.today())

    def anderedag(self, dagenverschil=None):
        self.dagenverschil = dagenverschil
        vandaag = self.vandaag
        if self.dagenverschil == None or 0:
            dag = vandaag
        else:
            vandaag = datetime.strptime(vandaag, "%Y-%M-%d") + timedelta(days=self.dagenverschil)
            dag = vandaag.strftime("%Y-%M-%d")
        return dag

    def rooster(self, dagenverschil=None):
        """
        Kan voor dagenverschil hier niks invullen of 1, 2, 3 etc. \n
        Dan krijg je de volgende dag,
        dus 1 zou morgen geven en 2 overmorgen enzovoort. \n
        0 doet hetzelfde als niks invullen.
        """
        rooster = ''
        dag = magisteragenda.anderedag(self, dagenverschil)
        for x in self.e:
            if dag in str(x._begin):
                rooster += str(x.name) + '\n'
                datumtijd = str(x._begin).split('T')
                datum, tijd = datumtijd
                tijd = str(tijd).split('+')
                tijd, _ = tijd
                tijdzone_correctie = datetime.strptime(tijd, "%H:%M:%S") + timedelta(hours=2)
                tijd = tijdzone_correctie.strftime("%H:%M:%S")
                rooster += str(tijd) + '\n'
            else:
                continue
        rooster = rooster.strip()
        return rooster

    def tijd_eerste_uur(self):
        eersteuur = None
        i = 0
        for x in self.e:
            if self.vandaag in str(x._begin) and  i==0:
                datumtijd = str(x._begin).split('T')
                _, tijd = datumtijd
                tijd = str(tijd).split('+')
                tijd, _ = tijd
                tijdzone_correctie = datetime.strptime(tijd, "%H:%M:%S") + timedelta(hours=2)
                eersteuur = str(tijdzone_correctie.strftime("%H:%M:%S"))
                i += 1 #zodat we alleen maar eerste uur van de dag pakken en niet de rest
            else:
                continue
        return eersteuur

agenda = magisteragenda()
rooster = agenda.rooster() # kan tussen haakjes 1 zetten voor volgende dag en 2 voor dag erna etc...
print(rooster)
eersteuur = agenda.tijd_eerste_uur()
print(eersteuur)
