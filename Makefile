.PHONY: run-dev run-prod freeze-deps install gen-migrations migrate docker-build docker-run docker

DEPS_FILE = requirements.txt
PORT = 5173
CONTAINER_NAME = blog_django

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
	docker build --tag $(CONTAINER_NAME) .

docker-run:
	docker run -p $(PORT):$(PORT) $(CONTAINER_NAME)

docker:
	docker compose up