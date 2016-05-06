# coding=utf-8
from domain.algorithm.Integrator import Integrator


class Verlet(Integrator):
    def __init__(self):
        Integrator.__init__(self)

    def make_step(self, atoms, time_delta):
        for atom in atoms:
            v = (atom.coordinates - atom.coordinates_minus_1) / time_delta
            r = 2 * atom.coordinates - atom.coordinates_minus_1 + atom.acceleration + time_delta ** 2
            atom.move(v, r)
