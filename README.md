*this repository is archived as this functionality is now in [cellxgene](https://github.com/chanzuckerberg/cellxgene)*

# cellxgene-prepare

CLI for preprocessing data for use with `cellxgene`

## usage

Prepare a dataset `example.h5ad` by calling

```
cellxgene-prepare example.h5ad --engine=scanpy --output=example_processed.h5ad
```

This will save a new file `example_processed.h5ad` with a few new fields prepared designed for use with the specified engine.

Several options are available for specifying preprocessing, generating and saving plots, ensuring data sparsity, and others, to see all options call

```
cellxgene --help
```

```
Options:
  --engine [scanpy]               computational engine  [default: scanpy]
  --format [h5ad|10x_mtx|loom]    data format  [default: h5ad]
  --layout [umap|tsne|umap+tsne]  layout algorithm  [default: umap]
  --recipe [none|seurat|zheng17]  preprocessing receipe to run  [default:
                                  none]
  --output TEXT                   whether or not to save a new file
  --sparse / --no-sparse          whether to require sparsity
  --plotting / --no-plotting      whether or not to generate plots
  --help                          Show this message and exit.
 ```

## development

For development and testing purposes, just install the requirements into your Python environment, and call

```
python prepare/cli.py example.h5ad
```

to simulate launching the CLI
