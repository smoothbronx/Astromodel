import networkx as nx
from collections import defaultdict
from .models import Kuramoto
from .exceptions import DataException

class JSONHandler:
    def __init__(self, data_matrix, names: tuple):
        self.matrix = data_matrix
        self.names = names
        self.response = defaultdict(dict)

    def collect(self, frames):
        positions = [list(self.matrix[-object_index-1, :])[:frames] for object_index in range(self.names.__len__())]
        list(map(lambda index: self.response['objects'].__setitem__(self.names[index], positions[index]),
                 (index for index in range(self.names.__len__()))))
        self.response['frames'] = frames
        return self.response


class KuramotoHandler:
    response = defaultdict(dict)

    def __init__(self, data: dict = None, handler=None):
        if data is not None:
            self.__initialize__(data)

    def setHandler(self, handler):
        self.handler = handler
        return self
    
    def setData(self, data):
        self.__initialize__(data)
        return self

    def build(self):
        return self.__build()

    def __get_param(self, parameter_name: str) -> list:
        return list(map(lambda object_name: self.objects_list[object_name].get(parameter_name), self.objects_names))

    def __build(self):
        graph = nx.erdos_renyi_graph(n=self.objects_list.__len__(), p=1)
        calculations = Kuramoto(graph, self.frames, dt=1/self.fps, connectivity=self.connectivities,
                                phases=self.phases, frequencies=self.frequencies).simulate()
        return self.handler(calculations, self.objects_names).collect(self.frames)
    
    def __initialize__(self, data, handler=None):
        
        if data is None:
            raise DataException("Data does`t exist. Check the integrity of the input parameters.")
        
        self.objects_list = data.get("objects")

        self.fps = data.get("fps")
        self.time = data.get("time")
        self.frames = self.fps * self.time

        self.objects_names = tuple(self.objects_list.keys())
        self.phases = self.__get_param('start_angle')
        self.frequencies = self.__get_param('frequency')
        self.connectivities = self.__get_param('connectivity')

        self.handler = handler if handler is not None else JSONHandler