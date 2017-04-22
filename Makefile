VERSION := dev
id := linkatos

image := $(id):$(VERSION)

DOCKER_TASK = docker run --rm -it

build:
	docker build --tag $(image) .
.PHONY: build

install:
	docker run -d -t --name $(id) \
             --env-file $(PWD)/.env \
             $(image)
.PHONY: install

clean:
	docker rm -vf $(id)
.PHONY: clean

logs:
	docker logs -f $(id)
.PHONY: logs


typecheck: FILE_LIST = $(filter-out %/utils.py, $(wildcard linkatos/*.py))
typecheck: EXTRA_FLAGS = $(if $(VERBOSE), --stats)
typecheck:
	@$(DOCKER_TASK) $(image) \
                  mypy --ignore-missing-imports \
                       --follow-imports=skip \
                       $(EXTRA_FLAGS) $(FILE_LIST)
.PHONY: typecheck

lint:
	@$(DOCKER_TASK) $(image) pylint linkatos
.PHONY: lint

test:
ifdef JUNIT
	@$(DOCKER_TASK) $(image) ./test_runner.sh
else
	@$(DOCKER_TASK) $(image) py.test -v tests
endif
.PHONY: test

shell:
	@$(DOCKER_TASK) --env-file $(PWD)/.env \
                  $(image) bash
.PHONY: shell

repl:
	@$(DOCKER_TASK) $(image) python
.PHONY: repl
