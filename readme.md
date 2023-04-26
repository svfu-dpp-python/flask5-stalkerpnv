# Flask-5

## Предварительные шаги

1. Откройте каталог проекта в редакторе VS Code

1. Создайте и активируйте виртуальное окружение 

Powershell:

```powershell
py -m venv venv
.\venv\scripts\activate.ps1
```

Командная строка:

```cmd
py -m venv venv
venv\scripts\activate.bat
```

2. Установите библиотеки используя список из `requirements.txt`:

```powershell
pip install -r requirements.txt
```

3. Инициализируйте базу данных:

```powershell
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4. Разрешите отладку и запустите веб-сервер разработчика:

Powershell:

```powershell
$ENV:FLASK_DEBUG=1
flask run
```

Командная строка:

```cmd
set FLASK_DEBUG=1
flask run
```

## Добавление комментариев

1. Добавьте модель для хранения комментариев к постам в файл `models.py` и выполните реструктуризацию данных в БД

1. Создайте форму для добавления комментариев в файл `forms.py`

1. Исправьте шаблон для просмотра постов так чтобы были видны комментарии к ним

1. Добавьте код во `views.py` для добавления нового комментария в базу данных (смотрите пример в документации Flask-SqlAlchemy)

1. Проверьте работу

1. Сделайте коммит

## Публикация на хостинге

1. Добавьте файл для интеграции с веб-сервером на хостинге `flask_app.py`:

```python
from blog import create_app

app = create_app()
```

2. Отправьте изменения на центральный сервер

```powershell
git push
```

3. Зарегистрируйте бесплатный аккаунт на сайте [PythonAnywhere](https://www.pythonanywhere.com) и войдите на сайт

1. В разделе `Consoles` откройте консоль `Bash`

1. Склонируйте репозиторий

```bash
git clone <URL репозитория>
```

6. Откройте раздел `Web` и запустите мастер публикации веб-приложения с помощью кнопки `Add a new web app`.

   * используйте бесплатно предоставляемое доменное имя и нажмите `Next`
   * выберите фреймворк `Flask`
   * выберите наиболее актуальную версию Python: `Python 3.10`
   * исправьте путь к файлу интеграции с веб-сервером хостинга (нужно вписать правильное название каталога с приложением):

```
/home/<имя пользователя>/<каталог с приложением>/flask_app.py
```

   * нажмите кнопку `Next` и дождитесь завершения процесса публикации
   * откройте гиперссылку с адресом вида `<имя пользователя>.pythonanywhere.com`

   При необходимости вы можете удалить публикацию веб-приложения и повторить её снова.

7. Проверьте работу сайта в браузере и сделайте скриншот сайта так, чтобы была видна адресная строка

1. Добавьте скриншот в каталог проекта, добавьте его к файлам приложения и сделайте коммит

## Ссылки

* [Документация Flask](https://flask.palletsprojects.com/)
* [Документация Flask-WTF](https://flask-wtf.readthedocs.io/)
* [Документация Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [Документация Flask-Migrate](https://flask.palletsprojects.com/)
* [Документация Flask-Admin](https://flask-admin.readthedocs.io/)
* [Документация WTForms](https://wtforms.readthedocs.io/)
* [Документация SqlAlchemy](https://www.sqlalchemy.org/)
* [Документация Alembic](https://alembic.sqlalchemy.org/)
