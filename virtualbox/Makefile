PACKER_CACHE_DIR=packer_cache
PYTHON=python3

all: clean
	make build $(shell $(PYTHON) packer_helper.py list-targets)

# If the first argument is "build"...
ifeq (build,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "build"
  BUILD_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(BUILD_ARGS):;@:)
endif

.PHONY: build
build:
	@if [ "$(BUILD_ARGS)" = "" ] ; then \
		make _build_help ; \
	else \
		for build in $(BUILD_ARGS) ; do \
			make _build_single BUILD_PARAM="$$build" ; \
		done; \
	fi	

_build_single:
	@echo building ${BUILD_PARAM}
	@mkdir -p ${PACKER_CACHE_DIR}
	@$(PYTHON) packer_helper.py template ${BUILD_PARAM} > ${PACKER_CACHE_DIR}/${BUILD_PARAM}.json
	@packer build ${PACKER_CACHE_DIR}/${BUILD_PARAM}.json

_build_help:
		@echo "'build' requires target(s). Please specify target(s)."
		@echo "Avaiable targets:"
		@for t in $(shell $(PYTHON) packer_helper.py list-targets) ; do \
			echo $${t} ; \
		done ; \

clean:
	@echo Cleaning...
	rm -f *.vmdk
	rm -f output/*

clean-full: clean
	rm -rf packer_cache

publish:
	@echo publishing...
	# TODO create publish method
	# Check output directory, and copy it over to target directory.
	# 	0. fetch existing hash file
	# 	1. update checksum hash file for updated images
	# 	2. upload image and new checksum file
	# access to destination should be provided by user
