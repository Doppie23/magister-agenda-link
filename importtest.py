from dotenv import load_dotenv
load_dotenv()
import os
from magisteragenda import magisteragenda

link = os.environ.get('link')
agenda = magisteragenda(link)

rooster = agenda.rooster(tijdinrooster=True) # kan tussen haakjes 1 zetten voor volgende dag en 2 voor dag erna etc...
print(rooster)

eersteuur = agenda.tijd_eerste_uur()
# print(eersteuur)