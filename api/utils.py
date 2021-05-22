from django.conf import settings
from django.http import JsonResponse
import networkx as nx
import numpy as np
from functools import wraps
import warnings
from json import loads
from api.responses import access_denied, oscillators_len
import scipy.integrate as it
from typing import Any
from collections import defaultdict


# DECORATORS
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


def oscillators_count(count):
    def pre_wrapper(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) if loads(args[-1].body)['objects'].__len__() >= count \
                else JsonResponse(oscillators_len, status=500, json_dumps_params={'indent': 4})
        return wrapper
    return pre_wrapper


def ensure_unweighted(graph):
    for _, _, attr in graph.edges(data=True):
        if not np.isclose(attr.get("weight", 1.0), 1.0):
            new_graph = graph.__class__()
            new_graph.add_nodes_from(graph)
            new_graph.add_edges_from(graph.edges)
            warnings.warn("Coercing weighted graph to unweighted.", RuntimeWarning)
            return new_graph
    return graph


# MODELS
class Kuramoto:
    __results = defaultdict(dict)

    @unweighted
    def __init__(self, graph, time: int = 20, dt: float = 0.01, connectivity=None, phases=None, frequencies=None):
        self.graph = graph
        self.dt = dt
        self.graph_array = nx.to_numpy_array(self.graph)
        self.nodes_count = self.graph.number_of_nodes()
        self.time = np.linspace(self.dt, time * self.dt, time)
        self.array_of_ones = np.ones(self.nodes_count)

        self.connectivity = (np.array(connectivity) if connectivity.__len__() == self.nodes_count else
                             DataLengthException('Connectivity must be equal to the number of oscillators').
                             raise_this()) if connectivity is not None else np.random.uniform(0.1, 10, self.nodes_count)

        self.null_theta = (phases if phases.__len__() == self.nodes_count
                           else DataLengthException('Phases must be equal to the number of oscillators').raise_this()) \
            if phases is not None else 2 * np.pi * np.random.rand(self.nodes_count)

        self.omega = (frequencies if frequencies.__len__() == self.nodes_count
                      else DataLengthException('Frequencies must be equal to the number of oscillators').raise_this()) \
            if frequencies is not None else np.random.uniform(0.9, 1.1, self.nodes_count)

    def simulate(self):
        ts_wrapper = it.odeint(self.theta, self.null_theta, self.time, args=(self.connectivity, self.omega, self.graph_array))
        ts = np.flipud(ts_wrapper.T) % (2 * np.pi)

        self.__results["internal_frequencies"] = self.omega
        self.__results["ground_truth"] = self.graph
        self.__results["TS"] = ts
        return ts

    def getResults(self):
        return self.__results

    def __set_res(self, path: str, obj: Any):
        return self.__results.__setitem__(path, obj)

    def theta(self, null_theta, time, connectivity, omega, graph_array):
        return omega + connectivity / self.nodes_count * \
               (self.graph_array * np.sin(np.outer(self.array_of_ones, null_theta)
                                          - np.outer(null_theta, self.array_of_ones))).dot(self.array_of_ones)


class DataLengthException(Exception):
    def __init__(self, message: str):
        self.__message = message

    def raise_this(self):
        raise self

    def __repr__(self):
        return self.__message


# HANDLERS
class JSONHandler:
    def __init__(self, data_matrix, names: tuple):
        self.matrix = data_matrix
        self.names = names
        self.response = defaultdict(dict)

    def collect(self, frames: int):
        positions = [list(self.matrix[-object_index-1, :])[:frames] for object_index in range(self.names.__len__())]
        list(map(lambda index: self.response['objects'].__setitem__(self.names[index], positions[index]),
                 (index for index in range(self.names.__len__()))))
        self.response['frames'] = frames
        return self.response


class KuramotoHandler:
    response = defaultdict(dict)

    def __init__(self, data: dict, handler=None):
        self.objects_list = data.get("objects")

        self.fps = data.get("fps")
        self.time = data.get("time")

        self.objects_names = tuple(self.objects_list.keys())
        self.phases = self.__get_param('start_angle')
        self.frequencies = self.__get_param('frequency')
        self.connectivities = self.__get_param('connectivity')

        self.handler = handler if handler is not None else JSONHandler

    def setHandler(self, handler):
        self.handler = handler
        return self

    def build(self):
        return self.__build()

    def __get_param(self, parameter_name: str) -> list:
        return list(map(lambda object_name: self.objects_list[object_name].get(parameter_name), self.objects_names))

    def __build(self):
        graph = nx.erdos_renyi_graph(n=self.objects_list.__len__(), p=1)
        frames = self.fps * self.time
        calculations = Kuramoto(graph, frames, dt=1/self.fps, connectivity=self.connectivities,
                                phases=self.phases, frequencies=self.frequencies).simulate()
        return self.handler(calculations, self.objects_names).collect(frames)


