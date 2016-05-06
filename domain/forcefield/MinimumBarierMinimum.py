# coding=utf8
from math import e

from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class MinimumBarierMinimum(ForceField):
    def __init__(self, a=5.0, b=10.0, c=3.0, d=0.02):
        ForceField.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def single_atom_contribution(self, atom):
        potential_energy = -self.a * e ** (-self.b * (atom.coordinates - 1) ** 2) - self.c * e ** (
            -(atom.coordinates + 1) ** 2) + self.d * atom.coordinates ** 4
        force = []
        for coord in atom.coordinates:
            first_part = 2 * self.a * self.b * (coord - 1) * e ** (-self.b * (coord - 1) ** 2)
            second_part = 2 * self.c * (coord + 1) * e ** (-(coord + 1) ** 2)
            third_part = 4 * self.d * coord ** 3
            force.append(first_part + second_part + third_part)
        atom.change_acc(Vector(force), potential_energy)
