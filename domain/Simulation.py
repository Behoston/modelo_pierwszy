# coding=utf8
from domain.forcefield.SoftWall import SoftWall
from domain.algorithm.Verlet import Verlet

from domain.Vector import Vector


class Simulation:
    def __init__(self, atoms, steps=1000, step_time=0.001, dim=3, save_step=10):
        self.atoms_count = len(atoms)
        self.atoms = atoms
        self.steps = steps
        self.save_step = save_step
        self.force_fields = []
        self.algorithm = Verlet()
        self.dim = dim
        self.dump_file = './output/simulation.pdb'
        with open(self.dump_file, 'w'):
            # czuszczenie pliku przed kolejną symulacją
            pass
        self.step_time = step_time

    def add_force_field(self, force_filed=SoftWall()):
        self.force_fields.append(force_filed)

    def set_algorithm(self, algorithm=Verlet()):
        self.algorithm = algorithm

    def __repr__(self):
        return 'Simulation(' + str(self.atoms_count) + ', ' + str(
            self.force_fields) + ')'

    def __str__(self):
        s = 'Simulation(' + str(self.atoms_count) + ')['
        for a in self.atoms:
            s += '\n\t' + str(a)
        s += '\n]'
        return s

    def dump(self, step):
        with open(self.dump_file, 'a') as plik:
            plik.write('MODEL ' + str(step / self.save_step + 1) + '\n')
            for atom in self.atoms:
                plik.write(atom.to_pdb_line() + '\n')
            plik.write('TER\n')

    def initialize(self):
        with open(self.dump_file, 'a') as plik:
            plik.write('MODEL 0\n')
            for atom in self.atoms:
                plik.write(atom.to_pdb_line() + '\n')
            plik.write('TER\n')
        for atom in self.atoms:
            atom.acceleration = Vector.zero(self.dim)

    def run(self):
        if len(self.force_fields) == 0:
            raise Exception('Please setup force field first')
        self.initialize()
        for step in xrange(self.steps):
            for atom in self.atoms:
                atom.prepare_for_new_step()
            for force_field in self.force_fields:
                for a1 in xrange(len(self.atoms)):
                    force_field.single_atom_contribution(self.atoms[a1])
                    if force_field.how_many_atoms_contribution() >= 2:
                        for a2 in xrange(len(self.atoms)):
                            if a1 < a2:
                                force_field.pair_atoms_contribution(self.atoms[a1], self.atoms[a2])
                                if force_field.how_many_atoms_contribution() == 3:
                                    for a3 in xrange(len(self.atoms)):
                                        if a3 < a2 and a3 < a1:
                                            force_field.three_atoms_contribution(
                                                self.atoms[a1], self.atoms[a2], self.atoms[a3])
            self.algorithm.make_step(self.atoms, self.step_time)
            if step % self.save_step == 0:
                self.dump(step)
