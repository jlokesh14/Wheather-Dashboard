from django.shortcuts import render

# Create your views here.
import json
import requests
from django.http import HttpResponse

def weather(request):
    weather_data = None
    city = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'eb638b22cc6e05ca8033f7ce37d199bd'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
            }
        else:
            weather_data = 'City not found.'
    if weather_data is None:
        return render(request, 'index.html', {'message': 'Enter city name to get weather details.'})
    elif weather_data == 'City not found.':
        return render(request, 'index.html', {'message': 'City not found, check the spelling of the city name and try again!'})
    else:
        return render(request, 'index.html', {'weather': weather_data, 'city': city})