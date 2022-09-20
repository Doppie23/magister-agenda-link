from ics import Calendar
from urllib.request import urlopen
from datetime import date, timedelta, datetime

class magisteragenda():
    def __init__(self, link):
        url = link
        self.c = Calendar(urlopen(url).read().decode('utf-8'))
        self.e = list(self.c.timeline)
        self.vandaag = str(date.today())

    def __anderedag(self, dagenverschil):
        vandaag = self.vandaag
        if dagenverschil == 0:
            dag = vandaag
        else:
            vandaag = datetime.strptime(vandaag, "%Y-%M-%d") + timedelta(days=dagenverschil)
            dag = vandaag.strftime("%Y-%M-%d")
        return dag

    def rooster(self, dagenverschil=0):
        """
        Kan voor dagenverschil hier niks invullen of 1, 2, 3 etc. \n
        Dan krijg je de volgende dag,
        dus 1 zou morgen geven en 2 overmorgen enzovoort. \n
        0 doet hetzelfde als niks invullen.
        """
        rooster = ''
        dag = magisteragenda.__anderedag(self, dagenverschil)
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
        """
        Geeft tijd van het eerste uur van de dag. \n
        Kan handig zijn voor automatische wekker.
        """
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