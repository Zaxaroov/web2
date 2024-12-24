from flask import Blueprint, render_template, request, redirect, abort, jsonify, current_app, session
from werkzeug.security import check_password_hash, generate_password_hash


lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    login = session.get('login', 'Anonymous')
    return render_template('lab8/lab8.html', login=login)