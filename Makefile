.PHONY: freeze-deps

DEPS_FILE + requirements.txt

freeze-deps:
	python3 -m pip freeze > $(DEPS_FILE)

install:
	python3 -m pip -r $(DEPS_FILE)