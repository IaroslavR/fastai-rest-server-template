PROJ_ROOT = $(shell pwd)

freeze:
	 conda env export | grep -v "^prefix: " > environment.yml

new:
	conda env create -f ${PROJ_ROOT}/environment.yml

test:
	@echo ${PROJ_ROOT}

.PONY: freeze env test
