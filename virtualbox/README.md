Packer
-
This repository contains all configuration, templates, and scripts to build base images for various distribution of linux on various platforms.

Supported platform
-
- Digital Ocean (WIP)
- Virtualbox

Supported operating system
-
- Centos (WIP)
- Debian

How to build
-
####Build all
To make all available builds (all platform, all OS) run following command:

```
make
```

####Build specific build
To build specific operating system:

```
make build debian9.6
```

####Show all build options
To display all build options:

```
make build
```




