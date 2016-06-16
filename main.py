# coding=utf8
import ConfigParser
import argparse

from domain.Simulation import Simulation
from functions.config_helper import *
from functions.drawing import draw

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('config', help='Configuration file')
args = argument_parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)

dimension = get_dimension(config)
steps = get_steps(config)
step_time = get_step_time(config)
spf = get_steps_per_frame(config)
output_dir = get_output_dir(config)
spe = get_steps_per_energy_dump(config)
algorithm = get_algorithm(config)
force_fields = get_force_fields(config)
atoms = get_atoms(config, dimension)

s = Simulation(atoms, steps=steps, step_time=step_time, dim=dimension, save_step=spf, output=output_dir,
               save_energy_step=spe)
s.set_algorithm(algorithm)
for force_field in force_fields:
    s.add_force_field(force_field)
s.run()
draw('./output/' + output_dir)
