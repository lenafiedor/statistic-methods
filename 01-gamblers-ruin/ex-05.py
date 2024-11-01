import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    # set initial capitals and define probabilities
    a_initial = 50
    b_initial = 50
    p_values = [0.2, 0.5]

    # retrieve mean game lenghts for the given probabilities
    mean_game_lengths = [estimate_game_length(NUM_GAMES_LONG, a_initial, b_initial, p)[1] for p in p_values]

    # create an array containing two tuples of three cases of game length for which the distribution will be generated
    n_values = [(10, int(mean / 2), int(mean * 0.9)) for mean in mean_game_lengths]

    final_capitals = estimate_capital_distribution(NUM_GAMES_LONG, a_initial, b_initial, n_values, p_values)

    # plot the histgograms
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Distribution of the final capital of player A for different probabilities (p) and game counts (n)', fontsize=16)
    colors = ['#A88C8C', '#82799B']

    for i, p in enumerate(p_values):
        for j, n in enumerate(n_values[i]):
            ax = axes[i, j]
            ax.hist(final_capitals[i][j], bins=50, alpha=0.7, color=colors[i], edgecolor='black', density=True)
            ax.set_title(f'p = {p}, n = {n}')
            ax.set_xlabel('Final Capital')
            ax.set_ylabel('Probability')
            ax.text(0.95, 0.95, f'Mean: {int(np.mean(final_capitals[i][j]))}', 
                transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.3', alpha=0.8))

    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
    plt.savefig('./images/ex-05')
