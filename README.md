# cellxgene-prepare

CLI for preprocessing data for use with `cellxgene`

*under active development*

## usage

Prepare a dataset by calling

```
cellxgene-prepare example.h5ad --engine=scanpy
```

This will save a new file `data-processed.h5ad` with a few new fields prepared designed for use with the specified engine.

Alternatively, calling

```
cellxgene-prepare data.h5ad --engine=scanpy --overwrite
```

Will overwrite the original file, which can be useful when these files are large.

## development

For development and testing purposes, just install the requirements into your Python environment, and call

```
python prepare/cli.py example.h5ad
```

To simulate launching the CLI