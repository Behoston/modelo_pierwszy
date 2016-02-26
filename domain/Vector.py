# coding=utf-8
from random import random


class Vector:
    def __init__(self, values):
        if values is None:
            self.dim = 0
            self.v = []
        elif isinstance(values, list):
            self.dim = len(values)
            self.v = values
        else:
            self.v = [values]
            self.dim = 1

    def __add__(self, other):
        result = []
        if isinstance(other, Vector):
            if self.dim == other.dim:
                if self.dim == 0:
                    return self
                for i in xrange(len(self.v)):
                    result.append(self.v[i] + self.v[i])
            else:
                raise Exception('Different dimension of vectors!')
        elif isinstance(other, int) or isinstance(other, float):
            for i in self.v:
                l = []
                isinstance(l, list)
                result.append(i + other)
        else:
            raise Exception('Don`t known type of other')
        return Vector(result)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        if self.dim != other.dim:
            return False
        for i in xrange(self.dim):
            if self.v[i] != other.v[i]:
                return False
        return True

    def __str__(self):
        return '[' + str(self.dim) + ']Vector(' + str(self.v) + ')'

    def __repr__(self):
        return 'Vector(' + str(self.v) + ')'

    def __iter__(self):
        return self.v.__iter__()

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = 0.0
            for i in xrange(self.dim):
                result += self.v[i] * other.v[i]
            return result
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([x * other for x in self])

    def wersor(self):
        length = self.length()
        return Vector([x / length for x in self])

    def length(self):
        result = 0.0
        for x in self.v:
            result += x ** 2
        return result ** 0.5

    @staticmethod
    def random(dim):
        return Vector([random() for i in xrange(dim)])


x = Vector([1, 2, 3])
y = Vector([1, 2, 3])
print x.wersor()
# print Vector.random(15).length()
# print x == y
print x * y
