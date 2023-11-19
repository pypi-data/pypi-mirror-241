import pandas as pd
import networkx as nx
import logging
from math import log10, floor, ceil
from statistics import mean, variance, stdev
from itertools import combinations, product
from multiprocessing import Pool
from functools import partial
import pygna.statistical_comparison as sc
from pygna2.parse_network_genesets import parse_network, parse_genesets
from pygna2.test_topology import rw_dict
from pygna2.test_plot import (plot_test_results, plot_test_clustermap,
                              plot_test_heatmap)

def run_comparison(sc_comparison, genes_a, genes_b, permutations: int = 200, cores: int = 1):
    (observed, pvalue, null_d, a_mapped, b_mapped) = sc_comparison.comparison_empirical_pvalue(
        genes_a, genes_b, max_iter=permutations, alternative="greater", keep=True
    )
    return observed, abs(int(observed<mean(null_d)) - pvalue/2), null_d


def run_comparison_on_genesets(sc_comparison, setname_a, genes_a, setname_b, genes_b,
                                permutations: int = 200,
                                processes: int = 1, verbose=False):
    if verbose:
        logging.info(f'Running test on {setname_a} vs {setname_b}')
    (observed, pvalue, null_d) = run_comparison(sc_comparison, genes_a, genes_b,
        permutations=permutations, cores=processes)
    if verbose:
        logging.info(f'Observed value: {observed}, P-value: {pvalue}')
    return setname_a, setname_b, observed, pvalue, null_d


def test_association(network: str, genesets_a: str, output: str,
                     rwr_matrix: str, genesets_b=None,
                     setnames_a=None, setnames_b=None, max_components=None,
                     min_component_size: int = 2,
                     min_set_size: int = 20, results_figure=None,
                     results_figure_type: str = 'box',
                     results_figure_significance: bool = False,
                     results_figure_rotate_xtick: int = 0,
                     results_figure_box_width: float = .3,
                     width: float = 7, height: float = 7,
                     null_distributions=None,
                     filtered_network_file=None,
                     degree_correction_bins=1,
                     rwr_matrix_in_memory=False,
                     permutations: int = 100, processes: int = 1):
    network  = parse_network(network, max_components=max_components,
        min_component_size=min_component_size)
    genesets_a = parse_genesets(genesets_a, setnames=setnames_a,
                                min_set_size=min_set_size)
    if genesets_b:
        genesets_b = parse_genesets(genesets_b, setnames=setnames_b,
                                    min_set_size=min_set_size)
    sc_comparison = sc.StatisticalComparison(sc.comparison_random_walk,
        network, n_proc=processes, degree_bins=degree_correction_bins,
        diz=rw_dict(rwr_matrix, in_memory=rwr_matrix_in_memory))
    geneset_pairs = tuple((setname_a, genes_a, setname_b, genes_b)
                          for (setname_a, genes_a), (setname_b, genes_b)
                          in (combinations(genesets_a.items(), 2)
                              if not genesets_b else product(genesets_a.items(),
                                                             genesets_b.items()))
                          if setname_a != setname_b)
    results = tuple(run_comparison_on_genesets(sc_comparison, setname_a,
        genes_a, setname_b, genes_b, permutations=permutations,
        processes=processes, verbose=True)
        for setname_a, genes_a, setname_b, genes_b in geneset_pairs)
    pd.DataFrame(
        (('association_rwr', setname_a, setname_b, permutations, observed,
          pvalue, mean(null_d), variance(null_d))
         if len(set(null_d))>1 else ('association_rwr', setname_a, setname_b,
                                     permutations, observed, pvalue,
                                     mean(null_d), 0)
         for setname_a, setname_b, observed, pvalue, null_d in results),
         columns=('Analysis', 'Gene set A', 'Gene set B', 'Permutations',
                  'Observed', 'P-value', 'Null mean', 'Null variance')
    ).to_csv(output, index=False, sep='\t' if output.endswith('.tsv') else ',')
    null_dists = pd.DataFrame(
        ((setname_a, setname_b, val) for setname_a, setname_b, _, _, null_d
         in results for val in null_d),
        columns=('Gene set A', 'Gene set B', 'Null distribution')
    )
    observed = pd.DataFrame(
        ((setname_a, setname_b, observed, pvalue,
          (observed - mean(null_d)) / stdev(null_d),
          '*'*min(3, floor(-1*log10(2*pvalue))))
         if len(set(null_d))>1 else (setname_a, setname_b, observed, pvalue,
          0, '*'*min(3, floor(-1*log10(2*pvalue))))
         for setname_a, setname_b, observed, pvalue, null_d in results),
        columns=('Gene set A', 'Gene set B', 'Observed', 'P-value', 'Z-score',
                 'Significance')
    )
    if results_figure:
        if not genesets_b:
            plot_test_clustermap(observed, results_figure,
                              figure_type=results_figure_type.replace('box', 'obs'),
                              significance=results_figure_significance,
                              width=width, height=height)
        elif len(genesets_b) == 1 or len(genesets_a) == 1:
            if len(genesets_b) == 1:
                null_dists['Gene set'] = null_dists['Gene set A']
                observed['Gene set'] = observed['Gene set A']
            elif len(genesets_a) == 1:
                null_dists['Gene set'] = null_dists['Gene set B']
                observed['Gene set'] = observed['Gene set B']
            plot_test_results(null_dists,
                              observed.loc[:,['Gene set', 'Observed', 'Significance']],
                              results_figure,
                              figure_type=results_figure_type,
                              significance=results_figure_significance,
                              width=width, height=height,
                              strip_alpha=min(1, 32/permutations),
                              x_label='Association RWR statistic',
                              rotate_xtick=results_figure_rotate_xtick,
                              box_width=results_figure_box_width)
        else:
            plot_test_heatmap(observed, results_figure,
                              figure_type=results_figure_type.replace('box', 'obs'),
                              significance=results_figure_significance,
                              width=width, height=height)
    if null_distributions:
        null_dists.to_csv(null_distributions, index=False,
                          sep='\t' if null_distributions.endswith('.tsv')
                          else ',')
    if filtered_network_file:
        nx.to_pandas_edgelist(network).to_csv(filtered_network_file,
            sep='\t', header=False, index=False)