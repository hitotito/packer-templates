import click
import json
import sys
import textwrap
import yaml
from jinja2 import Template

UNBUILDABLE_TARGET = ['global']
PACKER_VARIABLES = {
    "packer_name": "{{ .Name }}",
    "packer_path": "{{ .Path }}",
    "packer_http_ip": "{{ .HTTPIP }}",
    "packer_http_port": "{{ .HTTPPort }}",
    "packer_virtualbox_version": "{{ .Version }}",
}

DEFAULT_CONFIG_FILE = "config.yml"

ERROR_SUCCESS = 0
ERROR_NO_TARGET = 1
ERROR_INVALID_TARGET = 2

class ConfigException(Exception):
    pass

def check_target(config, target):
    available_targets = get_buildable_targets(config)
    if not target in available_targets:
        msg = textwrap.dedent("""
        Error: target [{target}] is not available. Please specify a valid target.
        Available targets:
        {targets_list}
        """.format(
            target=target,
            targets_list="\t".join(sorted(available_targets)),
        ))
        raise ConfigException(msg)

def get_config(config_file_path):
    return yaml.load(open(config_file_path, 'r').read(), Loader=yaml.FullLoader)

def get_buildable_targets(config):
    return [key for key in config.keys() if key not in UNBUILDABLE_TARGET]

def get_variables(config, target):
    """
    Method that will compute target variables from config.
    A few important mentions:
    `global` key will always be applied
    `_inherit` key can be used to create inheritance. If same key exists,
    higher level variables will override variables.
    """
    target_config = config.get(target, {})
    base_config = target_config.pop('_inherit', None)
    if base_config:
        return dict(get_variables(config, base_config), **target_config)
    return dict(config.get('global',{}), **target_config)

# cli interfaces
@click.group()
def entry_point():
    pass

@entry_point.command()
@click.option('-c', '--config', 'config_path', default=DEFAULT_CONFIG_FILE, help="configuration file path")
def list_targets(config_path):
    config = get_config(config_path)
    print (" ".join(sorted(get_buildable_targets(config))))

@entry_point.command()
@click.argument('target', required=True, nargs=1)
@click.option('-c', '--config', 'config_path', default=DEFAULT_CONFIG_FILE, help="configuration file path")
def template(target, config_path):
    """
    """
    # Check if specified target is in configuration
    try:
        config = get_config(config_path)
        check_target(config, target)
    except ConfigException as e:
        print (str(e), file=sys.stderr)
        sys.exit(ERROR_NO_TARGET)

    variables = get_variables(config, target)
    build_template = Template(open(variables.get('template'), 'r').read())
    print (build_template.render({**variables, **PACKER_VARIABLES}))
    sys.exit(ERROR_SUCCESS)

@entry_point.command()
@click.argument('target', required=True, nargs=1)
@click.option('-c', '--config', 'config_path', default=DEFAULT_CONFIG_FILE, help="configuration file path")
def variables(target, config_path):
    """
    """
    # Check if specified target is in configuration
    try:
        config = get_config(config_path)
        check_target(config, target)
    except ConfigException as e:
        print (str(e), file=sys.stderr)
        sys.exit(ERROR_NO_TARGET)

    variables = get_variables(config, target)
    print (json.dumps(variables))
    sys.exit(ERROR_SUCCESS)

if __name__ == '__main__':
    entry_point()
