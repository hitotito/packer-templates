import click
import sys
import yaml
from jinja2 import Template

PACKER_VARIABLES = {
    "packer_name": "{{ .Name }}",
    "packer_path": "{{ .Path }}",
    "packer_http_ip": "{{ .HTTPIP }}",
    "packer_http_port": "{{ .HTTPPort }}",
}

TEMPLATE_FILE = "template.json.j2"
CONFIG_FILE = "config.yml"

def get_variables(target):
    """
    Get global variables and we will extend target variables on top of it
    """
    variables_file_content = open(CONFIG_FILE, 'r').read()
    config = yaml.load(variables_file_content)
    return dict(config.get('global',{}), **config.get(target, {}))

@click.command()
@click.argument('target', required=True, nargs=1)
def generate_build_template(target):
    base_template = open(TEMPLATE_FILE, 'r').read()
    build_template = Template(base_template)
    variables = get_variables(target)
    print (build_template.render({**variables, **PACKER_VARIABLES}))

if __name__ == '__main__':
    generate_build_template()
