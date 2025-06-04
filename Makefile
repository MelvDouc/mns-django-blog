.PHONY: dev freeze-deps install gen-migrations migrate

DEPS_FILE = requirements.txt
DEV_PORT = 5173

dev:
	python3 manage.py runserver $(DEV_PORT)

freeze-deps:
	python3 -m pip freeze > $(DEPS_FILE)

install:
	python3 -m pip install -r $(DEPS_FILE)

gen-migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate