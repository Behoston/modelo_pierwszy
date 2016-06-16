# coding=utf8
from domain.Vector import Vector
from domain.forcefield.ForceField import ForceField


class SoftWall(ForceField):
    def __init__(self, size=5.0, f=1.0):
        ForceField.__init__(self)
        if size is None:
            size = 5.0
        if f is None:
            f = 1.0
        self.L = size
        self.f = f

    def how_many_atoms_contribution(self):
        return 1

    def single_atom_contribution(self, atom):
        potential_energy = 0.0
        force = []
        distance = atom.coordinates.length()
        calculate_potential_energy = False
        for coord in atom.coordinates:
            abs_coord = abs(coord)
            if abs_coord > self.L:
                calculate_potential_energy = True
                potential_energy += 0.5 * self.f * (self.L - abs_coord) ** 2
                force.append(self.f * coord * (self.L - abs_coord) / abs(coord))
            # elif coord < - self.L:
            #     calculate_potential_energy = True
            #     force.append(-self.f * coord * (1 - self.L / distance))
            #     potential_energy += 0.5 * self.f * (self.L + coord) ** 2
            else:
                force.append(0.0)
        # if calculate_potential_energy:
        #     potential_energy = 0.5 * self.f * (self.L - distance) ** 2
        atom.add_potential_energy(potential_energy)
        atom.change_acc(Vector(force))
