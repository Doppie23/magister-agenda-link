link = r'https://calendar.magister.net/api/icalendar/feeds/5bd9ac88-6e89-428c-9870-233085ef6636'

import requests

text = requests.get(link).text

print(text)