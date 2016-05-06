# coding=utf8
from math import fabs

from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class SoftWall(ForceField):
    def __init__(self, size=5.0, f=1.0):
        ForceField.__init__(self)
        self.size = size
        self.f = f

    def single_atom_contribution(self, atom):
        length = atom.coordinates.length()
        potential_energy = 0.0
        force = []
        for coord in atom.coordinates:
            force.append(0.0)
            if fabs(coord) > self.size:
                potential_energy = 0.5 * self.f * (self.size - length)
                force[-1] = (0.5 * self.f * self.size - coord)
        atom.change_acc(Vector(force), potential_energy)
