from flask import Blueprint, render_template, request, redirect, session, current_app
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab5 = Blueprint('lab5', __name__)
@lab5.route('/lab5')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))