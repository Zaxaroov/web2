from flask import Blueprint, redirect, url_for
from lab2 import lab2
lab1 = Blueprint('lab1',__name__)


@lab1.route("/lab1")
def lab():
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
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
        категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
        сознательно предоставляющих лишь самые базовые возможности.</p>

        <a href="/menu">menu</a>
        
        <h2>Реализованные роуты</h2>
        <div>
            <ol>
                <li>
                    <a href="lab1/oak">Дуб</a>
                </li>
                <li>
                    <a href="lab1/student">Студент</a>
                </li>
                <li>
                    <a href="lab1/python">Python</a>
                </li>
                <li>
                    <a href="lab1/crypto">Криптовалюта</a>
                </li>
            
            </ol>
        </div>
        
        <footer>
            &copy; Захаров Илья, ФБИ-24, 3 курс, 2024 
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='oak.css') + '''">
    <title>Дуб</title>
</head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='student.css') + '''">
    <title>Студент</title>
</head>
<body>
    <h1>Захаров Илья Максимович</h1>
    <img src="''' + url_for('static', filename='ngtu_logo.jpg') + '''" alt="Логотип НГТУ">
</body>
</html>
'''


@lab1.route("/lab1/python")
def python_info():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='python.css') + '''">
    <title>Python</title>
</head>
<body>
    <h1>Язык программирования Python</h1>
    <p>Python — это мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической 
    строгой типизацией и автоматическим управлением памятью. Он ориентирован на повышение производительности 
    разработчика, читаемости кода и качества написанных программ, а также на обеспечение их переносимости. 
    Язык является полностью объектно-ориентированным, что означает, что всё в нём представлено как объекты. 
    Необычной особенностью языка является выделение блоков кода отступами, а минималистичный синтаксис ядра 
    позволяет редко обращаться к документации. Python известен как интерпретируемый язык и часто используется 
    для написания скриптов. Однако его недостатками являются более низкая скорость работы и более высокое 
    потребление памяти по сравнению с аналогичным кодом на компилируемых языках, таких как C или C++.</p>
    
    <p>Python поддерживает множество парадигм программирования, включая императивное, процедурное, структурное 
    и функциональное программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. 
    Аспектно-ориентированное программирование частично поддерживается через декораторы, а более полноценная поддержка 
    обеспечивается дополнительными фреймворками. Методики, такие как контрактное и логическое программирование, можно 
    реализовать с помощью библиотек или расширений. Основные архитектурные черты включают динамическую типизацию, 
    автоматическое управление памятью, полную интроспекцию и механизм обработки исключений. Также поддерживается 
    многопоточность с глобальной блокировкой интерпретатора (GIL) и высокоуровневые структуры данных. Программы могут 
    быть разбиты на модули, которые могут объединяться в пакеты.</p>
    <img src="''' + url_for('static', filename='python.png') + '''" alt="Программирование на Python">
</body>
</html>
'''


@lab1.route("/lab1/crypto")
def mfg():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='crypto.css') + '''">
    <title>Melon Fashion Group</title>
</head>
<body>
    <h1>Криптовалюта</h1>
    <p>Криптовалю́та — разновидность цифровой валюты, учёт внутренних расчётных единиц которой обеспечивает децентрализованная платёжная система
    (нет внутреннего или внешнего администратора или какого-либо его аналога), работающая в полностью автоматическом режиме.
    Сама по себе криптовалюта не имеет какой-либо особой материальной или электронной формы — это просто число, обозначающее количество данных расчётных единиц
    которое записывается в соответствующей позиции информационного пакета протокола передачи данных и зачастую даже не подвергается шифрованию, как и вся иная
    информация о транзакциях между адресами системы.</p>
    <p>Термин криптовалюта закрепился после публикации статьи o системе Биткойн «Crypto currency» (Криптографическая валюта), опубликованной в 2011 году в журнале Forbes.
     При этом и создатель биткойна, и многие другие авторы использовали термин «электронная наличность» (англ. electronic cash).</p>
    <p>Криптографические методы задействованы в механизмах генерации адреса и проверки полномочий на операции с ним (цифровая подпись на основе системы с открытым ключом,
    распоряжение доступно исключительно обладателю соответствующего данному адресу секретного ключа), а также формирование пакета транзакций и его взаимосвязь с другими пакетами
    (последовательное хеширование, которое делает невозможным изменение информации о количестве криптовалюты). При этом в системе нет никакой информации о владельцах адресов или
    о факте создания адреса (адрес можно генерировать полностью автономно, даже не подключаясь к сети и ничего не сообщая в сеть в последующем) — то есть нет механизма убедиться,
    что адрес получателя действительно существует или что ключ доступа к нему не утерян. Отсутствие информации о владельце является основой (но не ограничивается только этим)
    анонимности участников транзакций. По своим экономическим условиям и последствиям платежи криптовалютой более похожи на платежи наличными деньгами, 
    чем на варианты безналичных платежей, хотя криптовалюты разрабатываются в первую очередь для дистанционных покупок (например, через Интернет).</p>
    <img src="''' + url_for('static', filename='crypto.jpg') + '''" alt="Программирование на Python">
</body>
</html>
'''