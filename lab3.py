from flask import Blueprint, render_template, request, url_for, make_response, redirect
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'Аноним')
    name_color = request.cookies.get('name_color', 'Blue')
    age = request.cookies.get('age', 'XX')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)