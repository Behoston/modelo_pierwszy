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
        id = str(self.id).ljust(5)
        name = 'C   '
        altLoc = ' '
        resName = 'GLY'
        chain = 'A'
        x = str(round(self.coordinates[0], 5))[:8].ljust(8)
        y = '0'.ljust(8)
        z = '0'.ljust(8)
        if self.dim > 1:
            y = str(round(self.coordinates[1], 8))[:8].ljust(8)
            if self.dim > 2:
                z = str(round(self.coordinates[2], 8))[:8].ljust(8)
        occupancy = ' ' * 6
        tempFactor = ' ' * 6
        element = ' C'
        charge = '0 '
        return 'ATOM  ' + id + name + altLoc + resName + chain + x + y + z + occupancy + tempFactor + element + charge
