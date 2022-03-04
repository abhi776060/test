from bs4 import BeautifulSoup
import requests

html_doc=requests.get('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
soup = BeautifulSoup(html_doc.json(), 'html.parser')
list1=[]
for x in soup.soup.title:
    list1.append(x)
# print(list1)