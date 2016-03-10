# coding=utf8


class ForceField:
    def __init__(self, time=0.0001):
        self.time = time

    def single_atom_contribution(self, atom):
        pass

    def pair_atoms_contribution(self, atom1, atom2):
        pass

    def three_atoms_contribution(self, atom1, atom2, atom3):
        pass
