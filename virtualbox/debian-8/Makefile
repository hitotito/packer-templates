.PHONY: all clean

all: clean
	packer build template.json | tee output

clean:
	rm -f debian-8-jessie.box 
