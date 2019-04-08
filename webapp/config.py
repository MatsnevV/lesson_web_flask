from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "a9b09d28f6334a54b0d104854191203"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "afasfasf42336**%!#$Jqegqegqezxcxbbnm)(&(^__)+@#$@532225247890-=09H325>CKAOEPfdsgH:"


REMEMBER_COOKIE_DURATION = timedelta(days=5)
