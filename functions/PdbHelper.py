# coding=utf-8
from domain.Atom import Atom
from domain.Vector import Vector


def pdb_file_to_atoms(file):
    atoms = []
    f = open(file)
    for line in f.readlines():
        if line[:4] == 'ATOM':
            x = float(line[31:38])
            y = float(line[39:46])
            z = float(line[47:54])
            atom = Atom(3, coordinates=Vector([x, y, z]))
            atom.coordinates_minus_1 = atom.coordinates - 0.01
            atoms.append(atom)
    f.close()
    return atoms
