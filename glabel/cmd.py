import click
import configparser
import sys

from .glabel import Glabel

def get_credentials(file):
    """ Derives credentials form an auth file
        :param: a config file with auth keys
        :return: config list with twitter credentials
    """
    lbl.read()
    config = configparser.ConfigParser()
    config.read(file)
    return config['github']['token']

@click.command()
@click.option('--config_file', default='./config.cfg',
                help='A path to a configuration file.',
                type=click.Path(exists=True))
@click.option('--state', default='open',
                help='Filter pulls by state. [default: open]')
@click.option('--base', help='Filter pulls by base (PR target) branch name.')

def run(config_file):
    """ Run terminal labeler """
    token = get_credentials(config_file)
    lbl = Glabel(token)
    lbl.read()
