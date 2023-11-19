import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import log10
from scipy.cluster.hierarchy import linkage
from itertools import combinations

ANALYSIS_LABEL = {'topology_total_degree': 'Topology Total Degree',
                  'topology_internal_degree': 'Topology Internal Degree (%)',
                  'topology_module': 'Largest Module Size',
                  'topology_rwr': 'Topology RWR statistic',
                  'association_rwr': 'Association RWR statistic'}

sns.set_style('whitegrid')

def parse_results_file(results_file: str):
    sep = '\t' if results_file.endswith('.tsv') else ','
    observed = pd.read_csv(results_file, sep=sep)
    observed['Significance'] = ['*'*int(n_stars)
                                for n_stars in np.floor(
                                    -1*np.log10(2*observed['P-value'])
                                ).combine(3, min)]
    if observed.loc[0, 'Analysis'].startswith('topology'):
        results_type = 'one-v-many'
    elif len(observed['Gene set A'].unique()) == 1 or len(observed['Gene set B'].unique()) == 1:
        results_type = 'one-v-many'
    elif sorted(combinations(set(observed['Gene set A']).union(set(observed['Gene set B'])), 2)) == sorted(zip(observed['Gene set A'], observed['Gene set B'])):
        results_type = 'all-v-all'
    else:
        results_type = 'many-v-many'
    return observed, results_type

def plot_test_results(null_dists, observed, output: str,
                      figure_type: str = 'box', significance=False,
                      width: float = 7.0, height: float = 7.0,
                      strip_alpha: float = 1,
                      x_label='Topology Internal Degree (%)',
                      rotate_xtick=0):
    n_genesets = len(observed.index)
    if x_label.endswith('(%)'):
        null_dists['Null distribution'] *= 100
        observed['Observed'] *= 100
    if figure_type == 'box':
        ax = sns.boxplot(
            data=null_dists,
            x='Null distribution',
            y='Gene set',
            whis=[0, 100],
            width=.3,
            palette=sns.husl_palette(n_genesets, l=0.9),
            zorder=1
        )
    elif figure_type == 'violin':
        ax = sns.violinplot(
            data=null_dists,
            x='Null distribution',
            y='Gene set',
            inner=None,
            palette=sns.husl_palette(n_genesets, l=0.9),
            zorder=1
        )
    elif figure_type == 'strip':
        ax = sns.stripplot(
            data=null_dists,
            x='Null distribution',
            y='Gene set',
            alpha=strip_alpha,
            palette=sns.husl_palette(n_genesets, s=0.4),
            zorder=1
        )
    sns.pointplot(ax=ax, data=observed, x='Observed', y='Gene set',
                  join=False, markers='d', errorbar=None, color='white',
                  scale=1.1)
    sns.pointplot(ax=ax, data=observed, x='Observed', y='Gene set',
                  join=False, markers='d', errorbar=None, palette='husl',
                  scale=1)
    if significance:
        for tick, (_, (_, obs, sig)) in zip(ax.get_yticks(),
                                            observed.iterrows()):
            if sig:
                ax.text(obs, tick, sig, horizontalalignment='center',
                        verticalalignment='bottom', color='black')
    sns.despine(left=True, bottom=True)
    plt.xticks(rotation=rotate_xtick, ha='right')
    ax.set(ylabel="", xlabel=x_label)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    fig.savefig(output)


def compute_linkage_matrix(stat_matrix, method='complete', optimal_ordering=True):
    """Compute a linkage matrix defining a hierarchical clustering
    
    Parameters
    ---------
    stat_matrix
        pandas data frame containing the stat matrix
    method : str
        linkage algorithm for hierarchical clustering. See
        `scipy.cluster.hierarchy.linkage` for details.
    optimal_ordering : bool
        If True, the linkage matrix will be reordered so that the distance
        between successive leaves is minimal. See
        `scipy.cluster.hierarchy.linkage`
    """

    stat_matrix_np = stat_matrix.to_numpy()
    similarity = stat_matrix_np[np.triu_indices(len(stat_matrix.index), k=1)]
    distance = 1 - similarity / similarity.max()
    return linkage(distance, method=method, optimal_ordering=optimal_ordering)


