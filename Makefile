NAME = 'test api'
DESCRIPTION = 'Un API creado con Fast API'

install:
		pipenv install

run:
		uvicorn main:app --reload

