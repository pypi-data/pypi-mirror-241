
# PyGNA2

PyGNA2 is based on [PyGNA](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03801-1). It uses the same statistical tests, but improves the way results are reported.

PyGNA is a tool that can perform several kinds of statistical tests on gene networks and gene sets.

- PyGNA Publication: [PyGNA: a unified framework for geneset network analysis](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03801-1)
- [PyGNA Documentation](https://pygna.readthedocs.io/en/latest/index.html)
- [PyGNA GitHub Repository](https://github.com/stracquadaniolab/pygna)
- [PyGNA workflow](https://github.com/stracquadaniolab/workflow-pygna)

See also:
- https://www.nature.com/articles/s41598-023-28593-1
- https://academic.oup.com/insilicoplants/article/2/1/diaa002/5763089
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6747016/

See also with gwas:
- https://www.nature.com/articles/s41598-021-03864-x
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5571659/
- https://bmcplantbiol.biomedcentral.com/articles/10.1186/s12870-021-03268-z

## Hypothesis

I have a gene network, consisting of pairs of co-expressed genes, e.g.:

A --- B

C --- D

Independently, I have single-cell data indicating genes are expressed in
specific cell types:

| Gene | Cell type |
| ---- | --------- |
| A    | Cortex    |
| B    | Cortex    |
| C    | Stele     |
| D    | Stele     |

Notably, the co-expressed genes share cell types. Is this a significant observation?

*Hypothesis: Pairs of co-expressed genes are more likely to share cell type than random pairs of genes.*

This is a hypothesis about the *topology* of the gene set with respect to the gene network.

## Network analysis

### Input files

1. Network file `network.tsv`, a tab-delimited file with two columns. Each row is a pair of co-expressed genes. For example:

```
Glyma.01G075300	Glyma.01G068000
Glyma.01G076100	Glyma.01G074800
Glyma.02G148200	Glyma.02G024200
Glyma.02G148500	Glyma.01G163500
Glyma.02G149600	Glyma.02G024200
Glyma.02G149600	Glyma.02G148200
...
```

> **Note:** The input file can contain additional columns (such as a Cytoscape edges file), but they will be ignored.

2. Gene set file `genesets.gmt`, a tab-delimited file with one row per gene set. Each row is a gene set name, followed by a description, followed by a tab-separated list of genes. This format is called GMT for "Gene Matrix Transposed". For example:

```
cortex	"genes expressed in cortex"	Glyma.01G075300	Glyma.09G115800	Glyma.12G116800	...
stele	"genes expressed in stele"	Glyma.01G075300	Glyma.09G115800	Glyma.12G116800	...
```

### Install PyGNA2

We can create and activate a conda environment with pygna by:

```sh
conda create -n pygna2 -c stracquadaniolab -c bioconda -c conda-forge pygna \
  "numpy<1.20"
conda activate pygna2
```

Then install `pygna2` with pip

```sh
pip install pygna2
```

Check that the installation was successful by running one of:

```sh
pygna2 --version
pygna2 --help
pygna2
```


### Summarize and filter networks

#### Summarize

Generate a summary of the network:
```sh
pygna2 network summary network.tsv network.tsv summary.txt
```

Usually, you should also plot the component size and degree distributions when summarizing:
```sh
pygna2 network summary network.tsv network.tsv summary.txt \
  --plot-component component-dist.pdf --plot-degree degree-dist.pdf
```

#### Filter

Filter a network to the 10 largest connected components
```sh
pygna2 network filter network.tsv filtered.tsv --max-components 10
```

Filter out components with fewer than 10 genes
```sh
pygna2 network filter network.tsv filtered.tsv --min-component-size 10
```

Filter out components that don't overlap any gene set
```sh
pygna2 network filter network.tsv filtered.tsv --genesets genesets.gmt
```

Filter to a minimal network that includes only genes that are in a gene set
or are part of a shortest path between set members.
```sh
pygna2 network filter network.tsv filtered.tsv --genesets genesets.gmt --minimal
```

Filter out all genes that are not in a gene set
```sh
pygna2 network filter network.tsv filtered.tsv --genesets genesets.gmt --strict
```

#### Visualize

Generate a GraphML file that can be visualized with E.G. cytoscape
```sh
pygna2 network cytoscape network.tsv network-x-genesets.graphml \
  --genesets genesets.gmt
```

By default, the graph will be filtered to include only components that overlap the gene sets. To visualize the entire graph without filtering, use the `--full` option
```sh
pygna2 network cytoscape network.tsv network-x-genesets.graphml \
  --genesets genesets.gmt --full
```

With the `--full` option, gene sets are not strictly required.
```sh
pygna2 network cytoscape network.tsv network.graphml --full
```

Optionally you may write a GMT file containing connected components
```sh
pygna2 network cytoscape network.tsv network-x-genesets.graphml \
  --genesets genesets.gmt --components-out network-x-genesets.gmt
```

### Perform topology and association tests

The tests in PyGNA2 are divided into two groups: topology tests, which test for topological significance of a single gene set, or association tests, which test for significant association between two gene sets. They include:

**Pygna2 hypothesis tests**

| Topology | Association |
| -------- | ----------- |
| Total Degree | Association Random Walk with Restart |
| Internal Degree | |
| Module | |
| Topological Random Walk with Restart |


The Random Walk with Restart tests require pre-computing an adjacency matrix. The matrix can be generated by:

```sh
pygna2 build network.tsv network-rwr.hdf5
```

#### Total Degree test

```sh
pygna2 test ttd network.tsv genesets.gmt topology_total_degree.csv
```

The Topology Total Degree statistic (TTD) is the average degree (number of edges) of genes in the gene set. The Total Degree test tests whether or not the TTD of the gene set is higher than the TTD of the entire network.

From the PyGNA paper:

> While TTD could be helpful to have an idea of how relevant and well characterized the nodes in the geneset are, we do not expect this statistic to be informative on the strength of interaction withing a geneset.

#### Internal Degree test

```sh
pygna2 test tid network.tsv genesets.gmt topology_internal_degree.csv
```

An *internal edge* of a gene in the gene set is an edge that connects it to another gene in the same gene set.

The *internal degree* of a gene is its number of internal edges.

The *internal fraction* of a gene is its internal degree divided by its degree. (a value between 0 and 1)

The Topology Internal Degree statistic (TID) is the average internal fraction of genes in the gene set (between 0 and 1). The Internal Degree test tests whether or not the TID of the gene set is higher than the TID of the entire network. In principle, highly connected gene sets should have TID close to 1.

From the PyGNA paper:

> In practice, the internal degree statistic captures the amount of direct interactions between genes in a geneset, and thus a geneset showing a network effect should have TTD values close to 1. However, the main limitation of this model lies in the fact that it only captures direct interactions, whereas biological networks are usually characterized by medium and long range interactions.

#### Module test

```sh
pygna2 test tm network.tsv genesets.gmt topology_module.csv
```

The gene network is made up of [*components*](https://en.wikipedia.org/wiki/Component_(graph_theory)). Two genes are in the same component if there is a path along edges connecting them. Two genes in different components do not have a path between them. The size of a component is the number of genes it contains. In the context of gene networks, components may be called modules.

As a subset of the network, the gene set also has components/modules. A highly connected gene set will have a few large components, while a disconnected gene set will have many small components. The Topology Module statistic (TM) is the size of the largest component in the gene set. The Module test tests whether TM of the gene set is larger than expected by chance.

#### Topological Random Walk with Restart test

```sh
pygna2 test trwr network.tsv genesets.gmt topology_rwr.csv network-rwr.hdf5
```

From the PyGNA paper:

> modelling gene interactions using shortest path provides a simple analytical framework to include local and global awareness of the connectivity. However, this approach is also sensitive to missing links and small-world effects, which is common in biological networks and could lead to false positives [19]. Propagation models provide an analytical model to overcome these limitations, and have been shown to be robust for biological network analysis [20]. While its interpretation is not necessarily straightforward, the RWR model is more robust than the shortest path model, because it effectively adjusts interaction effects for network structure; it rewards nodes connected with many shortest paths, and penalizes those that are connected only by path going through high degree nodes.


#### Association Random Walk with Restart test

The association RWR test can be run with one or two gene set files. If just one file is supplied, all pairs in the given gene set will be tested. If a second gene set file is supplied with the `--genesets-b` option, all sets in the first file (file A) will be tested against all sets in the second file (file B).

```sh
pygna2 test arwr network.tsv genesets.gmt all-x-all-rwr.csv network-rwr.hdf5 \
pygna2 test arwr network.tsv genesets.gmt a-x-b-rwr.csv network-rwr.hdf5 \
  --genesets-b genesets-b.gmt
```

### Plot results

To generate a plot from a results table, use `pygna2 plot`. Usually this
requires that you write null distributions when running the tests. For example:

```sh
pygna2 test tid network.tsv genesets.gmt results.tsv \
  --null-distributions null.tsv
pygna2 plot results.tsv output.pdf --null-distributions null.tsv
```
