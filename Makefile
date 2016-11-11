VERSION := dev
id := linkatos

image := $(id):$(VERSION)


build:
	docker build --tag $(image) .
.PHONY: build


# typecheck: FILE_LIST = $(filter-out %/utils.py, $(wildcard listener/**/*.py))
# typecheck: EXTRA_FLAGS = $(if $(VERBOSE), --stats)
# typecheck:
# 	@$(DOCKER_TASK) $(image) mypy --silent-imports $(EXTRA_FLAGS) $(FILE_LIST)
# 	@$(call success,Finished static type checking)
# .PHONY: typecheck

test:
	@docker run --rm -t $(image) py.test -v tests
.PHONY: test

shell:
	@docker run --rm -it $(image) bash
.PHONY: shell

repl:
	@docker run --rm -it $(image) python
.PHONY: repl
