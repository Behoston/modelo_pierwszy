# coding=utf8
import ConfigParser

import argparse

from domain.Simulation import Simulation
from functions.PdbHelper import pdb_file_to_atoms
from functions.config_helper import get_force_field_form_string

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('config', help='Configuration file')
args = argument_parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)

dimension = config.getint('main', 'dimension')
number_of_atoms = config.getint('main', 'number_of_atoms')
steps = config.getint('main', 'steps')
force_field = config.get('main', 'force_field')
step_time = config.getfloat('main', 'step_time')
spf = config.getint('main', 'spf')
atoms = pdb_file_to_atoms('input/input.pdb')

s = Simulation(atoms, steps=steps, step_time=step_time, dim=dimension, save_step=spf)
s.set_force_field(get_force_field_form_string(force_field))
s.run()
