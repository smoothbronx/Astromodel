import networkx as nx
import numpy as np
from functools import wraps

def unweighted(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ensure_unweighted(arg) if issubclass(arg.__class__, nx.Graph) else arg for arg in args]
        return func(*args, **kwargs)
    return wrapper

def ensure_unweighted(graph):
    for _, _, attr in graph.edges(data=True):
        if not np.isclose(attr.get("weight", 1.0), 1.0):
            new_graph = graph.__class__()
            new_graph.add_nodes_from(graph)
            new_graph.add_edges_from(graph.edges)
            return new_graph
    return graph