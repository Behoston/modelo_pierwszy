# coding=utf8
import os
from copy import copy

from domain.algorithm.Verlet import Verlet
from domain.forcefield.LenardJones import LenardJones
from domain.forcefield.SoftWall import SoftWall


class Simulation:
    def __init__(self, atoms, output, steps=1000, step_time=0.001, dim=3, save_step=10, save_energy_step=1):
        self.atoms_count = len(atoms)
        self.atoms = atoms
        self.steps = steps
        self.save_step = save_step
        self.save_energy_step = save_energy_step
        self.force_fields = []
        self.algorithm = Verlet()
        self.dim = dim
        self.output = output
        self.trajectory_file = './output/' + self.output + '/simulation.pdb'
        self.potential_energy_file = './output/' + self.output + '/potential_energy.csv'
        self.kinetic_energy_file = './output/' + self.output + '/kinetic_energy.csv'
        self.step_time = step_time

    def add_force_field(self, force_filed=SoftWall()):
        self.force_fields.append(force_filed)
        if isinstance(force_filed, LenardJones):
            for i in xrange(1, self.atoms_count):
                self.atoms[i].coordinates = self.atoms[i - 1].coordinates - 1.0
                self.atoms[i].coordinates_minus_1 = copy(self.atoms[i].coordinates)

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
        identifier = str(step / self.save_step + 1)
        with open(self.trajectory_file, 'a') as plik:
            plik.write('MODEL ' + identifier + '\n')
            for atom in self.atoms:
                plik.write(atom.to_pdb_line() + '\n')
            plik.write('TER\n')

    def dump_energy(self, step):
        identifier = str(step / self.save_energy_step + 1)
        potential_energy = 0
        kinetic_energy = 0
        for atom in self.atoms:
            potential_energy += atom.potential_energy
            kinetic_energy += atom.get_kinetic_energy()
        with open(self.kinetic_energy_file, 'a') as f:
            f.write(identifier + ',' + str(kinetic_energy) + '\n')
        with open(self.potential_energy_file, 'a') as f:
            f.write(identifier + ',' + str(potential_energy) + '\n')

    def initialize(self):
        """
        Saving initial state (clears previous files)
        and creating output dir
        """
        try:
            os.makedirs('./output/' + self.output)
        except:
            pass
        with open(self.trajectory_file, 'w') as f:
            f.write('MODEL 0\n')
            for atom in self.atoms:
                f.write(atom.to_pdb_line() + '\n')
            f.write('TER\n')
        potential_energy = 0
        kinetic_energy = 0
        for atom in self.atoms:
            potential_energy += atom.potential_energy
            kinetic_energy += atom.get_kinetic_energy()
        with open(self.kinetic_energy_file, 'w') as f:
            f.write('0,' + str(kinetic_energy) + '\n')
        with open(self.potential_energy_file, 'w') as f:
            f.write('0,' + str(potential_energy) + '\n')

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
            if step % self.save_energy_step == 0:
                self.dump_energy(step)
            if step % self.save_step == 0:
                self.dump(step)
