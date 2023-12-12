NAME = 'test api'
DESCRIPTION = 'Un API creado con Fast API'

shell:
	pipenv shell

install:
	pipenv install

dev:
	uvicorn main:app --reload

