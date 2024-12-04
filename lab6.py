from flask import Blueprint, render_template, request, redirect, session

lab6 = Blueprint('lab6', __name__)

# Создаем список офисов с ценой аренды
offices = []
for i in range(1, 11):
    offices.append({"number": i, "tenant": "", "price": 900 + (i % 3)})

@lab6.route('/lab6')
def main():
    return render_template('lab6/lab6.html')