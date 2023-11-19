"""PyGNA2 is based on `PyGNA <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03801-1>`_. It uses the same statistical tests, but improves the way results are reported.

PyGNA is a tool that can perform several kinds of statistical tests on gene networks and gene sets.

* PyGNA Publication: `PyGNA: a unified framework for geneset network analysis <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03801-1>`_
* `PyGNA Documentation <https://pygna.readthedocs.io/en/latest/index.html>`_
* `PyGNA GitHub Repository <https://github.com/stracquadaniolab/pygna>`_
* `PyGNA workflow <https://github.com/stracquadaniolab/workflow-pygna>`_

Hypothesis
----------

I have a gene network, consisting of pairs of co-expressed genes, e.g.:

A --- B

C --- D

Independently, I have single-cell data indicating genes are expressed in
specific cell types:

==== =========
Gene Cell type
==== =========
A    Cortex
B    Cortex
C    Stele
D    Stele
==== =========

Notably, the co-expressed genes share cell types. Is this a significant observation?

*Hypothesis: Pairs of co-expressed genes are more likely to share cell type than random pairs of genes.*

This is a hypothesis about the *topology* of the gene set with respect to the gene network.
"""