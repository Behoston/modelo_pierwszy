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
        self.coordinates_minus_1 = Vector([0 for i in xrange(dim)])
        self.coordinates_minus_2 = Vector([0 for i in xrange(dim)])
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

    def change_acc(self, force, time):
        self.acceleration = (1 / self.mass) * force
        self.velocity += self.acceleration * time
