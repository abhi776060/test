from bs4 import BeautifulSoup as soup
import requests
from datetime import date

today=date.today()
d=today.strftime('%m-%d-%y')

cnn_url='https://timesofindia.indiatimes.com/briefs'
print(d)
