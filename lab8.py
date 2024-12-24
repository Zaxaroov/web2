from flask import Blueprint, render_template, request, redirect, abort, jsonify, current_app, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def main():
    login = session.get('login', 'Anonymous')
    return render_template('lab8/lab8.html', login=login)


@lab8.route('/lab8/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    login_exist = users.query.filter_by(login = login_form).first()
    if login_exist:
        return render_template('lab8/register.html', error = 'Такой пользователь уже существует')
    
    if not (login_form or password_form):
        return render_template('lab8/register.html', error = 'Заполните все поля')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember = False)
    return render_template('/lab8/lab8.html', login=login_form)


@lab8.route('/lab8/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember = request.form.get('remember') == 'on'

    if not (login_form or password_form):
        return render_template('lab8/login.html', error = 'Заполните все поля')

    user = users.query.filter_by(login = login_form).first()
    

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember = remember)
            return render_template('lab8/lab8.html', login=login_form)
    
    return render_template('/lab8/login.html', error = 'Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/articles')
@login_required
def article_list():
    return 'Список статей'


@lab8.route('/lab8/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')


@lab8.route('/lab8/list')
@login_required
def list_articles():
    user_articles = articles.query.filter_by(login_id=current_user.id).order_by(
        articles.is_favorite.desc(),
        articles.id.asc()
    ).all()

    article_data = [
        {
            'id': article.id,
            'title': article.title,
            'article_text': article.article_text,
            'is_favorite': article.is_favorite,
        }
        for article in user_articles
    ]

    return render_template('lab8/articles.html', articles=article_data)

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create_article.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not (title and article_text):
        return render_template('lab8/create_article.html', error='Заполните все поля')

    new_article = articles(
        login_id=current_user.id,
        title=title,
        article_text=article_text,
        is_favorite=False,
        is_public=False,
        likes=0
    )
    db.session.add(new_article)
    db.session.commit()

    return redirect('/lab8/list')

@lab8.route('/lab8/delete_article', methods=['POST'])
@login_required
def delete_article():
    article_id = request.form.get('article_id')

    if not article_id:
        return redirect('/lab8/list', code=400)

    article_to_delete = articles.query.filter_by(id=article_id, login_id=current_user.id).first()

    if not article_to_delete:
        return redirect('/lab8/list', code=404)

    db.session.delete(article_to_delete)
    db.session.commit()

    return redirect('/lab8/list')


@lab8.route('/lab8/edit_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.filter_by(id=article_id, login_id=current_user.id).first()

    if not article:
        return redirect('/lab8/list', code=404)

    if request.method == 'GET':
        return render_template(
            'lab8/edit_article.html',
            article={
                'id': article.id,
                'title': article.title,
                'article_text': article.article_text,
            }
        )

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not (title and article_text):
        return render_template(
            'lab8/edit_article.html',
            article={
                'id': article.id,
                'title': title,
                'article_text': article_text,
            },
            error='Заполните все поля'
        )

    article.title = title
    article.article_text = article_text
    db.session.commit()

    return redirect('/lab8/list')

@lab8.route('/lab8/public_articles')
def public_articles():
    public_articles = articles.query.filter_by(is_public=True).order_by(
        articles.likes.desc(),
        articles.id.asc()
    ).all()

    article_data = [
        {
            'id': article.id,
            'title': article.title,
            'article_text': article.article_text,
            'is_favorite': article.is_favorite,
        }
        for article in public_articles
    ]

    return render_template('lab8/public_articles.html', articles=article_data)



@lab8.route('/lab8/search_articles', methods=['GET'])
@login_required
def search_articles():
    query = request.args.get('query', '').strip()
    search_type = request.args.get('search_type', '')

    if not query:
        return render_template(
            'lab8/public_articles.html',
            articles=[],
            error="Введите строку для поиска"
        )

    articles_query = []
    if search_type == 'own':
        articles_query = articles.query.filter(
            articles.login_id == current_user.id,
            db.or_(
                db.func.concat(' ', articles.title, ' ').ilike(f'% {query} %'),
                db.func.concat(' ', articles.article_text, ' ').ilike(f'% {query} %')
            )
        ).all()

    elif search_type == 'public':
        articles_query = articles.query.filter(
            articles.is_public == True,
            db.or_(
                db.func.concat(' ', articles.title, ' ').ilike(f'% {query} %'),
                db.func.concat(' ', articles.article_text, ' ').ilike(f'% {query} %')
            )
        ).all()

    else:
        return render_template(
            'lab8/public_articles.html',
            articles=[],
            error="Выберите тип поиска"
        )

    if not articles_query:
        return render_template(
            'lab8/public_articles.html',
            articles=[],
            error="Статьи по вашему запросу не найдены"
        )

    return render_template(
        'lab8/public_articles.html',
        articles=articles_query
    )
