Django-challenge-001
-

Objective:
-
- This project has the objective of improve my abilities using api rest framework

Installation:
-
- Docker
- Docker Compose
- Makefile

Connect DB
- 
- Rename file app/.env_sample to .env, file already have db connection information

run build:
-
- make build
- Install all libs in requirements.txt, upgrade pip and migrate

run server:
-
- make up
- Aggregate the output of each container, creating volumes, images and networks

down server:
-
- make down
- Stop containers and removes containers, networks, volumes and images created by up

run command in container:
-
- make command=""
- 

run all tests:
-
- make test

How to run coverage:
-
- make coverage
- open htmlcov/index.html to see html coverage
- test coverage is a software testing that measures the amount of testing performed by a set of test

Run docker attach:
-
- make attach

Run logs:
-
- make logs


Font:
-
- https://github.com/JungleDevs/django-challenge-001