# coding=utf-8
from domain.Atom import Atom
from domain.Vector import Vector
from domain.algorithm.LeapFrog import LeapFrog
from domain.algorithm.VelocityVerlet import VelocityVerlet
from domain.algorithm.Verlet import Verlet
from domain.forcefield.LenardJones import LenardJones
from domain.forcefield.MinimumBarrierMinimum import MinimumBarrierMinimum
from domain.forcefield.SoftWall import SoftWall
from functions.PdbHelper import pdb_file_to_atoms


def get_force_fields(config):
    print 'FORCE FIELDS'
    force_fields = []
    ff1_class = config.get('force_fields', 'force_field_1')
    ff1 = get_force_field(ff1_class, config, 1)
    force_fields.append(ff1)
    try:
        ff2_class = config.get('force_fields', 'force_field_2')
        if ff2_class:
            ff2 = get_force_field(ff2_class, config, 2)
            force_fields.append(ff2)
    except:
        pass
    try:
        ff3_class = config.get('force_fields', 'force_field_3')
        if ff3_class:
            ff3 = get_force_field(ff3_class, config, 3)
            force_fields.append(ff3)
    except:
        pass
    return force_fields


def get_force_field_from_string(force_field_name):
    force_field_name = force_field_name.upper()
    ff = [MinimumBarrierMinimum, LenardJones, SoftWall]
    for f in ff:
        if f.__name__.upper() == force_field_name:
            return f


def get_force_field(force_field, config, number):
    if force_field.upper() == 'SOFTWALL':
        return get_soft_wall(config, number)
    elif force_field.upper() == 'LENARDJONES':
        return get_lenard_jones(config, number)
    elif force_field.upper() == 'MINIMUMBARRIERMINIMUM':
        return get_minimum_barrier_minimum(config, number)
    raise Exception('Not supported force field')


def get_soft_wall(config, number):
    print '\tUsing Soft Wall'
    number = str(number)
    size = 5.0
    try:
        size = config.getfloat('force_fields',
                               'force_field_' + number + '_size')
    except:
        pass
    f = 1.0
    try:
        f = config.getfloat('force_fields', 'force_field_' + number + '_f')
    except:
        pass
    return SoftWall(size, f)


def get_minimum_barrier_minimum(config, number):
    print '\tUsing Minimum Barrier Minimum'
    number = str(number)
    a = 5.0
    b = 10.0
    c = 3.0
    d = 0.02
    try:
        a = config.getfloat('force_fields', 'force_field_' + number + '_a')
    except:
        pass
    try:
        b = config.getfloat('force_fields', 'force_field_' + number + '_b')
    except:
        pass
    try:
        c = config.getfloat('force_fields', 'force_field_' + number + '_c')
    except:
        pass
    try:
        d = config.getfloat('force_fields', 'force_field_' + number + '_d')
    except:
        pass
    return MinimumBarrierMinimum(a, b, c, d)


def get_lenard_jones(config, number):
    print '\tUsing Lenard Jones'
    number = str(number)
    R = 1.0
    epsilon = 1.0
    try:
        R = config.getfloat('force_fields', 'force_field_' + number + '_R')
    except:
        pass
    try:
        epsilon = config.gefloat('force_fields',
                                 'force_field_' + number + '_epsilon')
    except:
        pass
    return LenardJones(R, epsilon)


def get_algorithm(config):
    print 'ALGORITHM'
    try:
        algorithm__name = config.get('main', 'algorithm').upper()
    except:
        # default
        print '\tUsing default Verlet'
        return Verlet()
    if algorithm__name == 'VERLET':
        print '\tUsing Verlet'
        return Verlet()
    elif algorithm__name == 'VELOCITY_VERLET' or algorithm__name == 'VELOCITYVERLET':
        print '\tUsing Velocity Verlet'
        return VelocityVerlet()
    elif algorithm__name == 'LEAP_FROG' or algorithm__name == 'LEAPFROG':
        print '\tUsing Leap Frog'
        return LeapFrog()
    else:
        # default
        print '\tUnrecognized algorithm, using Verlet'
        return Verlet()


def get_atoms(config, dimension):
    try:
        input_file = config.get('main', 'input_file')
        return pdb_file_to_atoms(input_file, dimension)
    except:
        number_of_atoms = config.getint('main', 'number_of_atoms')
        return [Atom(dim=dimension, coordinates=Vector.random(dimension) * 10) for _ in xrange(number_of_atoms)]


def get_dimension(config):
    return config.getint('main', 'dimension')


def get_steps(config):
    return config.getint('main', 'steps')


def get_step_time(config):
    return config.getfloat('main', 'step_time')


def get_steps_per_frame(config):
    return config.getint('output', 'spf')


def get_output_dir(config):
    return config.get('output', 'output_dir')


def get_steps_per_energy_dump(config):
    try:
        spe = config.getint('output', 'spe')
    except:
        spe = 1
    return spe
