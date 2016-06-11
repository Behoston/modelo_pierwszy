# coding=utf8
from math import fabs

from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class SoftWall(ForceField):
    def __init__(self, size=5.0, f=1.0):
        ForceField.__init__(self)
        if size is None:
            size = 5.0
        if f is None:
            f = 1.0
        self.L = size
        self.f = f

    def how_many_atoms_contribution(self):
        return 1

    def single_atom_contribution(self, atom):
        potential_energy = 0.0
        force = []
        for coord in atom.coordinates:
            force.append(0.0)
            if coord > self.L:
                potential_energy = 0.5 * self.f * (self.L - coord) ** 2
                force[-1] = -self.f * (coord - self.L)
            elif coord < - self.L:
                potential_energy = 0.5 * self.f * (coord + self.L) ** 2
                force[-1] = -self.f * (self.L + coord)
            atom.add_potential_energy(potential_energy)
        atom.change_acc(Vector(force))
