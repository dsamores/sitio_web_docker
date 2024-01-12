build:
	docker-compose build

run:
	docker-compose up

test:
	docker build -t sitio_web_docker_tests .
	docker run sitio_web_docker_tests pytest --cov=app --cov-report term-missing --cov-fail-under=80
