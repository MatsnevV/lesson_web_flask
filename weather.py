import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        "key": "a9b09d28f6334a54b0d104854191203",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather: #прверка
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

#пока нет проверки 

if __name__ == "__main__":
    print(weather_by_city('Moscow,Russia'))


