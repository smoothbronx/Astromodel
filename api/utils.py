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
                                 [args[-1].headers.get('access-token', None),
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
        list(map(lambda index: self.response['objects'].__setitem__(self.names[index], positions[index]),
                 (index for index in range(len(self.names)))))
        self.response['frames'] = frames
        return self.response


class KuramotoHandler:
    def __init__(self, data: dict, handler=None):
        if handler is not None:
            self.handler = handler

        self.time = data.get('time', 20)
        self.fps = data.get('fps', 60)
        self.oscillators = data.get('objects')
        self.objects_name = tuple(self.oscillators.keys())
        self.start_angles = list(map(lambda name: float(self.oscillators[f'{name}'].get('start_angle')), self.objects_name))

    def connectHandler(self, handler):
        self.handler = handler
        return self

    def build(self):
        return self.__build(self.oscillators)

    def __calculate(self, vibration_array: list, fps: int = 60):
        model = Kuramoto(coupling=3, dt=0.01, total_time=self.time, vibration_array=vibration_array)
        calculations = model.run(connectivity_matrix=to_array(to_binomial(n=self.oscillators.__len__, p=self.oscillators.__len__)),
                                 angles_vector=self.start_angles)
        return self.handler(matrix=calculations, names=self.objects_name).collect(fps * self.time)

    def __build(self, objects):
        vibration_array = [objects[self.objects_name[object_index]]['frequency'] for object_index in
                           range(len(objects))]
        return self.__calculate(vibration_array=vibration_array, fps=self.fps)
