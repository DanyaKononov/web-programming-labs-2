from flask import Flask, url_for, redirect, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from db.models import users
from flask_login import LoginManager
from db import db
from os import path
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from kononov_rgz import kononov_rgz

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(kononov_rgz)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Тайна')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'danil_kononov_knowledge_base'
    db_user = 'danil_kononov_knowledge_base'
    db_password = '1234'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "database.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')


@app.errorhandler(404)
def not_found(err):
    paths = url_for("static", filename="lab1/Error404.png")
    return '''
        <!doctype html>
        <html>
            <body>
                <p>Ошибка 404. Не найдено.</p>
                <img src="''' + paths + '''">
            </body>
        </html>
        ''', 404


@app.route("/")
def start():
     return """<!doctype html>
        <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы.
            </title>
        </head>
            <header>
                <h1>НГТУ, ФБ, WEB-программирование,
часть 2. Список лабораторных.</h1>
            </header>
            <body> 
                <h2>Лабораторные работы</h2>
                <a href="/lab1">Первая лабораторная</a><br>
                <a href="/lab2">Вторая лабораторная</a><br>
                <a href="/lab3">Третья лабораторная</a><br>
                <a href="/lab4">Четвёртая лабораторная</a><br>
                <a href="/lab5">Пятая лабораторная</a><br>
                <a href="/lab6">Шестая лабораторная</a><br>
                <a href="/lab7">Седьмая лабораторная</a><br>
                <a href="/lab8">Восьмая лабораторная</a><br>
                <a href="/lab9">Девятая лабораторная</a><br>
                <a href="/kononov_rgz">РГЗ</a><br>
            </body>
            <footer>
                <p>Кононов Данил Александрович, ФБИ-21, 3 курс, 2024</p>
            </footer>
        </html>"""


@app.route("/index")
def starter():
     return """<!doctype html>
        <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы.
            </title>
        </head>
            <header>
                <h1>НГТУ, ФБ, WEB-программирование,
часть 2. Список лабораторных.</h1>
            </header>
            <body> 
                <h2>Лабораторные работы</h2>
                <a href="/lab1">Первая лабораторная</a><br>
                <a href="/lab2">Вторая лабораторная</a><br>
                <a href="/lab3">Третья лабораторная</a><br>
                <a href="/lab4">Четвёртая лабораторная</a><br>
                <a href="/lab5">Пятая лабораторная</a><br>
                <a href="/lab6">Шестая лабораторная</a><br>
                <a href="/lab7">Седьмая лабораторная</a><br>
                <a href="/lab8">Восьмая лабораторная</a><br>
                <a href="/lab9">Девятая лабораторная</a><br>
                <a href="/kononov_rgz">РГЗ</a><br>
            </body>
            <footer>
                <p>Кононов Данил Александрович, ФБИ-21, 3 курс, 2024</p>
            </footer>
        </html>"""


@app.errorhandler(500)
def not_f(err):
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Внутренняя ошибка сервера.</h1>
                <p>На сервере произошла внутренняя ошибка, и он не смог выполнить ваш запрос. Либо сервер перегружен, либо в приложении ошибка.</p>
            </body>
        </html>
        ''', 500

