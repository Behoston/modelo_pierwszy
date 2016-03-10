# coding=utf8
from domain.ForceField import ForceField


class LenardJones(ForceField):
    def __init__(self, time=0.0001, R=1.0, epsilon=1.0):
        ForceField.__init__(self, time)
        self.R = R
        self.epsilon = epsilon

    def pair_atoms_contribution(self, atom1, atom2):
        distance = (atom1 - atom2).length()
        force = self.epsilon * ((self.R / distance) ** 12 - 2 * (self.R / distance) ** 6)
        atom1.change_acc(force, self.time)
        atom2.change_acc(-force, self.time)
