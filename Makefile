NAME = 'dgec test api'
DESCRIPTION = 'Un API creado con Fast API'

shell:
	pipenv shell

install:
	pipenv install

dev:
	uvicorn app.main:app --reload

podman-build:
	podman build -t dgec-test-api .

podman-run:
	podman run -p 8000:8000 dgec-test-api