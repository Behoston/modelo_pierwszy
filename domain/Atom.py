# coding=utf8
from copy import copy

from domain.Vector import Vector


class Atom:
    mass = 1.0
    id = -1

    def __init__(self, dim=3, velocity=None, coordinates=None, acceleration=None, het=True):
        Atom.id += 1
        self.het = het
        self.id = Atom.id
        self.dim = dim
        self.velocity = velocity
        if self.velocity is None:
            self.velocity = Vector.zero(dim)
        self.coordinates = coordinates
        if self.coordinates is None:
            self.coordinates = Vector.zero(dim)
        if self.coordinates.dim > self.dim:
            self.coordinates = Vector(self.coordinates.v[:self.dim])
        self.coordinates_minus_1 = copy(coordinates)
        self.acceleration = acceleration
        if self.acceleration is None:
            self.acceleration = Vector.zero(dim)
        self.acceleration_minus_1 = Vector.zero(dim)
        self.kinetic_energy = (self.velocity.length() * self.mass) ** 2
        self.potential_energy = 0.0

    def __str__(self):
        return 'Atom(\n\tdim=' + str(self.dim) + ', \n\tvelocity=' + str(
            self.velocity) + ', \n\tcoordinates=' + \
               str(self.coordinates) + ', \n\tacceleration=' + str(
            self.acceleration) + '\n)'

    def __repr__(self):
        return 'Atom[' + str(self.id) + ']'

    def __eq__(self, other):
        if not isinstance(other, Atom):
            return False
        return self.id == other.id

    def prepare_for_new_step(self):
        self.acceleration_minus_1 = self.acceleration
        self.acceleration = Vector.zero(self.dim)
        self.potential_energy = 0.0

    def change_acc(self, force):
        self.acceleration += (1.0 / self.mass) * force

    def add_potential_energy(self, potential_energy):
        self.potential_energy += potential_energy

    def move(self, new_velocity, new_coordinates):
        self.coordinates_minus_1 = copy(self.coordinates)
        self.coordinates = new_coordinates
        self.velocity = new_velocity

    def to_pdb_line(self):
        if not self.het:
            section = 'ATOM'.ljust(6)  # 1-6
        else:
            section = 'HETATM'.ljust(6)  # 1-6
        id = str(self.id).rjust(5)  # 7-11
        space1 = ''.rjust(1)  # 12
        name = ' C'.ljust(4)  # 13-16
        altLoc = ''.rjust(1)  # 17
        resName = 'GLY'.rjust(3)  # 18-20
        space2 = ''.rjust(1)  # 21
        chain = 'A'.rjust(1)  # 22
        resSeq = str(self.id).rjust(4)  # 23-26
        iCode = ''.rjust(1)  # 27
        space3 = ''.rjust(3)  # 28-30
        x = str(round(self.coordinates[0], 5))[:8].rjust(8)  # 31-38
        y_value = 0.0
        z_value = 0.0
        if self.dim >= 2:
            y_value = self.coordinates[1]
            if self.dim == 3:
                z_value = self.coordinates[2]
        y = str(round(y_value, 5))[:8].rjust(8)  # 39-46
        z = str(round(z_value, 5))[:8].rjust(8).rjust(8)  # 47-54
        occupancy = ''.rjust(6)  # 55-60
        tempFactor = ''.rjust(6)  # 61-66
        space4 = ''.rjust(10)  # 67-76
        element = 'C'.rjust(2)  # 77-78
        charge = '0'.rjust(2)  # 79-80
        return section + id + space1 + name + altLoc + resName + space2 + \
               chain + resSeq + iCode + space3 + x + y + z \
               + occupancy + tempFactor + space4 + element + charge
