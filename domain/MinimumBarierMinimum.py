# coding=utf8
from math import e

from domain.ForceField import ForceField


class MinimumBarierMinimum(ForceField):
    def __init__(self, time=0.0001, a=5.0, b=10.0, c=3.0, d=0.02):
        ForceField.__init__(self, time)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def single_atom_contribution(self, atom):
        force = -self.a * e ** (-self.b * (atom.coordinates - 1) ** 2) - self.c * e ** (
            -(atom.coordinates + 1) ** 2) + self.d * atom.coordinates ** 4
        atom.change_acc(force, self.time)
