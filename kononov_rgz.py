from flask import Blueprint, url_for, redirect, render_template, request, make_response, session, current_app, jsonify
import sqlite3
import json
from os import path
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
kononov_rgz = Blueprint('kononov_rgz', __name__)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'danil_kononov_knowledge_base',
            user = 'danil_kononov_knowledge_base',
            password = '1234'
            )

        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn,cur):
    conn.commit()
    cur.close()
    conn.close()


#Загрузка основной страницы
@kononov_rgz.route('/kononov_rgz')
def kr():
    if 'login' in session:
        login = session['login']
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM mabel")
            mabel = cur.fetchall()
        else: 
            cur.execute(f"SELECT * FROM mabel")
            mabel = [dict(row) for row in cur.fetchall()]
        db_close(conn,cur)
        return render_template('/kononov_rgz/main.html', mabel=mabel, login=login)
    else:
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM mabel")
            mabel = cur.fetchall()
        else: 
            cur.execute(f"SELECT * FROM mabel")
            mabel = [dict(row) for row in cur.fetchall()]
        db_close(conn,cur)
        return render_template('/kononov_rgz/main.html', mabel=mabel)

#Авторизация
@kononov_rgz.route('/kononov_rgz/login', methods=['GET','POST'])
def kr_login():
    if request.method == 'GET':
        return render_template('/kononov_rgz/login.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        conn, cur = db_connect()


        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM users1 WHERE login=%s;", (login,))
            user = cur.fetchone()
        else:
            cur.execute(f"SELECT * FROM users1 WHERE login=?;", (login,))
            user = cur.lastrowid
        if not user:
            db_close(conn,cur)
            return render_template('/kononov_rgz/login.html', error='Логин и/или пароль неверны')
        
        if not check_password_hash(user['password'], password):
            db_close(conn,cur)
            return render_template('/kononov_rgz/login.html', error='Логин и/или пароль неверны')
    session['login'] = login
    db_close(conn,cur)
    return redirect('/kononov_rgz')

#Регистрация
@kononov_rgz.route('/kononov_rgz/registration', methods=['GET','POST'])
def kr_reg():
    if request.method == 'GET':
        return render_template('/kononov_rgz/registration.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        conn, cur = db_connect()


        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"SELECT * FROM users1 WHERE login=%s;", (login,))
            user = cur.fetchone()
        else:
            cur.execute(f"SELECT * FROM users1 WHERE login=?;", (login,))
            user = cur.lastrowid
        if user:
            db_close(conn,cur)
            return render_template('/kononov_rgz/registration.html', error='Пользователь с таким логином уже есть')
        
        password_hash = generate_password_hash(password)
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(f"INSERT INTO users1 (login, password) VALUES (%s, %s);", (login,password_hash))
        else:
            cur.execute(f"INSERT INTO users1 (login, password) VALUES (?, ?);", (login,password_hash))
        db_close(conn,cur)
        session['login'] = login
        return redirect('/kononov_rgz')

#Добавление товара в карзину
@kononov_rgz.route('/kononov_rgz/add_car', methods=['POST'])
def add_car():
    car1 = request.form.get('car1')
    car2 = request.form.get('car2')
    car3 = request.form.get('car3')
    car4 = request.form.get('car4')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"INSERT INTO car (name, price, photo, login) VALUES (%s, %s, %s, %s);", (car1,car2,car3,car4))
    else:
        cur.execute(f"INSERT INTO car (name, price, photo, login) VALUES (?, ?, ?, ?);", (car1,car2,car3,car4))
    db_close(conn,cur)
    return redirect('/kononov_rgz')


#Открытие карзины
@kononov_rgz.route('/kononov_rgz/car', methods=['POST'])
def car():
    car1 = request.form.get('car1')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"SELECT * FROM car WHERE login=%s", (car1,))
        mabel = cur.fetchall()
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=%s", (car1,))
        total_price = cur.fetchone()
    else:
        cur.execute(f"SELECT * FROM car WHERE login=?", (car1,))
        mabel = [dict(row) for row in cur.fetchall()]
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=?", (car1,))
        total_price = cur.lastrowid
    db_close(conn,cur)
    return render_template('/kononov_rgz/car.html', mabel=mabel, car1=car1, total_price=total_price)

#Удалить из карзины 
@kononov_rgz.route("/kononov_rgz/delete_car", methods=['POST'])
def delete_car():
    car1 = request.form.get('car1')
    car11 = request.form.get('car11')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"DELETE FROM car WHERE id=%s", (car11,))
        cur.execute(f"SELECT * FROM car WHERE login=%s", (car1,))
        mabel = cur.fetchall()
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=%s", (car1,))
        total_price = cur.fetchone()
    else:
        cur.execute(f"DELETE FROM car WHERE id=?", (car11,))
        cur.execute(f"SELECT * FROM car WHERE login=?", (car1,))
        mabel = [dict(row) for row in cur.fetchall()]
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=?", (car1,))
        total_price = cur.lastrowid
    db_close(conn,cur)
    return render_template('/kononov_rgz/car.html', mabel=mabel, car1=car1, total_price=total_price)


#Разлогиниться
@kononov_rgz.route("/kononov_rgz/logout", methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect("/kononov_rgz")


#Купить товары
@kononov_rgz.route("/kononov_rgz/buy", methods=['POST'])
def buy():
    car1 = request.form.get('car1')
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute(f"DELETE FROM car WHERE login=%s", (car1,))
        cur.execute(f"SELECT * FROM car WHERE login=%s", (car1,))
        mabel = cur.fetchall()
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=%s", (car1,))
        total_price = cur.fetchone()
    else:
        cur.execute(f"DELETE FROM car WHERE login=?", (car1,))
        cur.execute(f"SELECT * FROM car WHERE login=?", (car1,))
        mabel = [dict(row) for row in cur.fetchall()]
        cur.execute(f"SELECT SUM(price) FROM car WHERE login=?", (car1,))
        total_price = cur.lastrowid
    db_close(conn,cur)
    return render_template('/kononov_rgz/car.html', mabel=mabel, car1=car1, total_price=total_price, thx=True)
    