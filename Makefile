.DEFAULT_GOAL := help

all: help all

.PHONY: all

help: # generate make help
	@grep -E '^[a-zA-Z_-]+:.*?#+.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?#+"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

up: # Spins up local containerized development environment
	docker-compose up -d
	docker exec -it advent-of-code-2021 bash

down: # Spins down local containerized development environment
	docker-compose down
