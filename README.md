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

## Deploy to VM

```bash
docker build --tag blog_django
docker save blog_django > project.rar
scp -r {project.rar,docker-compose.yml,.config/nginx.conf} $vm_username@$vm_ip:
scp .env.prod $vm_username@$vm_ip:.env # Copy as `.env` so the Compose file reads it.
```

Log into the VM by running: `ssh $vm_username@$vm_ip`.

In the Compose file replace:

- `app.build` with `app.image: blog_django:latest`,
- `.env.prod` with `.env`.

Run `docker compose up` and open a new terminal in the VM.

```bash
docker ps -a # Get app container id.
docker exec -it $id python3 manage.py collectstatic
docker exec -it $id python3 manage.py migrate
docker exec -it $id python3 manage.py createsuperuser
```

Open a browser at `http://$vm_ip:8080`.
