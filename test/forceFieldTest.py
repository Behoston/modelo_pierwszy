# coding=utf-8
import unittest

from domain.Atom import Atom
from domain.MinimumBarierMinimum import MinimumBarierMinimum


class ForceFieldTest(unittest.TestCase):
    def testMBM(self):
        atom = Atom()
        mbm = MinimumBarierMinimum()
        mbm.single_atom_contribution(atom)
