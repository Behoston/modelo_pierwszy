# coding=utf-8
from domain.MinimumBarierMinimum import MinimumBarierMinimum
from domain.SoftWall import SoftWall

from domain.forcefield.LenardJones import LenardJones


def get_force_field_form_string(force_field_name):
    force_field_name = force_field_name.upper()
    ff = [MinimumBarierMinimum, LenardJones, SoftWall]
    for f in ff:
        if f.__name__.upper() == force_field_name:
            return f()
