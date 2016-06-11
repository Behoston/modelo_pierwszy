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
        self.max_distance = 2

    def how_many_atoms_contribution(self):
        return 2

    def pair_atoms_contribution(self, atom1, atom2):
        distance = (atom1.coordinates - atom2.coordinates).length()
        if distance < self.max_distance and distance != 0:
            potential_energy = self.epsilon * ((self.R / distance) ** 12 - 2 * (self.R / distance) ** 6)
            force = []
            for i in xrange(atom1.dim):
                dist = fabs(atom1.coordinates[i] - atom2.coordinates[i])
                if dist == 0:
                    f = 0
                else:
                    f = 12 * self.R6 * self.epsilon * (dist ** 6 - self.R6) / dist
                force.append(f)
            atom1.change_acc(Vector(force))
            atom2.change_acc(Vector([-x for x in force]))
            atom1.add_potential_energy(potential_energy)
            atom2.add_potential_energy(potential_energy)
