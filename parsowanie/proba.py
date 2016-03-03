# coding=utf-8
import ConfigParser

import argparse

parser = argparse.ArgumentParser(description='Jakiś parser')
parser.add_argument("-n", type=int)
parser.add_argument("config", type=str)

args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config)

print args
