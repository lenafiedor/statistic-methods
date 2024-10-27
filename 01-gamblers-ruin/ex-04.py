import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    NUM_GAMES = 100

    a_initial = 50
    b_initial = 50
    p_values = np.arange(0.0, 1.1, 0.1)

    # run the simulation (averaging over 100 games)
    mean_lengths = [estimate_game_length(NUM_GAMES, a_initial, b_initial, p)[1] for p in p_values]

    # plot the probabilites
    plt.figure(figsize=(12, 6))
    
    plt.plot(p_values, mean_lengths, marker='o', color='#A88C8C')

    plt.xlabel('Probability value (p)')
    plt.ylabel('Game length (number of rounds)')
    plt.grid()
    plt.title(f'Average number of rounds over p probability ({NUM_GAMES} games)')

    plt.savefig('./images/ex-04')
