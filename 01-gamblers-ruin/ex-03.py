import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    a_initial = 50
    b_initial = 50
    p_values = [0.2, 0.5, 0.8]

    # run the short simulation (averaging over 10 games)
    num_rounds_mean_short = []
    num_rounds_stdev_short = []
    
    for p in p_values:
        mean_length, stdev_length = estimate_game_length(NUM_GAMES_SHORT, a_initial, b_initial, p)
        num_rounds_mean_short.append(mean_length)
        num_rounds_stdev_short.append(stdev_length)

    # run the long simulation (averaging over 1000 games)
    num_rounds_mean_long = []
    num_rounds_stdev_long = []

    for p in p_values:
        mean_length, stdev_length = estimate_game_length(NUM_GAMES_LONG, a_initial, b_initial, p)
        num_rounds_mean_long.append(mean_length)
        num_rounds_stdev_long.append(stdev_length)

    # plot the probabilites
    plt.errorbar(p_values, num_rounds_mean_short, yerr=num_rounds_stdev_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C', capsize=5)
    plt.errorbar(p_values, num_rounds_mean_long, yerr=num_rounds_stdev_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B', capsize=5)

    plt.xlabel('Probability value (p)')
    plt.ylabel('Game length (number of rounds)')
    plt.legend()
    plt.grid()
    plt.title('Average number of rounds over p probability')

    plt.savefig('./images/ex-03')
