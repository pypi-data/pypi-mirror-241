from itertools import chain, islice
import networkx as nx
import pygna.reading_class as rc

def parse_network(network: str, max_components=None,
                  min_component_size: int = 2) -> nx.Graph:
    """Load network and geneset files, and return the network or subnetwork
    to operate on

    Parameters
    ----------
    network : str
        TSV file defining the input network
    max_components
        Load only n largest components
    min_component_size
        Load only components with at least n genes (default: 2)

    Returns
    -------
    nx.Graph
        The [filtered] network
    """

    network = rc.ReadTsv(network).get_network()
    if max_components or (min_component_size > 2):
        filtered_network = nx.Graph()
        for component in filter(lambda c: len(c)>=min_component_size,
                                islice(sorted(nx.connected_components(network),
                                    key=len, reverse=True), max_components)):
            filtered_network = nx.compose(filtered_network,
                                          network.subgraph(component).copy())
        network = filtered_network
    return network
    

def parse_genesets(genesets: str, setnames=None, min_set_size: int = 20) -> dict:
    """Load gene set files and parse them into a dict. If setnames are given,
    load the named sets, otherwise load all sets in the file

    Parameters
    ----------
    genesets
        GMT file containing gene sets (default: None)
    setnames
        List of gene set names (default: None)

    Returns
    -------
    dict
        Dictiinary of gene sets
    """

    if not setnames:
        setnames = tuple(gs for gs in rc.ReadGmt(genesets).get_data().keys()
                            if gs != 'Gene Set')
    genesets = dict((setname, genes) for setname, genes in chain.from_iterable(
        rc.ReadGmt(genesets).get_geneset(setname).items()
        for setname in setnames) if len(genes) > min_set_size)
    return genesets


def parse_network_and_genesets(network, genesets=None,
                               setnames=None, max_components=None,
                               min_component_size: int = 2,
                               min_set_size: int = 20) -> (nx.Graph, dict):
    """Load network and geneset files, and return the network or subnetwork
    to operate on

    Parameters
    ----------
    network : str
        TSV file defining the input network
    genesets
        GMT file containing gene sets (default: None)
    setnames
        List of gene set names (default: None)
    max_components
        Load only n largest components
    min_component_size : int
        Load only components with at least n genes (default: 2)
    min_set_size : int
        Only consider gene sets with more than n genes

    Returns
    -------
    nx.Graph
        The network of interest
    dict
        Dictionary of gene sets
    """

    network = parse_network(network, max_components=max_components,
                            min_component_size=min_component_size)
    genesets = parse_genesets(genesets, setnames=setnames,
                              min_set_size=min_set_size) if genesets else {}
    return network, genesets