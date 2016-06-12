# coding=utf8
from math import fabs

from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class LenardJones(ForceField):
    def __init__(self, R=1.0, epsilon=1.0):
        ForceField.__init__(self)
        self.R = R
        self.R6 = R ** 6
        self.epsilon = epsilon

    def how_many_atoms_contribution(self):
        return 2

    # def f(self, atom1, atom2, i):
    #     numerator = (atom1.coordinates[i] - atom2.coordinates[i])
    #     if atom1.dim == 1:
    #         return numerator / (numerator ** 2) ** 0.5
    #     elif atom1.dim == 2:
    #
    #         return numerator / ((atom1.coordinates[0] - atom2.coordinates[0]) ** 2 + (
    #             atom1.coordinates[1] - atom2.coordinates[1]) ** 2) ** 0.5
    #     else:
    #         return numerator / ()

    def pair_atoms_contribution(self, atom1, atom2):
        distance = (atom1.coordinates - atom2.coordinates).length()
        potential_energy = self.epsilon * ((self.R / distance) ** 12 - 2 * (self.R / distance) ** 6)
        force1 = []
        force2 = []
        for i in xrange(atom1.dim):
            dist = atom1.coordinates[i] - atom2.coordinates[i]
            if dist == 0:
                f1 = 0
                f2 = 0
            else:
                f1 = 12 * self.epsilon * self.R6 * (self.R6 - distance ** 6) * dist / distance ** 14
                f2 = -12 * self.epsilon * self.R6 * (self.R6 - distance ** 6) * dist / distance ** 14
                # f1 = -12 * self.epsilon * self.R6 * dist * (self.R6 - dist ** 6) / distance ** 14
                # f2 = -12 * self.epsilon * self.R6 * dist * (dist ** 6 - self.R6) / distance ** 14
            force1.append(f1)
            force2.append(f2)
        atom1.change_acc(Vector(force1))
        atom2.change_acc(Vector(force2))
        atom1.add_potential_energy(potential_energy)
        atom2.add_potential_energy(potential_energy)
