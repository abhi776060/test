from multiprocessing import context
from django.shortcuts import render
import requests

# Create your views here.

def featch(request):
    context={}
    try:
        if request.method=='POST':
            city_name=request.POST['city']
            api_key='214144f32e1be8724f4c6a16a4d9c70c'
            lang='en'
            api=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
            get_data=requests.get(api).json()
            
            context['name']=get_data['name']
            context['code']=get_data['cod']
            context['main']=get_data['weather'][0]['main']
            context['description']=get_data['weather'][0]['description']
            context['temp']=(((get_data['main']['temp'])))
            str1=float(get_data['main']['feels_like']-273.15)
            context['feels_like']=round(str1,1)
            str2=float(get_data['main']['temp_min']-273.15)
            context['temp_min']=round(str2,1)
            str3=float(get_data['main']['temp_max']-273.15)
            context['temp_max']=round(str3,1)
            context['pressure']=get_data['main']['pressure']
            context['humidity']=get_data['main']['humidity']
            context['speed']=get_data['wind']['speed']
            context['deg']=get_data['wind']['deg']
            context['country']=get_data['sys']['country']
            
        return(render(request,'fetch.html',context=context))
    except:
        context['error']='NO SUCH CITY'
        return(render(request,'fetch.html',context=context))

