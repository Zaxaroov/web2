from flask import Blueprint, render_template, request, redirect, session

lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    # Если в сессии уже есть поздравление, показываем его
    if 'message' in session and 'image' in session:
        message = session['message']
        image = session['image']
        return render_template('lab9/congratulations.html', message=message, image=image)
    return render_template('lab9/form_name.html')

@lab9.route('/lab9/age', methods=['POST'])
def get_age():
    session['name'] = request.form.get('name')
    return render_template('lab9/form_age.html', name=session['name'])

@lab9.route('/lab9/gender', methods=['POST'])
def get_gender():
    session['age'] = request.form.get('age')
    return render_template('lab9/form_gender.html', name=session['name'], age=session['age'])

@lab9.route('/lab9/preference', methods=['POST'])
def get_preference():
    session['gender'] = request.form.get('gender')
    return render_template('lab9/form_preference.html', name=session['name'])

@lab9.route('/lab9/sub_preference', methods=['POST'])
def get_sub_preference():
    session['preference'] = request.form.get('preference')
    if session['preference'] == 'tasty':
        return render_template('lab9/form_sub_preference_tasty.html', name=session['name'])
    else:
        return render_template('lab9/form_sub_preference_beautiful.html', name=session['name'])


@lab9.route('/lab9/congratulations', methods=['GET', 'POST'])
def congratulations():
    # Если поздравление уже есть в сессии, показываем его
    if 'message' in session and 'image' in session:
        return render_template('lab9/congratulations.html', message=session['message'], image=session['image'])

    # Генерация поздравления при новом прохождении
    session['sub_preference'] = request.form.get('sub_preference')

    name = session['name']
    age = int(session['age'])
    gender = session['gender']
    preference = session['preference']
    sub_preference = session['sub_preference']

    if gender == 'male':
        pronoun = 'ты быстро вырос, был умным и счастливым'
    else:
        pronoun = 'ты быстро выросла, была умной и счастливой'

    if preference == 'tasty':
        if sub_preference == 'sweet':
            gift = 'мешочек конфет'
            image = '/static/lab9/candy.png'
        else:
            gift = 'праздничное блюдо'
            image = '/static/lab9/meal.png'
    else:
        if sub_preference == 'sport':
            gift = 'футбольный мяч'
            image = '/static/lab9/football.png'
        else:
            gift = 'украшение'
            image = '/static/lab9/jewelry.png'

    message = f"Поздравляю тебя, {name}! Желаю, чтобы {pronoun}. Вот тебе подарок — {gift}."

    # Сохраняем данные поздравления в сессии
    session['message'] = message
    session['image'] = image

    return render_template('lab9/congratulations.html', message=message, image=image)

@lab9.route('/lab9/reset', methods=['POST'])
def reset():
    # Очищаем сессию
    session.clear()
    # Возвращаем начальную страницу
    return render_template('lab9/form_name.html')