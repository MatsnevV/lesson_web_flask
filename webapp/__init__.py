from flask import Flask, render_template

from webapp.model import db
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    @app.route('/')
    def index():
        title = "NEWs Python"
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = get_python_news()
        return render_template('index.html', weather=weather_text, page_title=title, news_list=news_list)
    return app


#a9b09d28f6334a54b0d104854191203
