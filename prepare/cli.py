import click

from os.path import isfile

settings = dict(help_option_names=['-h', '--help'])

@click.command()
@click.argument('dataset', nargs=1, metavar='<dataset: name of dataset>', required=True)
@click.option('--engine', default='scanpy', type=click.Choice(['scanpy']), help='computational engine', show_default=True)
@click.option('--format', default='h5ad', type=click.Choice(['h5ad', '10x_mtx', 'loom']), help='data format', show_default=True)
@click.option('--layout', default='umap', type=click.Choice(['umap', 'tsne', 'umap+tsne']), help='layout algorithm', show_default=True)
@click.option('--recipe', default='none', type=click.Choice(['none', 'seurat', 'zheng17']), help='preprocessing receipe to run', show_default=True)
@click.option('--output', default='', help='whether or not to save a new file')
@click.option('--sparse/--no-sparse', default=False, help='whether to require sparsity')
@click.option('--plotting/--no-plotting', default=False, help='whether or not to generate plots')
def cli(dataset, engine, format, layout, recipe, output, sparse, plotting):
    """
    Hi! This is a tool for preprocessing data for use with cellxgene.
    """
    import matplotlib
    matplotlib.use('Agg')
    import scanpy.api as sc
    import pandas as pd
    import numpy as np

    # scanpy settings 
    sc.settings.verbosity = 2
    sc.settings.autosave = True

    # data loading
    adata = None

    if format == 'h5ad':
        adata = sc.read_h5ad(dataset)
    if format == '10x_mtx':
        adata = sc.read_10x_mtx(dataset)

    adata.var_names_make_unique()

    # run a recipe if requested
    if recipe == 'seurat':
        sc.pp.recipe_seurat(adata)
    elif recipe == 'zheng17':
        sc.pp.recipe_zheng17(adata)
    else:
        sc.pp.filter_cells(adata, min_genes=5)
        sc.pp.filter_genes(adata, min_cells=25)
        if sparse:
            sc.pp.scale(adata, zero_center=False)
        else:
            sc.pp.scale(adata)

    # dimensionality reduction
    if sparse:
        sc.pp.pca(adata, svd_solver='arpack', zero_center=False)
    else:
        sc.pp.pca(adata, svd_solver='arpack')

    # neighbors and clustering
    sc.pp.neighbors(adata)
    sc.tl.louvain(adata)

    # layout and plotting
    if len(np.unique(adata.obs['louvain'].values)) < 10:
        palette = 'tab10'
    else:
        palette = 'tab20'

    if layout == 'umap' or layout == 'umap+tsne':
        sc.tl.umap(adata)
        if plotting:
            sc.pl.umap(adata, color='louvain', palette=palette, save='_louvain')

    if layout == 'tsne' or layout == 'umap+tsne':
        sc.tl.tsne(adata)
        if plotting:
            sc.pl.tsne(adata, color='louvain', palette=palette, save='_louvain')    

    # show the structure
    print('data structure...')
    print(adata)

    # saving file
    if not output == '':
        print('saving output...')
        adata.write(output)

if __name__ == '__main__':
  cli()