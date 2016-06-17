# coding=utf8
from domain.forcefield.ForceField import ForceField


class LenardJones(ForceField):
    def __init__(self, R=1.0, epsilon=1.0):
        ForceField.__init__(self)
        self.R = R
        self.R6 = R ** 6
        self.R12 = R ** 12
        self.epsilon = epsilon

    def how_many_atoms_contribution(self):
        return 2

    def pair_atoms_contribution(self, atom1, atom2):
        distance = (atom1.coordinates - atom2.coordinates).length()

        first = self.R12 / distance ** 12
        second = 2 * self.R6 / distance ** 6
        potential_energy = self.epsilon * (first - second)

        force = -12 * self.epsilon * self.R6 * (self.R6 - distance ** 6) / distance ** 13

        atom1.change_acc((atom2.coordinates - atom1.coordinates).wersor() * force)
        atom2.change_acc((atom1.coordinates - atom2.coordinates).wersor() * force)
        atom1.add_potential_energy(potential_energy / 2)
        atom2.add_potential_energy(potential_energy / 2)

    def __str__(self):
        return "Stachu Dżones :V"
