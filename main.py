import logging
import os
from datetime import date, datetime
from pathlib import Path
from typing import Optional
import urllib.request
from urllib.request import urlopen 

import fire
import pandas as pd
from ics import Calendar

link = 'webcal://calendar.magister.net/api/icalendar/feeds/5bd9ac88-6e89-428c-9870-233085ef6636'

def main():
    req = urllib.request('webcal://calendar.magister.net/api/icalendar/feeds/5bd9ac88-6e89-428c-9870-233085ef6636')
    response = urlopen(req)
    data = response.read()

    cal = Calendar.from_ical(data)

    for event in cal.walk('vevent'):

        date = event.get('dtstart')
        summery = event.get('summary')

        print(str(date))
        print(str(summery))

    return

main()

