# coding=utf8
from domain.Vector import Vector


class Atom:
    mass = 1.0
    id = -1

    def __init__(self, dim=3, velocity=None, coordinates=None, acceleration=None):
        Atom.id += 1
        self.id = Atom.id
        self.dim = dim
        self.velocity = velocity
        if self.velocity is None:
            self.velocity = Vector.random(dim)
        self.coordinates = coordinates
        if coordinates is None:
            self.coordinates = Vector.random(dim) * 10
        self.coordinates_minus_1 = Vector.zero(self.dim)
        self.coordinates_minus_2 = Vector.zero(self.dim)
        self.acceleration = acceleration
        if self.acceleration is None:
            self.acceleration = Vector.random(dim)
        self.kinetic_energy = (self.velocity.length() * self.mass) ** 2
        self.potential_energy = 0.0

    def __str__(self):
        return 'Atom(\n\tdim=' + str(self.dim) + ', \n\tvelocity=' + str(self.velocity) + ', \n\tcoordinates=' + \
               str(self.coordinates) + ', \n\tacceleration=' + str(self.acceleration) + '\n)'

    def __repr__(self):
        return 'Atom[' + str(self.id) + ']'

    def __eq__(self, other):
        if not isinstance(other, Atom):
            return False
        return self.id == other.id

    def prepare_for_new_step(self):
        self.acceleration = Vector.zero(self.dim)
        self.potential_energy = 0.0

    def change_acc(self, force, potential_energy):
        self.acceleration = (1.0 / self.mass) * force
        self.potential_energy += potential_energy

    def move(self, time):
        self.velocity += self.acceleration * time
        self.coordinates_minus_2 = self.coordinates_minus_1
        self.coordinates_minus_1 = self.coordinates
        self.coordinates += self.velocity * time
        self.kinetic_energy = (self.velocity.length() * self.mass) ** 2

    def to_pdb_line(self):
        section = 'ATOM'.ljust(6)  # 1-6
        id = str(self.id).rjust(5)  # 7-11
        space1 = ''.rjust(1)  # 12
        name = ' C'.ljust(4)  # 13-16
        altLoc = ''.rjust(1)  # 17
        resName = 'GLY'.rjust(3)  # 18-20
        space2 = ''.rjust(1)  # 21
        chain = 'A'.rjust(1)  # 22
        resSeq = '1'.rjust(4)  # 23-26
        iCode = ''.rjust(1)  # 27
        space3 = ''.rjust(3)  # 28-30
        x = str(round(self.coordinates[0], 5))[:8].rjust(8)  # 31-38
        y = '0'.rjust(8)  # 39-46
        z = '0'.rjust(8)  # 47-54
        if self.dim > 1:
            y = str(round(self.coordinates[1], 8))[:8].rjust(8)
            if self.dim > 2:
                z = str(round(self.coordinates[2], 8))[:8].rjust(8)
        occupancy = ''.rjust(6)  # 55-60
        tempFactor = ''.rjust(6)  # 61-66
        space4 = ''.rjust(10)  # 67-76
        element = 'C'.rjust(2)  # 77-78
        charge = '0'.rjust(2)  # 79-80
        return section + id + space1 + name + altLoc + resName + space2 + chain + resSeq + iCode + space3 + x + y + z \
               + occupancy + tempFactor + space4 + element + charge
