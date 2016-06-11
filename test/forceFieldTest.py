# coding=utf-8
import unittest

from domain.Atom import Atom
from domain.forcefield.MinimumBarrierMinimum import MinimumBarrierMinimum


class ForceFieldTest(unittest.TestCase):
    def testMBM(self):
        atom = Atom()
        mbm = MinimumBarrierMinimum()
        mbm.single_atom_contribution(atom)
