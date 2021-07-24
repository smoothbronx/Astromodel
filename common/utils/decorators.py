from django.conf import settings
from django.http import JsonResponse
import networkx as nx
import numpy as np
from functools import wraps
from .responses import access_denied

def validate(function):
    def wrapper(*args, **kwargs):
        return JsonResponse(access_denied, status=403, json_dumps_params={'indent': 4}) \
            if not (any(list(map(lambda data: data == settings.API_TOKEN,
                                 [args[-1].headers.get('access-token', None),
                                  kwargs.get('token', None)])))) else function(*args, **kwargs)
    return wrapper

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