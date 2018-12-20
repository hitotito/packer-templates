.PHONY: all clean

PACKER_CACHE_DIR=packer_cache

all: clean dev dev-raid
	packer build template.json | tee output

# TODO, we should use multiple build property of `packer` so that can simple pass in --only option to packer, or build all
debian8.10:
	python generate_template.py debian8.10 > ${PACKER_CACHE_DIR}/debian8.10.json
	packer build ${PACKER_CACHE_DIR}/debian8.10.json

debian9.6:
	python generate_template.py debian9.6 > ${PACKER_CACHE_DIR}/debian9.6.json
	packer build ${PACKER_CACHE_DIR}/debian9.6.json

dev-raid:  # debian-9-stretch-raid.box
	packer build template_raid.json | tee output

clean:
	rm -f *.vmdk
	rm -f output/*

clean-full: clean
	rm -rf packer_cache
