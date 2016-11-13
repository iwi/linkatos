VERSION := dev
id := linkatos

image := $(id):$(VERSION)

DOCKER_TASK = docker run --rm -it

build:
	docker build --tag $(image) .
.PHONY: build

install:
	docker run -d --name $(id) \
             --env SLACK_BOT_TOKEN=$(LINKATOS_SECRET) \
             --env BOT_ID=$(LINKATOS_ID) \
             $(image)
.PHONY: install

clean:
	docker rm -vf $(id)
.PHONY: clean


typecheck: FILE_LIST = $(filter-out %/utils.py, $(wildcard linkatos/*.py))
typecheck: EXTRA_FLAGS = $(if $(VERBOSE), --stats)
typecheck:
	@$(DOCKER_TASK) $(image) mypy --silent-imports $(EXTRA_FLAGS) $(FILE_LIST)
.PHONY: typecheck

test:
	@$(DOCKER_TASK) $(image) py.test -v tests
.PHONY: test

shell:
	@$(DOCKER_TASK) $(image) bash
.PHONY: shell

repl:
	@$(DOCKER_TASK) $(image) python
.PHONY: repl
