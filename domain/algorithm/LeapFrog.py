# coding=utf-8
from domain.algorithm.Integrator import Integrator


class LeapFrog(Integrator):
    def __init__(self):
        Integrator.__init__(self)

    def make_step(self, atoms, time_delta):
        for atom in atoms:
            v = atom.velocity + atom.acceleration * time_delta
            r = atom.coordinates + v * time_delta
            atom.move(v, r)
