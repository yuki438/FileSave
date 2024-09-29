# ☁ Pet-проект для онлайн хранения файлов

# 🔨 Стек
- Python 3.11
- Django 5.0
- Django REST framework (Simple JWT)

# 🔧 Установка

### 1. Скопировать репозиторий

Windows/Unix/macOS:

```bash
git clone https://github.com/yuki438/FileSave.git
cd FileSave
```

### 2. Создать и активировать .venv

Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Unix/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Создать config.env и задать SECRET_KEY

Windows:

```bash
py -c "from django.core.management.utils import get_random_secret_key as g; open('config.env', 'w').write(f'SECRET_KEY={g()}')"
```

Unix/macOS:

```bash
python3 -c "import os; from django.core.management.utils import get_random_secret_key as g; open('config.env','w').write(f'SECRET_KEY={g()}')"
```

### 4. Создать миграции и запустить сервер

Windows:

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

Unix/macOS:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```