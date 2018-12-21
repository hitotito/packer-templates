PACKER_CACHE_DIR=packer_cache

all: clean
	make build $(shell python packer_helper.py list_targets)

# If the first argument is "build"...
ifeq (build,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
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
	@python packer_helper.py template ${BUILD_PARAM} > ${PACKER_CACHE_DIR}/${BUILD_PARAM}.json
	@packer build ${PACKER_CACHE_DIR}/${BUILD_PARAM}.json

_build_help:
		@echo "'build' requires target(s). Please specify target(s)."
		@echo "Avaiable targets:"
		@for t in $(shell python packer_helper.py list_targets) ; do \
			echo $${t} ; \
		done ; \

# TODO - create different config for this, requires template speficiation
dev-raid:  # debian-9-stretch-raid.box
	packer build template_raid.json | tee output

clean:
	@echo Cleaning...
	rm -f *.vmdk
	rm -f output/*

clean-full: clean
	rm -rf packer_cache
