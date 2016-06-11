# coding=utf-8
from domain.Atom import Atom
from domain.Vector import Vector


def pdb_file_to_atoms(file, dim=3):
    atoms = []
    f = open(file)
    for line in f.readlines():
        hetatm = line[:6] == 'HETATM'
        if line[:4] == 'ATOM' or hetatm:
            x = float(line[31:38])
            y = float(line[39:46])
            z = float(line[47:54])
            atom = Atom(dim, coordinates=Vector([x, y, z]), het=hetatm)
            atom.coordinates_minus_1 = atom.coordinates - 0.01
            atoms.append(atom)
    f.close()
    return atoms
