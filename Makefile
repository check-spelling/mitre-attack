.PHONY: docker

all: clean test build

clean:
	rm -rf dist

docker:
	docker build --tag mitre-attack --file docker/Dockerfile .

update:
	poetry show -o
	poetry update
	poetry export -f requirements.txt -o requirements.txt --without-hashes
	poetry show --tree

 test:
	poetry run coverage run -m pytest

install:
	poetry install

build: test
	poetry build

release: build
	poetry publish
