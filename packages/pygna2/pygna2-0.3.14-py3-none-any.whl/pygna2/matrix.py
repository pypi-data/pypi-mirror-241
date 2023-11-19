#===============================================================================
# matrix.py
#===============================================================================

"""Build the RWR diffusion matrix"""

# Imports ======================================================================

import networkx as nx
import numpy as np
import scipy
import logging
import tables
from pygna2.parse_network_genesets import parse_network

# Functions ====================================================================

def build_rwr_diffusion_matrix(network, output, beta: float = 0.85,
                               max_components=None,
                               min_component_size: int = 2,
                               filtered_network_file=None):
    """Build the RWR diffusion matrix
    
    Parameters
    ----------
    network : str
        TSV file defining the input network
    output : str
        Text file containing summary
    beta : float
        Beta (restart probability) parameter of diffusion
    max_components
        Load only n largest components
    min_component_size
        Load only components with at least n genes (default: 2)
    filtered_network
        Output file for filtered network (default: None)
    """

    network = parse_network(network, max_components=max_components,
                            min_component_size=min_component_size)
    nodes = list(network.nodes())
    logging.info("Beginning to calculate RWR matrix")
    a = nx.adjacency_matrix(network)
    k = 1 / np.array(list(dict(network.degree()).values()))
    d = scipy.sparse.dia_matrix((k, [0]), shape=a.shape)
    a = a.dot(d)
    n = np.shape(a)[1]
    with tables.open_file(output, mode="w") as hdf5_file:
        # create a hdf5 file with two objects:
        # - one is the nodes array,
        hdf5_file.create_array(hdf5_file.root, "nodes", nodes)
        # -  the other is the RWR matrix
        hdf5_file.create_array(hdf5_file.root, "matrix",
                               beta*np.linalg.inv(np.eye(n)-(1.0-beta)*a))
        logging.info("Saving network")
        hdf5_file.close()
    if filtered_network_file:
        nx.to_pandas_edgelist(network).to_csv(filtered_network_file,
            sep='\t', header=False, index=False)
