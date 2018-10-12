import click

from os.path import isfile
from scanpy.api import read_h5ad

settings = dict(help_option_names=['-h', '--help'])

@click.command()
@click.argument('dataset', nargs=1, metavar='<dataset: name of dataset>', required=True)
def cli(dataset):
    """
    Hi! This is a tool for preprocessing data for use with cellxgene.
    """
    print(read_h5ad(dataset))

if __name__ == '__main__':
  cli()