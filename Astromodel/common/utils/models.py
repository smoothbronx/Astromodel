import networkx
from numpy import linspace, ones, array, flipud, sin, outer, pi
from numpy.random import rand, uniform
from scipy.integrate import odeint

from .exceptions import DataException
from .decorators import unweighted


class Kuramoto:
    @unweighted
    def __init__(self, graph, time: int = 20, dt: float = 0.01, connectivity=None, phases=None, frequencies=None):
        self.graph = graph
        self.dt = dt
        self.graph_array = networkx.to_numpy_array(self.graph)
        self.nodes_count = self.graph.number_of_nodes()
        self.time = linspace(self.dt, time * self.dt, time)
        self.array_of_ones = ones(self.nodes_count)

        self.connectivity = (array(connectivity) if connectivity.__len__() == self.nodes_count else
                             DataException('Connectivity must be equal to the number of oscillators').
                             raise_this()) if connectivity is not None else uniform(0.1, 10, self.nodes_count)

        self.null_theta = (phases if phases.__len__() == self.nodes_count
                           else DataException('Phases must be equal to the number of oscillators').raise_this()) \
            if phases is not None else 2 * pi * rand(self.nodes_count)

        self.omega = (frequencies if frequencies.__len__() == self.nodes_count
                      else DataException('Frequencies must be equal to the number of oscillators').raise_this()) \
            if frequencies is not None else uniform(0.9, 1.1, self.nodes_count)

    def simulate(self):
        wrapper = odeint(self.theta, self.null_theta, self.time, (self.connectivity, self.omega, self.graph_array))
        return flipud(wrapper.T) % (2 * pi)

    def theta(self, null_theta, time, connectivity, omega, graph_array):
        return omega + connectivity / self.nodes_count * \
               (self.graph_array * sin(outer(self.array_of_ones, null_theta)
                                          - outer(null_theta, self.array_of_ones))).dot(self.array_of_ones)