#===============================================================================
# pygna2.py
#===============================================================================

"""Gene network analysis"""

# Imports ======================================================================

import numpy as np
import pandas as pd
import logging
import sys
from argparse import ArgumentParser
from math import floor, log10
import pygna.statistical_test as st
from pygna2.version import __version__
from pygna2.network import summary, filter_network, cytoscape
from pygna2.matrix import build_rwr_diffusion_matrix
from pygna2.test_topology import test_topology
from pygna2.test_association import test_association
from pygna2.test_plot import (ANALYSIS_LABEL, plot_test_results,
                              plot_test_clustermap, plot_test_heatmap,
                              parse_results_file)

# Logging ======================================================================

logging.basicConfig(level=logging.INFO)

# Functions ====================================================================

def _summary(args):
    summary(args.network, args.output, genesets=args.genesets,
            setnames=args.setname, net_name=args.network_name,
            max_components=args.max_components,
            min_component_size=args.min_component_size,
            min_set_size=args.min_set_size, minimal=args.minimal,
            strict=args.strict, plot_degree_file=args.plot_degree,
            plot_component_file=args.plot_component,
            filtered_network_file=args.filtered_network)


def _filter_network(args):
    filter_network(args.network, args.output, genesets=args.genesets,
            setnames=args.setname, max_components=args.max_components,
            min_component_size=args.min_component_size,
            min_set_size=args.min_set_size, minimal=args.minimal,
            strict=args.strict,
            max_output_components=args.max_output_components,
            min_output_component_size=args.min_output_component_size)


def _cytoscape(args):
    cytoscape(args.network, args.output_graphml,
              components_out=args.components_out,
              genesets=args.genesets, setnames=args.setname,
              max_components=args.max_components,
              min_component_size=args.min_component_size,
              min_set_size=args.min_set_size, minimal=args.minimal,
              strict=args.strict, full_network=args.full,
              max_output_components=args.max_output_components,
              min_output_component_size=args.min_output_component_size,
              filtered_network_file=args.filtered_network)


def _build_rwr_diffusion_matrix(args):
    build_rwr_diffusion_matrix(args.network, args.output, beta=args.beta,
                               max_components=args.max_components,
                               min_component_size=args.min_component_size,
                               filtered_network_file=args.filtered_network)


def _test_topology_total_degree(args):
    test_topology(args.network, args.genesets, args.output,
        stat=st.geneset_total_degree_statistic,
        stat_name='topology_total_degree',
        setnames=args.setname, max_components=args.max_components,
        min_component_size=args.min_component_size,
        min_set_size=args.min_set_size,
        results_figure=args.results_figure,
        results_figure_type=args.results_figure_type,
        results_figure_significance=args.results_figure_significance,
        results_figure_x_label='Topology Total Degree',
        width=args.results_figure_width, height=args.results_figure_height,
        null_distributions=args.null_distributions,
        filtered_network_file=args.filtered_network,
        degree_correction_bins=args.degree_correction_bins,
        permutations=args.permutations, processes=args.cores)


def _test_topology_internal_degree(args):
    test_topology(args.network, args.genesets, args.output,
        setnames=args.setname, max_components=args.max_components,
        min_component_size=args.min_component_size,
        min_set_size=args.min_set_size,
        results_figure=args.results_figure,
        results_figure_type=args.results_figure_type,
        results_figure_significance=args.results_figure_significance,
        width=args.results_figure_width, height=args.results_figure_height,
        null_distributions=args.null_distributions,
        filtered_network_file=args.filtered_network,
        degree_correction_bins=args.degree_correction_bins,
        permutations=args.permutations, processes=args.cores)


def _test_topology_module(args):
    test_topology(args.network, args.genesets, args.output,
        stat=st.geneset_module_statistic,
        stat_name='topology_module',
        setnames=args.setname, max_components=args.max_components,
        min_component_size=args.min_component_size,
        min_set_size=args.min_set_size,
        results_figure=args.results_figure,
        results_figure_type=args.results_figure_type,
        results_figure_significance=args.results_figure_significance,
        results_figure_x_label='Largest Module Size',
        width=args.results_figure_width, height=args.results_figure_height,
        null_distributions=args.null_distributions,
        filtered_network_file=args.filtered_network,
        degree_correction_bins=args.degree_correction_bins,
        permutations=args.permutations, processes=args.cores)


