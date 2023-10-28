# automated-ru-ch-translation-validator
Для запуска приложения требуется установленный Python 3.8 или выше

## Установка виртуального окружения и зависимостей:
* `...\> python -m venv env`
* `...\> env\Scripts\activate`
* `(env) ...\> pip install -r requirements.txt`

## Не забываем провести миграции при первом запуске:
Переходим в папку с проектом:
* `(env) ...\> cd JSTZ`
Проводим миграции:
* `(env) ...\JSTZ> python manage.py makemigrations`
* `(env) ...\JSTZ> python manage.py migrate`
Загружаем стартовые данные в базу данных:
* `(env) ...\JSTZ> python manage.py loaddata dump.json`

## Запуск:
Переходим в папку с проектом:
* `(env) ...\> cd JSTZ`
Запускаем сервер:
* `(env) ...\JSTZ> python manage.py runserver`
* Приложение запускается по адресу `http://127.0.0.1:8000/` (можно открыть в браузере)
