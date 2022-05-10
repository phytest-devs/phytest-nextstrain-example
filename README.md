# Nextstrain build for Zika virus tutorial

This repository provides the data and scripts associated with the [Zika virus tutorial](https://nextstrain.org/docs/getting-started/zika-tutorial).

See the [original Zika build repository](https://github.com/nextstrain/zika) for more about the public build.


# Usage 

Create a conda environment named `nextstrain` and install all the necessary software using mamba:

```
mamba create -n nextstrain \
  -c conda-forge -c bioconda \
  nextstrain-cli augur auspice nextalign snakemake git \
  --yes
```

Activate the conda environment:

```
conda activate nextstrain
```

Add the `phytest` dependency.

```
# pip install git+https://github.com/phytest-devs/phytest.git
pip install phytest
```

Run the pipeline 

```
snakemake -c 1 
```