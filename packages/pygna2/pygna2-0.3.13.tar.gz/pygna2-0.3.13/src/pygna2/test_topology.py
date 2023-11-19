import pandas as pd
import networkx as nx
import logging
from math import log10, floor
from statistics import mean, variance
from multiprocessing import Pool
from functools import partial
import pygna.statistical_test as st
from pygna.command import read_distance_matrix

from pygna2.parse_network_genesets import parse_network_and_genesets
from pygna2.test_plot import plot_test_results

TABLE_HEADER = ("analysis,setname,n_mapped,n_geneset,number_of_permutations,observed,empirical_pvalue,mean(null),"
                      "var(null),network,geneset\n")

def run_test(st_test, genes, permutations: int = 200, cores: int = 1):
    (observed, pvalue, null_d, n_mapped, n_geneset) = st_test.empirical_pvalue(
        genes, max_iter=permutations, alternative="greater", cores=cores
    )
    return observed, abs(int(observed<mean(null_d)) - pvalue/2), null_d


def rw_dict(rwr_matrix, in_memory=False):
    if rwr_matrix:
        return dict(zip(('nodes', 'matrix'),
            read_distance_matrix(rwr_matrix, in_memory=in_memory)))


def run_test_on_geneset(st_test, setname, genes, permutations: int = 200,
                        processes: int = 1, verbose=False):
    if verbose:
        logging.info(f'Running test on {setname}')
    (observed, pvalue, null_d) = run_test(st_test, genes,
        permutations=permutations, cores=processes)
    if verbose:
        logging.info(f'Observed value: {observed}, P-value: {pvalue}')
    return setname, observed, pvalue, null_d


def test_topology(network: str, genesets: str, output: str, rwr_matrix=None,
                  stat=st.geneset_internal_degree_statistic,
                  stat_name='topology_internal_degree',
                  setnames=None, max_components=None,
                  min_component_size: int = 2,
                  min_set_size: int = 20, results_figure=None,
                  results_figure_type: str = 'box',
                  results_figure_significance: bool = False,
                  results_figure_x_label: str = 'Topology Internal Degree (%)',
                  width: float = 7, height: float = 7,
                  null_distributions=None,
                  filtered_network_file=None,
                  degree_correction_bins=1,
                  rwr_matrix_in_memory=False,
                  permutations: int = 200, processes: int = 1):
    network, genesets = parse_network_and_genesets(network, genesets=genesets,
        setnames=setnames, max_components=max_components,
        min_component_size=min_component_size, min_set_size=min_set_size)
    st_test = st.StatisticalTest(stat, network,
        degree_bins=degree_correction_bins,
        diz=rw_dict(rwr_matrix, in_memory=rwr_matrix_in_memory)
                    if rwr_matrix else {})
    results = tuple(run_test_on_geneset(st_test, setname, genes,
                                        permutations=permutations,
                                        processes=processes, verbose=True)
                    for setname, genes in genesets.items())
    pd.DataFrame(
        ((stat_name, setname, permutations, observed, pvalue, mean(null_d),
          variance(null_d))
         if len(set(null_d))>1 else (stat_name, setname, permutations,
                                     observed, pvalue, mean(null_d),
                                     0)
         for setname, observed, pvalue, null_d in results
        ),
         columns=('Analysis', 'Gene set', 'Permutations', 'Observed',
                  'P-value', 'Null mean', 'Null variance')
    ).to_csv(output, index=False, sep='\t' if output.endswith('.tsv') else ',')
    null_dists = pd.DataFrame(
        ((setname, val) for setname, _, _, null_d in results for val in null_d),
        columns=('Gene set', 'Null distribution')
    )
    observed = pd.DataFrame(
        ((setname, observed, '*'*min(3, floor(-1*log10(2*pvalue))))
         for setname, observed, pvalue, _ in results),
        columns=('Gene set', 'Observed', 'Significance')
    )
    if results_figure:
        plot_test_results(null_dists, observed, results_figure,
                          figure_type=results_figure_type,
                          significance=results_figure_significance,
                          width=width, height=height,
                          strip_alpha=min(1, 32/permutations),
                          x_label=results_figure_x_label)
    if null_distributions:
        null_dists.to_csv(null_distributions, index=False,
                          sep='\t' if null_distributions.endswith('.tsv')
                          else ',')
    if filtered_network_file:
        nx.to_pandas_edgelist(network).to_csv(filtered_network_file,
            sep='\t', header=False, index=False)
