from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from db import db
from os import path
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
import os

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет') 
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'ilya_zaxarov_orm'
    db_user = 'ilya_zaxarov_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "roman_chukaev_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)


@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
        <title>Захаров Илья Максимович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>
                <li>
                    <a href="/lab2">Лабораторная работа 2</a>
                </li>
                <li>
                    <a href="/lab3">Лабораторная работа 3</a>
                </li>
                 <li>
                    <a href="/lab4">Лабораторная работа 4</a>
                </li>
                <li>
                    <a href="/lab5">Лабораторная работа 5</a>
                </li>
                <li>
                    <a href="/lab6">Лабораторная работа 6</a>
                </li>
                <li>
                    <a href="/lab7">Лабораторная работа 7</a>
                </li>
                <li>
                    <a href="/lab8/">Лабораторная работа 8</a>
                </li>
                <li>
                    <a href="/lab9/">Лабораторная работа 9</a>
                </li>
            </ol>
        </div>

        <footer class="footer">
            &copy; Захаров Илья, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''


@app.route('/lab2/a')
def a():
    return 'без слеша'

@app.route('/lab2/a/')
def a2():
    return 'со слешом'

flower_list = ['тюльпан', 'роза', 'хризантема','ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >=len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Цветы</title>
</head>
<body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: ''' + {name} +'''</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
</body>
</html>
'''

@app.route('/lab2')
def example():
    name = 'Захаров Илья'
    group = 'ФБИ-24'
    number = '2'
    curs = '3'
    return render_template('lab2.html', name=name, group=group, number=number, curs=curs)


