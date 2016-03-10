# coding=utf8
from domain.Atom import Atom
from domain.SoftWall import SoftWall


class Simulation:
    def __init__(self, atoms_count=10, steps=1000):
        self.atoms_count = atoms_count
        self.atoms = [Atom(dim=3) for i in xrange(self.atoms_count)]
        self.steps = steps
        self.force_field = None

    def set_force_field(self, force_filed=SoftWall()):
        self.force_field = force_filed

    def __repr__(self):
        return 'Simulation(' + str(self.atoms_count) + ', ' + self.force_field.__name__ + ')'

    def __str__(self):
        s = 'Simulation(' + str(self.atoms_count) + ')['
        for a in self.atoms:
            s += '\n\t' + str(a)
        s += '\n]'
        return s

    def run(self):
        if self.force_field is None:
            raise Exception('Please setup force field')
        for step in xrange(self.steps):
            for atom in self.atoms:
                self.force_field.single_atom_contribution(atom)
