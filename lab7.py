from flask import Blueprint, render_template, request, abort, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

lab7 = Blueprint('lab7', __name__, static_folder='static')

@lab7.route('/lab7')
def main():
    return render_template('lab7/lab7.html')