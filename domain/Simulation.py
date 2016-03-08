# coding=utf8
from domain.Atom import Atom


class Simulation:
    def __init__(self, atoms_count=10):
        self.atoms_count = atoms_count
        self.atoms = [Atom(dim=3) for i in xrange(self.atoms_count)]

    def __repr__(self):
        return 'Simulation(' + str(self.atoms_count) + ')'

    def __str__(self):
        s = 'Simulation(' + str(self.atoms_count) + ')['
        for a in self.atoms:
            s += '\n\t' + str(a)
        s += '\n]'
        return s


s = Simulation()
print s
