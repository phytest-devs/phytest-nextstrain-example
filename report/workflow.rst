=====================
Nextstrain + Phytest
=====================

This workflow provides an example of using `phytest <https://github.com/phytest-devs/phytest>`_ for quality control in a Snakemake pipeline. 
Phytest allows us to write tests for our pipeline the same way we write test for our code. 
This repo builds on the data and scripts associated with the `Zika virus tutorial <https://nextstrain.org/docs/getting-started/zika-tutorial>`_. 
We add phytest to the pipeline to ensure our alignment and maximum likelihood tree meet our explicit requirements before proceeding though the pipeline.
