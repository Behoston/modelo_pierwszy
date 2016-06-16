# coding=utf8
import matplotlib.pyplot as plt


def draw_potential_energy_plot(steps, potential_energy, output_dir):
    plt.title('Potential energy')
    plt.ylabel('potential energy')
    plt.xlabel('step')
    plt.grid(True),
    plt.plot(steps, potential_energy, color='blue', label='Potential Energy')
    # plt.savefig(output_dir + '/potential_energy.png')
    # plt.close()


def draw_kinetic_energy_plot(steps, kinetic_energy, output_dir):
    plt.title('Kinetic energy')
    plt.ylabel('kinetic energy')
    plt.xlabel('step')
    plt.grid(True),
    plt.plot(steps, kinetic_energy, color='red', label='Kinetic Energy')
    # plt.savefig(output_dir + '/kinetic_energy.png')
    # plt.close()


def draw_energy_plot(steps, energy, output_dir):
    plt.title('Energy')
    plt.ylabel('energy')
    plt.xlabel('step')
    plt.grid(True),
    plt.plot(steps, energy, color='green', label='Energy')
    # plt.savefig(output_dir + '/energy.png')
    # plt.close()


def draw(input_dir):
    steps = []
    potential_energy = []
    kinetic_energy = []
    energy = []
    potential_energy_file = open(input_dir + '/potential_energy.csv')
    kinetic_energy_file = open(input_dir + '/kinetic_energy.csv')
    for p_e_l in potential_energy_file:
        p_e_l = p_e_l.strip().split(',')
        s = int(p_e_l[0])
        p_e = float(p_e_l[1])
        k_e = float(kinetic_energy_file.readline().strip().split(',')[1])
        e = p_e + k_e
        steps.append(s)
        potential_energy.append(p_e)
        kinetic_energy.append(k_e)
        energy.append(e)
    potential_energy_file.close()
    kinetic_energy_file.close()

    draw_potential_energy_plot(steps, potential_energy, input_dir)
    draw_kinetic_energy_plot(steps, kinetic_energy, input_dir)
    draw_energy_plot(steps, energy, input_dir)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, shadow=True, ncol=5)
    plt.savefig(input_dir + '/energy.png')
    plt.close()
