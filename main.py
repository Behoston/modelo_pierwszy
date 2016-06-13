# coding=utf8
import ConfigParser

import argparse

from domain.Vector import Vector
from domain.Atom import Atom
from domain.Simulation import Simulation
from functions.PdbHelper import pdb_file_to_atoms
from functions.config_helper import get_force_fields, get_algorithm
from functions.drawing import draw

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('config', help='Configuration file')
args = argument_parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)

dimension = config.getint('main', 'dimension')
try:
    input_file = config.get('main', 'input_file')
    atoms = pdb_file_to_atoms(input_file, dimension)
except:
    number_of_atoms = config.getint('main', 'number_of_atoms')
    atoms = [Atom(dim=dimension, coordinates=Vector.random(dimension) * 10) for _ in xrange(number_of_atoms)]
steps = config.getint('main', 'steps')
step_time = config.getfloat('main', 'step_time')
spf = config.getint('output', 'spf')
output_dir = config.get('output', 'output_dir')
try:
    spe = config.getint('output', 'spe')
except:
    spe = 1
algorithm = get_algorithm(config)
force_fields = get_force_fields(config)

s = Simulation(atoms, steps=steps, step_time=step_time, dim=dimension, save_step=spf, output=output_dir,
               save_energy_step=spe)
s.set_algorithm(algorithm)
for force_field in force_fields:
    s.add_force_field(force_field)
s.run()
draw('./output/' + output_dir)
