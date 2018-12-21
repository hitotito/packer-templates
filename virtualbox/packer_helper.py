import click
import sys
import yaml
from jinja2 import Template

UNBUILDABLE_TARGET = ['global']
PACKER_VARIABLES = {
    "packer_name": "{{ .Name }}",
    "packer_path": "{{ .Path }}",
    "packer_http_ip": "{{ .HTTPIP }}",
    "packer_http_port": "{{ .HTTPPort }}",
}

TEMPLATE_FILE = "template.json.j2"
CONFIG_FILE = "config.yml"

ERROR_SUCCESS = 0
ERROR_NO_TARGET = 1
ERROR_INVALID_TARGET = 2

def get_config():
    return yaml.load(open(CONFIG_FILE, 'r').read())

def get_buildable_targets(config):
    return [key for key in config.keys() if key not in UNBUILDABLE_TARGET]

def get_variables(config, target):
    """
    Get global variables and we will extend target variables on top of it
    """
    return dict(config.get('global',{}), **config.get(target, {}))

# cli interfaces
@click.group()
def entry_point():
    pass

@entry_point.command()
def list_targets():
    config = get_config()
    print (" ".join(sorted(get_buildable_targets(config))))

@entry_point.command()
@click.argument('target', required=True, nargs=1)
def template(target):
    """
    """
    # Check if specified target is in configuration
    config = yaml.load(open(CONFIG_FILE, 'r').read())
    available_targets = get_buildable_targets(config)
    if not target in available_targets:
        print ("Error: target [{}] is not available. Please specify a valid target.".format(target), file=sys.stderr)
        print ("  Available targets:\n\t{}".format("\n\t".join(sorted(available_targets))), file=sys.stderr)
        sys.exit(ERROR_INVALID_TARGET)

    variables = get_variables(config, target)
    build_template = Template(open(TEMPLATE_FILE, 'r').read())
    print (build_template.render({**variables, **PACKER_VARIABLES}))
    sys.exit(ERROR_SUCCESS)

if __name__ == '__main__':
    entry_point()