def _test_topology_rwr(args):
    test_topology(args.network, args.genesets, args.output,
        rwr_matrix=args.rwr_matrix,
        stat=st.geneset_RW_statistic,
        stat_name='topology_rwr',
        setnames=args.setname, max_components=args.max_components,
        min_component_size=args.min_component_size,
        min_set_size=args.min_set_size,
        results_figure=args.results_figure,
        results_figure_type=args.results_figure_type,
        results_figure_significance=args.results_figure_significance,
        results_figure_x_label='Topology RWR statistic',
        width=args.results_figure_width, height=args.results_figure_height,
        null_distributions=args.null_distributions,
        filtered_network_file=args.filtered_network,
        rwr_matrix_in_memory=args.in_memory,
        degree_correction_bins=args.degree_correction_bins,
        permutations=args.permutations, processes=args.cores)


def _test_association(args):
    test_association(args.network, args.genesets_a, args.output,
        args.rwr_matrix, genesets_b=args.genesets_b,
        setnames_a=args.setname_a, setnames_b=args.setname_b,
        max_components=args.max_components,
        min_component_size=args.min_component_size,
        min_set_size=args.min_set_size,
        results_figure=args.results_figure,
        results_figure_type=args.results_figure_type,
        results_figure_significance=args.results_figure_significance,
        width=args.results_figure_width, height=args.results_figure_height,
        null_distributions=args.null_distributions,
        filtered_network_file=args.filtered_network,
        rwr_matrix_in_memory=args.in_memory,
        degree_correction_bins=args.degree_correction_bins,
        permutations=args.permutations, processes=args.cores)

def _plot_test_results(args):
    observed, results_type = parse_results_file(args.results)
    if results_type == 'one-v-many':
        if not args.type in {'box', 'strip', 'violin'}:
            raise RuntimeError('invalid figure type')
        if args.null_distributions:
            sep = '\t' if args.null_distributions.endswith('.tsv') else ','
            null_dists = pd.read_csv(args.null_distributions, sep=sep)
            if len(observed['Gene set B'].unique()) == 1:
                null_dists['Gene set'] = null_dists['Gene set A']
                observed['Gene set'] = observed['Gene set A']
            elif len(observed['Gene set A'].unique()) == 1:
                null_dists['Gene set'] = null_dists['Gene set B']
                observed['Gene set'] = observed['Gene set B']
            plot_test_results(null_dists, observed.loc[:,['Gene set', 'Observed', 'Significance']], args.output,
                              figure_type=args.type,
                              significance=args.significance,
                              width=args.width, height=args.height,
                              x_label=ANALYSIS_LABEL[observed.loc[0,'Analysis']],
                              rotate_xtick=args.rotate_xtick)
        else:
            raise RuntimeError('null distributions are required for one-v-many plot')
    else:
        figure_type = args.type.replace('box', 'obs')
        if not figure_type in {'obs', 'zscore', 'pvalue'}:
            raise RuntimeError('invalid figure type')
        observed['Z-score'] = (observed['Observed']-observed['Null mean'])/np.sqrt(observed['Null variance'])
        if results_type == 'all-v-all':
            plot_test_clustermap(observed.loc[:,['Gene set A', 'Gene set B', 'Observed', 'P-value', 'Z-score', 'Significance']],
                                 args.output, figure_type=figure_type,
                                 significance=args.significance,
                                 width=args.width, height=args.height)
        elif results_type == 'many-v-many':
            plot_test_heatmap(observed.loc[:,['Gene set A', 'Gene set B', 'Observed', 'P-value', 'Z-score', 'Significance']],
                                 args.output, figure_type=figure_type,
                                 significance=args.significance,
                                 width=args.width, height=args.height)
        


def add_network_arg(parser):
    parser.add_argument('network', metavar='<network.tsv>',
        help='Table defining network, 1st 2 cols should be gene pairs/edges')


def add_network_args(parser):
    add_network_arg(parser)
    parser.add_argument('--max-components', metavar='<int>', type=int,
        help='Use only n largest components')
    parser.add_argument('--min-component-size', metavar='<int>', type=int,
        default=2,
        help='Use only components with at least n genes (default: 2)')


def add_geneset_args(parser, full_arg=False):
    parser.add_argument('--genesets', metavar='<genesets.gmt>',
                        help='GMT file containing gene sets')
    parser.add_argument('--setname', metavar='<name>', nargs='+',
                        help='List of gene set names')
    parser.add_argument('--min-set-size', metavar='<int>', type=int, default=20,
                        help='Minimum gene set size (default: 20)')
    completeness_group = parser.add_mutually_exclusive_group()
    completeness_group.add_argument('--minimal', action='store_true',
        help='Filter out genes that are not part of a path between set members')
    completeness_group.add_argument('--strict', action='store_true',
        help='Filter out genes that are not part of a gene set')
    return completeness_group


def construct_network_parser(parser, func):
    parser.set_defaults(func=func)
    add_network_args(parser)
    return add_geneset_args(parser)


def add_output_component_args(parser):
    parser.add_argument('--max-output-components', metavar='<int>', type=int,
        help='Store only n largest components')
    parser.add_argument('--min-output-component-size', metavar='<int>',
        type=int, default=2,
        help='Store only components with at least n genes (default: 2)')


