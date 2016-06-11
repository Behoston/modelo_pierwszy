# coding=utf8
import ConfigParser

import argparse

from domain.Simulation import Simulation
from functions.PdbHelper import pdb_file_to_atoms
from functions.config_helper import get_force_fields, get_algorithm

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('config', help='Configuration file')
args = argument_parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)

dimension = config.getint('main', 'dimension')
# number_of_atoms = config.getint('main', 'number_of_atoms')
steps = config.getint('main', 'steps')
step_time = config.getfloat('main', 'step_time')
spf = config.getint('main', 'spf')
input_file = config.get('main', 'input_file')

atoms = pdb_file_to_atoms(input_file, dimension)
isinstance('s', float)
s = Simulation(atoms, steps=steps, step_time=step_time, dim=dimension, save_step=spf)
algorithm = get_algorithm(config)
s.set_algorithm(algorithm)
force_fields = get_force_fields(config)
for force_field in force_fields:
    s.add_force_field(force_field)
s.run()
