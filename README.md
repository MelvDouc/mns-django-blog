# Django blog

## Create main app (sub-project)

```bash
django-admin startproject $main_app $location
```

## Create app

```bash
python3 manage.py startapp $app
```

Declare it in $main_app/settings.py:

```python
INSTALLED_APPS = [
  # ...,
  "$app"
]
```

## Migrations

Generate:

```bash
python3 manage.py makemigrations
```

Apply:

```bash
python3 manage.py migrate
```

## Create admin

Run initial migration first.

```bash
python3 manage.py createsuperuser
```
