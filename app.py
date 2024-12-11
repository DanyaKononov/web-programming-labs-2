from flask import Flask, url_for, redirect, render_template
from lab1 import lab1


app = Flask(__name__)
app.register_blueprint(lab1)


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
                <a href="/lab1">Первая лабораторная</a><br>
                <a href="/lab2">Вторая лабораторная</a><br>
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


@app.route('/lab2/a')
def a():
    return 'без слеша'


@app.route('/lab2/a/')
def a2():
    return 'со слешем'


flower_list = ['Роза', 'Тюльпан', 'Незабудка', 'Ромашка']


@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):


    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return render_template('flowers.html',flower_id=flower_id)


@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Добавлен новый цветок</h1>
        <p>Название нового цветка: {name} </p>
        <p>Всего цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list} </p>
    </body>
</html>        
'''


@app.route('/lab2/all_flowers/')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <p>Полный список: {flower_list} </p>
    </body>
</html>        
'''


@app.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Данил Кононов', 2 , 'ФБИ-21', '3 курс'
    fruits = [{'name': 'Яблоки', 'price': 100},
              {'name': 'Груши', 'price': 120},
              {'name': 'Апельсины', 'price': 80},
              {'name': 'Мандарины', 'price': 95},
              {'name': 'Манго', 'price': 321},
             ]
    return render_template('example.html', name=name, lab_num=lab_num, group=group, course=course, fruits=fruits)


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filters.html', phrase=phrase)


@app.route('/lab2/add_flower/')
def not_add():
    return 'вы не задали имя цветка', 400


@app.route('/lab2/counter_flower/')
def counter_flower():
    return f'''
<!doctype html>
<html>
    <body>
        <p>Всего цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list} </p>
    </body>
</html>        
'''


@app.route('/lab2/clean_flowers/')
def clean_flowers():
    global flower_list
    flower_list = []
    return '''
    <!doctype html>
    <html>
        <body>
        <p>Всё чисто</p>
        <a href="/lab2/all_flowers/">Все цветы</a>
        </body>
    </html>        
    '''


@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
    <!doctype html>
        <html>
            <body>
                <p>{a} + {b} = {a+b}</p>
                <p>{a} - {b} = {a-b}</p>
                <p>{a} x {b} = {a*b}</p>
                <p>{a} / {b} = {a/b}</p
                <p>{a}<sup>{b}</sup> = {a**b}</p>
            </body>
        </html>
        '''


@app.route('/lab2/calc/')
def redir():
    return  redirect("/lab2/calc/1/1")


@app.route('/lab2/calc/<int:a>')
def redir_second(a):
    return  redirect(f"/lab2/calc/{a}/1")


@app.route('/lab2/books/')
def book():
    books = [{'author': 'Марк Твен', 'name': 'Приключения Тома Сойера', 'janr': 'Детская литература', 'count_str': 191},
              {'author': 'Лев Толстой', 'name': 'Война и мир', 'janr': 'Роман', 'count_str': 1300},
              {'author': 'Маргарет Митчелл', 'name': 'Унесённые ветром', 'janr': 'Роман', 'count_str': 640},
              {'author': 'Стивен Кинг', 'name': 'Зелёная миля', 'janr': 'Хоррор', 'count_str': 384},
              {'author': 'Кэтрин Стокетт', 'name': 'Прислуга', 'janr': 'Роман', 'count_str': 512},
              {'author': 'Джордж Р. Р. Мартин', 'name': 'Буря мечей', 'janr': 'Фентези', 'count_str': 1521},
              {'author': 'Борис Львович Васильев', 'name': 'Приключения Тома Сойера', 'janr': 'Военная проза', 'count_str': 352},
              {'author': 'Ли Бардуго', 'name': 'Продажное королевство', 'janr': 'Фентези', 'count_str': 672},
              {'author': 'Борис Львович Васильев', 'name': 'А зори здесь тихие', 'janr': 'История', 'count_str': 128},
              {'author': 'Джонатан Страуд', 'name': 'Пустая могила', 'janr': 'Мистерия', 'count_str': 480},
             ]
    return render_template('books.html', books=books)


@app.route('/lab2/cars/')
def cars_describe():
    cars = [{'img': '/static/Toyota.jpg', 'name': 'Toyota', 'describe': 'Потребителям запомнился их слоган «TOYOTA. Управляй мечтой», под которым бренд рекламировался в течение многих лет. Однако несколько лет назад (в 2013 году) официальный вариант слогана в России изменен на «TOYOTA. Стремиться к лучшему» (оригинальный вариант «Always a better way»).'},
            {'img': '/static/Lexus.png', 'name': 'Lexus', 'describe': 'Происхождение названия Lexus часто относят к комбинации слов luxury (роскошь) и elegance (элегантность). По другой теории Lexus является акронимом фразы luxury exports to U.S.'},
            {'img': '/static/Lamborghini.png', 'name': 'Lamborghini', 'describe': '«The sky will never be the same» («Небо никогда не будет прежним») — это слоган с недавно опубликованного тизера компании Lamborghini, которые выпустили в преддверии дебюта нового спорткара.'},
            {'img': '/static/Porsche.jpg', 'name': 'Porsche', 'describe': '"На гонку в воскресенье, в дорогу в понедельник" – девиз многих водителей Porsche 356 в 1950-х. Ведь 356-я модель могла в выходные выиграть гонку, а потом снова стать надежным автомобилем для повседневной жизни.'},
            {'img': '/static/Ferrari.png', 'name': 'Ferrari', 'describe': 'Фелипе Масса: "Наш девиз - смотреть вперед и не сдаваться" В традиционной авторской колонке на официальном сайте Ferrari, Фелипе Масса вспоминал о Гран При Сингапура, говорил о регламенте машины безопасности и ситуации в чемпионате... Фелипе Масса: "После Гран При Сингапура наш девиз - смотреть вперед и не сдаваться.'},
            ]
    return render_template('cars.html', cars=cars)


@app.route('/lab2/favicon')
def favi():
    favicon = url_for("static", filename="Logo.png")
    return render_template('base.html',favicon=favicon)