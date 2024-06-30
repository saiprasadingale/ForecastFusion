from django.shortcuts import render
import requests
import datetime


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = ''  # Replace with your OpenWeatherMap API key

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            visibility = data.get('visibility', 'N/A')
            wind_speed = data['wind']['speed']
            wind_deg = data['wind']['deg']
            clouds_all = data['clouds']['all']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']

            # sunrise and sunset timestamps to human-readable format
            sunrise_timestamp = data['sys']['sunrise']
            sunset_timestamp = data['sys']['sunset']

            sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            sunset = datetime.datetime.fromtimestamp(sunset_timestamp).strftime('%Y-%m-%d %H:%M:%S')

            country = data['sys']['country']
            timezone = data['timezone']

            context = {
                'city': city,
                'temperature': temperature,
                'feels_like': feels_like,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'pressure': pressure,
                'humidity': humidity,
                'visibility': visibility,
                'wind_speed': wind_speed,
                'wind_deg': wind_deg,
                'clouds_all': clouds_all,
                'description': description,
                'icon': icon,
                'sunrise': sunrise,
                'sunset': sunset,
                'country': country,
                'timezone': timezone,
            }

            return render(request, 'weather/weather.html', context)
        else:
            error_message = f'Error fetching weather data: {response.status_code}'
            return render(request, 'weather/index.html', {'error_message': error_message})

    else:
        return render(request, 'weather/index.html')
