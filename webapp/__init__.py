from flask import Flask, render_template, flash, url_for, redirect
from flask_login import LoginManager, logout_user, login_user, current_user, login_required

from webapp.forms import LoginForm
from webapp.model import db, News, User
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    
    @app.route('/')
    def index():
        title = "NEWs Python"
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', weather=weather_text, page_title=title, news_list=news_list)
    

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        print(current_user)
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))

        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы разлогинились')
        return redirect(url_for('index'))


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'


    return app


#a9b09d28f6334a54b0d104854191203
