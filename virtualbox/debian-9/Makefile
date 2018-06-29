.PHONY: all clean

all: clean dev dev-raid
	packer build template.json | tee output

dev:  # debian-9-stretch.box
	packer build template.json | tee output

dev-raid:  # debian-9-stretch-raid.box
	packer build template_raid.json | tee output

clean:
	rm -f *.vmdk
	rm -f debian-9-stretch*.box

clean-full: clean
	rm -rf packer_cache
