.PHONY: run-dev run freeze-deps install gen-migrations migrate docker-build docker-run docker-save docker-compose

DEPS_FILE = requirements.txt
PORT = 8000
TAG = blog_django

run-dev:
	python3 manage.py runserver 0.0.0.0:$(PORT)

run:
	gunicorn blog.wsgi:application --bind 0.0.0.0:$(PORT)

freeze-deps:
	python3 -m pip freeze > $(DEPS_FILE)

install:
	python3 -m pip install -r $(DEPS_FILE)

gen-migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

docker-build:
	docker build --tag $(TAG) .

docker-run:
	docker run -p $(PORT):$(PORT) $(TAG)

docker-save:
	docker save $(TAG) > project.rar

docker-compose:
	docker compose up --build
