from bs4 import BeautifulSoup
import requests

html_doc=requests.get('https://timesofindia.indiatimes.com/rssfeedstopstories.cms').json()
soup = BeautifulSoup(html_doc, 'html.parser')
list1=[]
for x in soup.soup.title:
    list1.append(x)
print(list1)