def add_results_fig_param_args(parser):
    parser.add_argument('--results-figure-significance', action='store_true',
                        help='Draw asterisks over significant results')
    parser.add_argument('--results-figure-width', metavar='<float>',
                        type=float, default=7.0,
                        help='Width of plot in inches')
    parser.add_argument('--results-figure-height', metavar='<float>',
                        type=float, default=7.0,
                        help='Height of plot in inches')


def add_null_dist_arg(parser):
    parser.add_argument('--null-distributions', metavar='<null.{csv,tsv}>',
                        help='Write null distributions to disk')

def add_filtered_network_arg(parser):
    parser.add_argument('--filtered-network', metavar='<filtered.tsv>',
        help='Write TSV file containing filtered network')


def add_permutation_args(parser):
    parser.add_argument('--degree-correction-bins', metavar='<int>', type=int,
        default=1, help='Apply degree correction using n bins (default: 1)')
    parser.add_argument('--permutations', metavar='<int>', type=int,
                        default=200,
                        help='Number of permutations (default: 200)')


def add_parallelization_args(parser):
    parser.add_argument('--cores', metavar='<int>', type=int, default=1,
                        help='Number of cores (default: 1)')


def construct_test_topology_parser(parser, func):
    parser.set_defaults(func=func)
    add_network_args(parser)
    parser.add_argument('genesets', metavar='<genesets.gmt>',
                        help='GMT file containing gene sets')
    parser.add_argument('output', metavar='<output.{csv,tsv}>',
                        help='Results table file')
    parser.add_argument('--setname', metavar='<name>', nargs='+',
                        help='List of gene set names')
    parser.add_argument('--min-set-size', metavar='<int>', type=int, default=20,
                        help='Minimum gene set size (default: 20)')
    parser.add_argument('--results-figure', metavar='<figure.{pdf,png,svg}>',
                        help='Path to results figure')
    parser.add_argument('--results-figure-type',
                        choices=('box', 'violin', 'strip'), default='box',
                        help='Type of results figure(default: box)')
    add_results_fig_param_args(parser)
    add_null_dist_arg(parser)
    add_filtered_network_arg(parser)
    add_permutation_args(parser)
    add_parallelization_args(parser)


def construct_test_association_parser(parser, func):
    parser.set_defaults(func=func)
    add_network_args(parser)
    parser.add_argument('genesets_a', metavar='<genesets-a.gmt>',
                        help='GMT file containing gene sets')
    parser.add_argument('output', metavar='<output.{csv,tsv}>',
                        help='Results table file')
    parser.add_argument('--genesets-b', metavar='<genesets-b.gmt>',
                        help='GMT file containing gene sets')
    parser.add_argument('--setname-a', metavar='<name>', nargs='+',
                        help='List of gene set names')
    parser.add_argument('--setname-b', metavar='<name>', nargs='+',
                        help='List of gene set names')
    parser.add_argument('--min-set-size', metavar='<int>', type=int, default=20,
                        help='Minimum gene set size (default: 20)')
    parser.add_argument('--results-figure', metavar='<figure.{pdf,png,svg}>',
                        help='Path to results figure')
    parser.add_argument('--results-figure-type',
                        choices=('box', 'violin', 'strip', 'obs', 'zscore',
                                 'pvalue'),
                        default='box',
                        help='Type of results figure (default: box/obs)')
    add_results_fig_param_args(parser)
    add_null_dist_arg(parser)
    add_filtered_network_arg(parser)
    add_permutation_args(parser)
    add_parallelization_args(parser)
    

