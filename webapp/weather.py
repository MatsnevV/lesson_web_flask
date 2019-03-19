from flask import current_app
import requests



def weather_by_city(city_name):
    weather_url = current_app.config["WEATHER_URL"]
    params = {
        "key": current_app.config["WEATHER_API_KEY"],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather: #прверка
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException):
        print('сетевая ошибка')
        return False
    return False
    

#пока нет проверки 

if __name__ == "__main__":
    print(weather_by_city('Moscow,Russia'))