def plot_test_clustermap(observed, output: str, figure_type: str = 'obs',
                         significance=False, cmap: str = 'rocket_r',
                         width: float = 7.0, height: float = 7.0,
                         method='complete', optimal_ordering: bool = True,
                         square: bool = True, heatmap_tick_pos='right',
                         cbar_tick_pos='left', dendrogram_ratio: float = 0.2,
                         dendrogram_spacer: float = 0.1):

    """Plot a clustered heatmap of genome similarity values

    Parameters
    ----------
    observed: DataFrame
        Pandas data frame representing the observed values
    output : str
        path to destination file for plot
    cmap : str
        color map for the heatmap
    width : float
        width of the plot in inches
    height : float
        height of the plot in inches
    method : str
        linkage algorithm for hierarchical clustering. See
        `scipy.cluster.hierarchy.linkage` for details.
    optimal_ordering : bool
        If True, the linkage matrix will be reordered so that the distance
        between successive leaves is minimal. See
        `scipy.cluster.hierarchy.linkage`
    square : bool
        If True, the heatmap will be drawn square. This may force the figure
        dimensions to be altered slightly
    heatmap_tick_pos: str
        Position of heatmap ticks. Must be "left" or "right" [right]
    cbar_tick_pos : str
        Position of color bar ticks. Must be "left" or "right" [left]
    dendrogram_ratio : float
        Fraction of plot width used for dendrogram [0.2]
    dendrogram_spacer : float
        Fraction of plot width used as spacer between dendrogram and heatmap [0.1]
    """

    genesets = sorted(set(observed['Gene set A']).union(set(observed['Gene set B'])))
    stat_matrix = pd.DataFrame(dtype=float, index=genesets, columns=genesets)
    sig_matrix = pd.DataFrame('', dtype=str, index=genesets, columns=genesets)
    for _, (setname_a, setname_b, obs, pvalue, zscore, sig) in observed.iterrows():
        if figure_type == 'obs':
            stat_matrix.loc[setname_a, setname_b] = obs
            stat_matrix.loc[setname_b, setname_a] = obs
        elif figure_type == 'zscore':
            stat_matrix.loc[setname_a, setname_b] = zscore
            stat_matrix.loc[setname_b, setname_a] = zscore
        elif figure_type == 'pvalue':
            stat_matrix.loc[setname_a, setname_b] = -1 * log10(pvalue)
            stat_matrix.loc[setname_b, setname_a] = -1 * log10(pvalue)
        sig_matrix.loc[setname_a, setname_b] = -1 * log10(pvalue)
        sig_matrix.loc[setname_b, setname_a] = -1 * log10(pvalue)
        # sig_matrix.loc[setname_a, setname_b] = sig
        # sig_matrix.loc[setname_b, setname_a] = sig

    link = compute_linkage_matrix(stat_matrix, method=method,
                                     optimal_ordering=optimal_ordering)
    ax = sns.clustermap(stat_matrix, cmap=cmap, figsize=(width, height),
                        row_linkage=link, col_linkage=link,
                        xticklabels=False,
                        dendrogram_ratio=(dendrogram_ratio,0),
                        annot=sig_matrix if significance else False)
    if square:
        ax.ax_heatmap.set_aspect("equal")
    ax.ax_col_dendrogram.set_visible(False)
    ax_hm_pos = ax.ax_heatmap.get_position()
    ax_row_pos = ax.ax_row_dendrogram.get_position()
    if heatmap_tick_pos == 'left':
            ax.ax_heatmap.set_position([.9-ax_hm_pos.width, ax_hm_pos.y0,
                                        ax_hm_pos.width, ax_hm_pos.height])
    elif heatmap_tick_pos == 'right':
            ax.ax_heatmap.set_position([ax_hm_pos.x0-.1, ax_hm_pos.y0,
                                        ax_hm_pos.width, ax_hm_pos.height])
    ax.ax_heatmap.yaxis.set_ticks_position(heatmap_tick_pos)
    ax.ax_heatmap.set_yticklabels(ax.ax_heatmap.get_yticklabels(), rotation=0)
    ax.ax_row_dendrogram.set_position([ax_row_pos.x0, ax_hm_pos.y0, 
                                       ax_row_pos.width-dendrogram_spacer,
                                       ax_hm_pos.height])
    ax.ax_cbar.set_position([.97, ax_hm_pos.y0, .03, ax_hm_pos.height])
    ax.ax_cbar.yaxis.set_ticks_position(cbar_tick_pos)
    ax.savefig(output)


def plot_test_heatmap(observed, output: str, figure_type: str = 'obs',
                         significance=False, cmap: str = 'rocket_r',
                         width: float = 7.0, height: float = 7.0,
                         square: bool = True):
    genesets_a = observed['Gene set A'].unique()
    genesets_b = observed['Gene set B'].unique()
    stat_matrix = pd.DataFrame(dtype=float, index=genesets_a, columns=genesets_b)
    sig_matrix = pd.DataFrame('', dtype=str, index=genesets_a, columns=genesets_b)
    for _, (setname_a, setname_b, obs, pvalue, zscore, sig) in observed.iterrows():
        if figure_type == 'obs':
            stat_matrix.loc[setname_a, setname_b] = obs
        elif figure_type == 'zscore':
            stat_matrix.loc[setname_a, setname_b] = zscore
        elif figure_type == 'pvalue':
            stat_matrix.loc[setname_a, setname_b] = -1 * log10(pvalue)
        sig_matrix.loc[setname_a, setname_b] = -1 * log10(pvalue)
        # sig_matrix.loc[setname_a, setname_b] = sig
    ax = sns.heatmap(stat_matrix, cmap=cmap, square=square,
                     annot=sig_matrix if significance else False)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    fig.savefig(output)
