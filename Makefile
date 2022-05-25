coverage:
	coverage run manage.py test
	coverage report
	coverage html

up:
	docker-compose up

down:
	docker-compose down

build:
	docker exec db pip install -r requirements.txt
	docker exec db pip install --upgrade pip
	docker exec db python3 manage.py migrate

test:
	docker exec db python3 manage.py test

logs:
	docker-compose logs -f --tail 100

run:
	docker exec -it db $(command)

attach:
	docker attach db
