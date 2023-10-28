# automated-ru-ch-translation-validator
Для запуска приложения требуется установленный Python 3.8 или выше

## Установка виртуального окружения и зависимостей:
* `...\> python -m venv env`
* `...\> env\Scripts\activate`
* `(env) ...\> pip install -r requirements.txt`

## Не забываем провести миграции при первом запуске:
* `(env) ...\> cd JSTZ`
* `(env) ...\JSTZ> python manage.py makemigrations`
* `(env) ...\JSTZ> python manage.py migrate`
* `(env) ...\JSTZ> python manage.py loaddata dump.json`

## Запуск:
* `(env) ...\> cd JSTZ`
* `(env) ...\JSTZ> python manage.py runserver`
