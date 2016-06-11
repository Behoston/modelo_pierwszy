# coding=utf-8
from domain.algorithm.Integrator import Integrator


class VelocityVerlet(Integrator):
    def __init__(self):
        Integrator.__init__(self)

    def make_step(self, atoms, time_delta):
        for atom in atoms:
            v = atom.velocity + (atom.acceleration_minus_1 + atom.acceleration) * (time_delta / 2)
            r = (atom.coordinates + v * time_delta) + ((atom.acceleration / 2) * time_delta ** 2)
            atom.move(v, r)
