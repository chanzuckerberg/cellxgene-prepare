# cellxgene-prepare

CLI for preprocessing data for use with `cellxgene`

*under active development*

## usage

Prepare a dataset `example.h5ad` by calling

```
cellxgene-prepare example.h5ad --engine=scanpy --output=example_processed.h5ad
```

This will save a new file `example_processed.h5ad` with a few new fields prepared designed for use with the specified engine.

Several options are available for specifying preprocessing, generating and saving plots, ensuring data sparsity, and others. To see all options, type

```
cellxgene --help
```

## development

For development and testing purposes, just install the requirements into your Python environment, and call

```
python prepare/cli.py example.h5ad
```

to simulate launching the CLI