from flask import Flask, url_for, redirect, render_template
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)


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

