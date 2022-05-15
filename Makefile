run:
	pip install -r requirements.txt
	docker-compose up -d
	python3 manage.py migrate
	python3 manage.py runserver

test:
	python3 manage.py test

build:
	python3 manage.py makemigrations
	python3 manage.py migrate

logs:
	docker-compose logs -f --tail 100

coverage:
	coverage run manage.py test
	coverage report
	coverage html

