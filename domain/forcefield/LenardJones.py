# coding=utf8
from math import fabs

from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class LenardJones(ForceField):
    def __init__(self, R=1.0, epsilon=1.0):
        ForceField.__init__(self)
        self.R = R
        self.R6 = R ** 6
        self.R12 = self.R6 ** 2
        self.epsilon = epsilon

    def pair_atoms_contribution(self, atom1, atom2):
        distance = (atom1 - atom2).length()
        potential_energy = self.epsilon * ((self.R / distance) ** 12 - 2 * (self.R / distance) ** 6)
        force = []
        for i in xrange(atom1.dim):
            dist = fabs(atom1[i] - atom2[i])
            first = self.R12 / dist ** 12
            second = 2 * self.R6 / dist ** 6
            force.append(self.epsilon * (first - second))
        atom1.change_acc(Vector(force), potential_energy)