def parse_arguments():
    parser = ArgumentParser(
        description='Statistical tests on gene networks and gene sets')
    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))
    parser.set_defaults(func=lambda _: parser.print_help(sys.stdout))
    subparsers = parser.add_subparsers()
    
    # Network parsers
    parser_network = subparsers.add_parser('network',
        help='Report properties of the network')
    network_parsers = parser_network.add_subparsers()
    parser_network_summary = network_parsers.add_parser('summary',
        help='Summarize the network')
    construct_network_parser(parser_network_summary, _summary)
    parser_network_summary.add_argument('output', metavar='<output.txt>',
                              help='Text file containing summary')
    parser_network_summary.add_argument('--network-name', metavar='<name>',
        default='network', help='A name for the network')
    parser_network_summary.add_argument('--plot-degree',
        metavar='<output.{pdf,png}>', help='Plot the degree distribution')
    parser_network_summary.add_argument('--plot-component',
        metavar='<output.{pdf,png}>',
        help='Plot the distribution of component sizes')
    parser_network_summary.add_argument('--filtered-network',
        metavar='<filtered.tsv>',
        help='Write TSV file containing filtered network')
    parser_network_filter = network_parsers.add_parser('filter',
        help='Filter small components out of the network')
    construct_network_parser(parser_network_filter, _filter_network)
    add_output_component_args(parser_network_filter)
    parser_network_filter.add_argument('output', metavar='<output.tsv>',
        help='TSV file containing filtered network')
    parser_network_cytoscape = network_parsers.add_parser('cytoscape',
        help='Generate a GraphML file that can be viewed in cytoscape')
    completeness_group_cytoscape = construct_network_parser(parser_network_cytoscape, _cytoscape)
    add_output_component_args(parser_network_cytoscape)
    parser_network_cytoscape.add_argument('output_graphml',
        metavar='<output.graphml>',
        help='GraphML file containing network or subnetwork')
    parser_network_cytoscape.add_argument('--components-out',
        metavar='<components.gmt>',
        help='Write GMT file containing components of the output graph')
    completeness_group_cytoscape.add_argument('--full', action='store_true',
        help='Store the full network')
    parser_network_cytoscape.add_argument('--filtered-network',
        metavar='<filtered.tsv>',
        help='Write TSV file containing filtered network')
    
    # Build parser
    parser_build = subparsers.add_parser('build',
        help='Build a RWR diffusion matrix')
    parser_build.set_defaults(func=_build_rwr_diffusion_matrix)
    add_network_args(parser_build)
    parser_build.add_argument('output', metavar='<rwr-matrix.hdf5>',
                         help='Output file for RWR diffusion matrix')
    parser_build.add_argument('--beta', metavar='<float>', type=float,
                         default=0.85, help='Restart probability (default: 0.85)')
    parser_build.add_argument('--filtered-network', metavar='<filtered.tsv>',
                              help='Write TSV file containing filtered network')

    # Test parsers
    parser_test = subparsers.add_parser('test', help='Statistical tests')
    test_parsers = parser_test.add_subparsers()
    parser_ttd = test_parsers.add_parser('ttd',
        help='Topology Total Degree statistic')
    construct_test_topology_parser(parser_ttd, _test_topology_total_degree)
    parser_tid = test_parsers.add_parser('tid',
        help='Topology Internal Degree statistic')
    construct_test_topology_parser(parser_tid, _test_topology_internal_degree)
    parser_tm = test_parsers.add_parser('tm',
        help='Topology Module statistic (largest module size)')
    construct_test_topology_parser(parser_tm, _test_topology_module)
    parser_trwr = test_parsers.add_parser('trwr',
        help='Topology Random Walk with Restart diffusion statistic')
    construct_test_topology_parser(parser_trwr, _test_topology_rwr)
    parser_trwr.add_argument('rwr_matrix', metavar='<rwr-matrix.hdf5>',
        help='RWR diffusion matrix')
    parser_trwr.add_argument('--in-memory', action='store_true',
        help='Load the entire RWR diffusion matrix in memory')
    parser_arwr = test_parsers.add_parser('arwr',
        help='Association Random Walk with Restart diffusion statistic')
    construct_test_association_parser(parser_arwr, _test_association)
    parser_arwr.add_argument('rwr_matrix', metavar='<rwr-matrix.hdf5>',
        help='RWR diffusion matrix')
    parser_arwr.add_argument('--in-memory', action='store_true',
        help='Load the entire RWR diffusion matrix in memory')

    # Plot parsers
    parser_plot = subparsers.add_parser('plot',
        help='Plot a figure from a results table')
    parser_plot.set_defaults(func=_plot_test_results)
    parser_plot.add_argument('results', metavar='<results.{csv,tsv}>',
                        help='Results table from pygna2 test')
    parser_plot.add_argument('output', metavar='<output.{pdf,png,svg}>',
                        help='Output file for plot')
    parser_plot.add_argument('--null-distributions',
                        metavar='<null_distributions.{csv,tsv}>',
                        help='Null distributions from pygna2 test, required for topology or one-v-many')
    parser_plot.add_argument('--type', choices=('box', 'violin', 'strip', 'obs',
                                           'zscore', 'pvalue'),
                        default='box',
                        help='Type of results figure (default: box/obs)')
    parser_plot.add_argument('--significance', action='store_true',
                        help='Draw asterisks over significant results')
    parser_plot.add_argument('--width', metavar='<float>', type=float, default=7.0,
                        help='Width of plot in inches')
    parser_plot.add_argument('--height', metavar='<float>', type=float, default=7.0,
                        help='Height of plot in inches')
    parser_plot.add_argument('--rotate-xtick', metavar='<int>', type=int, default=0,
                        help='Rotate x tick labels')
    return parser.parse_args()

def main():
    args = parse_arguments()
    args.func(args)
