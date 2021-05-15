from django.conf import settings
from django.http import JsonResponse
from networkx import binomial_graph as to_binomial, to_numpy_array as to_array
from collections import defaultdict
from api.models import Kuramoto
from api.responses import access_denied


# DECORATORS
def validate(function):
    def wrapper(*args, **kwargs):
        return JsonResponse(access_denied, status=403, json_dumps_params={'indent': 4}) \
            if not (any(list(map(lambda data: data == settings.API_TOKEN,
                                 [args[-1].headers.get('Access-Token', None),
                                  kwargs.get('token', None)])))) else function(*args, **kwargs)
    return wrapper


# HANDLERS
class JSONHandler:
    def __init__(self, dict_type=None, matrix=None, names=None):
        if matrix is not None:
            self.matrix = matrix
        if names is not None:
            self.names = names

        self.response = defaultdict(dict if dict_type is None else dict_type)

    def createDict(self, dd_type=None):
        self.response = defaultdict(dict if dd_type is None else dd_type)
        return self

    def fromMatrix(self, matrix):
        self.matrix = matrix
        return self

    def withNames(self, names: tuple):
        self.names = names
        return self

    def collect(self, frames: int):
        positions = [list(self.matrix[object_id, :])[:frames] for object_id in range(len(self.names))]
        list(map(lambda name: list(
            map(lambda position: self.response['objects'].__setitem__(name, position), positions)), self.names))
        return self.response


class KuramotoHandler:
    def __init__(self, data: dict, handler=None, time=None):
        if handler is not None:
            self.handler = handler
        if time is not None:
            self.time = time
        self.data = data
        self.objects_name = tuple(data['objects'].keys())

    def connectHandler(self, handler):
        self.handler = handler
        return self

    def setTime(self, time):
        self.time = time
        return self

    def build(self):
        return self.__build(self.data['objects'])

    def __calculate(self, vibration_array: list, fps: int = 60):
        model = Kuramoto(coupling=3, dt=0.01, total_time=self.time, vibration_array=vibration_array)
        calculations = model.run(connectivity_matrix=to_array(to_binomial(n=len(self.objects_name), p=1)))
        return self.handler(matrix=calculations, names=self.objects_name).collect(fps * self.time)

    def __build(self, objects):
        vibration_array = [objects[self.objects_name[object_index]]['frequency'] for object_index in
                           range(len(objects))]
        return self.__calculate(vibration_array=vibration_array, fps=self.data['fps'])
