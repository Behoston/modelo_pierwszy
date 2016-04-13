# coding=utf8
from domain.Atom import Atom
from domain.ForceField import ForceField
from domain.Integrator import Integrator
from domain.SoftWall import SoftWall
from time import time

from domain.Vector import Vector
from domain.Verlet import Verlet


class Simulation:
    def __init__(self, atoms, steps=1000, step_time=0.001, dim=3, save_step=10):
        self.atoms_count = len(atoms)
        self.atoms = atoms
        self.steps = steps
        self.save_step = save_step
        self.force_field = ForceField()
        self.algorithm = Verlet()
        self.dim = dim
        self.dump_file = './output/simulation_.pdb'
        self.step_time = step_time

    def set_force_field(self, force_filed=SoftWall()):
        self.force_field = force_filed

    def set_algorithm(self, algorithm=Verlet()):
        self.algorithm = algorithm

    def __repr__(self):
        return 'Simulation(' + str(self.atoms_count) + ', ' + self.force_field.__name__ + ')'

    def __str__(self):
        s = 'Simulation(' + str(self.atoms_count) + ')['
        for a in self.atoms:
            s += '\n\t' + str(a)
        s += '\n]'
        return s

    def dump(self, step):
        with open(self.dump_file, 'a') as plik:
            plik.write('MODEL ' + str(step / self.save_step) + '\n')
            for atom in self.atoms:
                plik.write(atom.to_pdb_line() + '\n')
            plik.write('TER\n')

    def initialize(self):
        for atom in self.atoms:
            atom.acceleration = Vector.random(self.dim) * 10000

    def run(self):
        if self.force_field is None:
            raise Exception('Please setup force field first')
        self.initialize()
        for step in xrange(self.steps):
            for atom in self.atoms:
                atom.prepare_for_new_step()
            for atom1 in self.atoms:
                self.force_field.single_atom_contribution(atom1)
                for atom2 in self.atoms:
                    if atom1 != atom2:
                        self.force_field.pair_atoms_contribution(atom1, atom2)
                        for atom3 in self.atoms:
                            if atom3 != atom2 and atom3 != atom1:
                                self.force_field.three_atoms_contribution(atom1, atom2, atom3)
            self.algorithm.make_step(self.atoms, self.step_time)
            if step % self.save_step == 0:
                self.dump(step)
