
from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET

context={}
# Create your views here.
def newz(request):

   
    url='https://newsapi.org/v2/everything?domains=wsj.com&apiKey=7cf68483bb604c169cf03488a634941a'
    response=requests.get(url).json()
    dict1={}
    for x in response['articles']:
            y=x['publishedAt'][:16]
            dict2={}
            dict2['content']=x['content']
            dict2['description']=x['description']
            dict2['title']=x['title']
            dict1[y]=dict2
            
    context['data']=dict1
    # print(context)
    return render(request,'newz.html',context=context)
def discription(request,str1):
    # print(context['data'][str1])
    context1={}
    context1['content']=context['data'][str1]['content']
    context1['description']=context['data'][str1]['description']
    context1['title']=context['data'][str1]['title']
    return render(request,'discription.html',context=context1)

