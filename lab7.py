from flask import Blueprint, render_template, request, abort, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

lab7 = Blueprint('lab7', __name__, static_folder='static')

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='alina_andreicheva_knowledge_base',
            user='alina_andreicheva_knowledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur, commit=False):
    if commit:
        conn.commit()
    cur.close()
    conn.close()

@lab7.route('/lab7')
def main():
    return render_template('lab7/lab7.html')

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn, cur = db_connect()
    cur.execute("SELECT * FROM films;")
    films = cur.fetchall()
    db_close(conn, cur)
    return [dict(film) for film in films]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn, cur = db_connect()
    query = "SELECT * FROM films WHERE id = %s;" if current_app.config['DB_TYPE'] == 'postgres' else "SELECT * FROM films WHERE id = ?;"
    cur.execute(query, (id,) if current_app.config['DB_TYPE'] == 'postgres' else (id,))
    film = cur.fetchone()
    db_close(conn, cur)
    if film is None:
        abort(404)
    return dict(film)

