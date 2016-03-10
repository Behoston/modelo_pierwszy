# coding=utf8
from domain.Atom import Atom
from domain.ForceField import ForceField


class SoftWall(ForceField):
    def __init__(self, time=0.0001, size=5.0, f=1.0):
        ForceField.__init__(self, time)
        self.size = size
        self.f = f

    def single_atom_contribution(self, atom):
        force = 0.5 * self.f * (self.size - atom.coordinates.length())
        atom.change_acc(force, self.time)
