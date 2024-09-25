from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    paths = url_for("static", filename="Error404.png")
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
                <a href="/lab1">Первая лабораторная</a>
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
                <a href="/lab1">Первая лабораторная</a>
            </body>
            <footer>
                <p>Кононов Данил Александрович, ФБИ-21, 3 курс, 2024</p>
            </footer>
        </html>"""

@app.route("/lab1")
def first():
    return '''
<!doctype html>
<html>
<head>
    <title>Лабораторная работа 1</title>
</head>
    <body>
        <p>Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые
 базовые возможности.</p>
        <a href="/">Все лабораторные работы</a>
        <h2>Список роутов:</h2>
        <a href="/">Главная страница через /</a><br>
        <a href="/index">Главная страница через /index</a><br>
        <a href="/lab123">Обработчик ошибки 404</a><br>
        <a href="/lab1/web">HTML-текст(Работа с заголовками)</a><br>
        <a href="/lab1/author">Информация об авторе</a><br>
        <a href="/lab1/oak">Дуб с подключением CSS</a><br>
        <a href="/lab1/counter">Счётчик</a><br>
        <a href="/lab1/cleaner">Очиститель</a><br>
        <a href="/lab1/info">Роут info с переносом на другую страницу</a><br>
        <a href="/lab1/created">Роут 201</a><br>
        <a href="/lab1/error400">Ошибка 400</a><br>
        <a href="/lab1/error401">Ошибка 401</a><br>
        <a href="/lab1/error402">Ошибка 402</a><br>
        <a href="/lab1/error403">Ошибка 403</a><br>
        <a href="/lab1/error405">Ошибка 405</a><br>
        <a href="/lab1/error418">Ошибка 418</a><br>
        <a href="/lab1/error">Ошибка 500 с своим обработчиком</a><br>
        <a href="/lab1/my">Свой роут с нестандартными заголовками</a><br>
    </body>
</html>
'''

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
           <body> 
               <h1>web-сервер на flask</h1>
               <a href="/lab1/author">author</a>
           </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Кононов Данил Александрович"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Групп: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

@app.route("/lab1/oak")
def oak():
    path = url_for("static", filename="oak.jpg")
    connectcss = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + connectcss + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

@app.route('/lab1/counter')
def counter():
    global count
    count +=1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <a href="/lab1/cleaner">Очистить счётчик!</a>
    </body>
</html>
'''

@app.route('/lab1/cleaner')
def clean():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        Счётчик был сброшен до: ''' + str(count) + '''
        <a href="/lab1/counter">Вернутся на счётчик!</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </div>
</html>    
''', 201

@app.route("/lab1/error400")
def err400():
    return "Ошибка 400. Неправильный запрос", 400

@app.route("/lab1/error401")
def err401():
    return "Ошибка 401. Не авторизован", 401

@app.route("/lab1/error402")
def err402():
    return "Ошибка 402. Необходима оплата", 402

@app.route("/lab1/error403")
def err403():
    return "Ошибка 403. Запрещено", 403

@app.route("/lab1/error405")
def err405():
    return "Ошибка 405. Метод не поддерживается", 405

@app.route("/lab1/error418")
def err418():
    return "Ошибка 418. Я - чайник. Сам ты чайник!", 418

@app.route("/lab1/error")
def error():
    first_num = 10
    second_num = 0
    return '''
    <!doctype html>
        <html>
            <body>
                Деление: ''' + first_num/second_num + '''
            </body>
        </html>
        '''
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

@app.route("/lab1/my")
def new():
    pic = url_for("static", filename="Garou.jpg")
    return '''
        <!doctype html>
        <html>
            <body>
                <p>Гароу (ガロウ, Гаро:; Азбука: Гаро) — антизлодей, мастер боевых искусств, самопровозглашённый «Охотник на героев», самопровозглашённый «Монстр» и главный противник Ассоциации Героев и Ассоциации Монстров. Он являлся учеником Бэнга, но был изгнан из его додзё после того, как устроил там бойню.</p>
                <img src="''' + pic + '''">
            </body>
        </html>
        ''', 200, {
            'X-Range': 'dimple',
        }