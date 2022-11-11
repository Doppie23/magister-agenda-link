from dotenv import load_dotenv
load_dotenv()
import os
import sys
import subprocess
from magisteragenda import magisteragenda

link = os.environ.get('link')
agenda = magisteragenda(link)

rooster = agenda.rooster(1, False)

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
ahk = 'rooster.ahk'
path = os.path.join(dir_path, ahk)

subprocess.call(["C:\Program Files\AutoHotkey\AutoHotkey.exe", path, rooster])