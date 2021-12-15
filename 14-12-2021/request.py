import requests

respons = requests.get('https://www.youtube.com/')

#print(respons)#200

print(respons.encoding)