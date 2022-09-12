from ics import Calendar
from urllib.request import urlopen

url = r'https://calendar.magister.net/api/icalendar/feeds/2187c94f-24b9-46c8-83b1-822d6af3ba27'
c = Calendar(urlopen(url).read().decode('utf-8'))

print(c)

print(c.events)