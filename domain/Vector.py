# coding=utf-8
from copy import copy
from random import random

from functions.all import isnumeric


class Vector:
    def __init__(self, values=None):
        if values is None:
            self.dim = 0
            self.v = []
        elif isinstance(values, list):
            self.dim = len(values)
            self.v = values
        else:
            self.v = [values]
            self.dim = 1

    def __getitem__(self, item):
        return self.v.__getitem__(item)

    def __add__(self, other):
        result = []
        if isinstance(other, Vector):
            if self.dim == other.dim:
                if self.dim == 0:
                    return self
                for i in xrange(len(self.v)):
                    result.append(self.v[i] + other.v[i])
            else:
                raise Exception('Different dimension of vectors!')
        elif isnumeric(other):
            for i in self.v:
                result.append(i + other)
        else:
            raise Exception('Don`t known type of other')
        return Vector(result)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        result = []
        if isinstance(other, Vector):
            if self.dim == other.dim:
                if self.dim == 0:
                    return self
                for i in xrange(len(self.v)):
                    result.append(self.v[i] - other.v[i])
            else:
                raise Exception('Different dimension of vectors!')
        elif isnumeric(other):
            for i in self.v:
                result.append(i - other)
        else:
            raise Exception('Don`t known type of other')
        return Vector(result)

    def __rsub__(self, other):
        return self - other

    def __div__(self, other):
        if isnumeric(other):
            l = []
            for i in self.v:
                l.append((i + 0.0) / other)
            return Vector(l)
        raise Exception('Divide operation allowed only by numeric')

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
        elif isnumeric(other):
            return Vector([x * other for x in self])

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power, modulo=None):
        result = Vector(copy(self.v))
        if isinstance(power, int):
            for i in xrange(power - 1):
                result *= self
        return result

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

    @staticmethod
    def zero(dim):
        return Vector([0 for i in xrange(dim)])
