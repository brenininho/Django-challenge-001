coverage:
	docker exec app coverage run manage.py test
	docker exec app coverage report
	docker exec app coverage html

up:
	docker-compose up

down:
	docker-compose down

build:
	docker exec app pip install -r requirements.txt
	docker exec app pip install --upgrade pip
	docker exec app python3 manage.py migrate

test:
	docker exec app python3 manage.py test

logs:
	docker-compose logs -f --tail 100

run:
	docker exec -it app $(command)

attach:
	docker attach app
