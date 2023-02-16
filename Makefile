install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black project2/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py project2/*.py

all: install format lint