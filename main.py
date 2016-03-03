# coding=utf8
import ConfigParser

import argparse

from domain.Vector import Vector

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('config', help='Configuration file')
args = argument_parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)
dimension = config.getint('main', 'dimension')

v = Vector.random(dimension)
print v
