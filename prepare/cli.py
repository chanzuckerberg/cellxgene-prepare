import click

from os.path import isfile
from scanpy.api import read_h5ad

settings = dict(help_option_names=['-h', '--help'])

@click.command()
@click.argument('dataset', nargs=1, metavar='<dataset: name of dataset>', required=True)
@click.option('--overwrite/--no-overwrite', default=True, help='whether or not to overwrite file')
def cli(dataset, overwrite):
    """
    Hi! This is a tool for preprocessing data for use with cellxgene.
    """
    print(read_h5ad(dataset))

    # here's where the business logic will go

    # load the dataset

    # perform any precomputation

    # save results or overwrite

if __name__ == '__main__':
  cli()