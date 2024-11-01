import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    a_initial = 50
    b_initial = 50
    p_values = [0.2, 0.5, 0.8]

    # run the short simulation (averaging over 10 games)
    num_rounds_short = []
    num_rounds_mean_short = []
    num_rounds_stdev_short = []
    
    for p in p_values:
        num_rounds, mean_length, stdev_length = estimate_game_length(NUM_GAMES_SHORT, a_initial, b_initial, p)
        num_rounds_short.append(num_rounds)
        num_rounds_mean_short.append(mean_length)
        num_rounds_stdev_short.append(stdev_length)

    # run the long simulation (averaging over 1000 games)
    num_rounds_long = []
    num_rounds_mean_long = []
    num_rounds_stdev_long = []

    for p in p_values:
        num_rounds, mean_length, stdev_length = estimate_game_length(NUM_GAMES_LONG, a_initial, b_initial, p)
        num_rounds_long.append(num_rounds)
        num_rounds_mean_long.append(mean_length)
        num_rounds_stdev_long.append(stdev_length)

    # plot the histograms
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    for ax, p, lengths, mean, stdev in zip(axes[0], p_values, num_rounds_short, num_rounds_mean_short, num_rounds_stdev_short):
        ax.hist(lengths, bins=50, color='#A88C8C', edgecolor='black', alpha=0.7, density=True)
        ax.set_title(f'Short simulation (p = {p})')
        ax.set_xlabel('Game length')
        ax.set_ylabel('Probability')
        ax.text(0.95, 0.95, f'Mean: {mean}\nStd dev: {stdev:.2f}', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.3', alpha=0.8))
        
    for ax, p, lengths, mean, stdev in zip(axes[1], p_values, num_rounds_long, num_rounds_mean_long, num_rounds_stdev_long):
        ax.hist(lengths, bins=50, color='#82799B', edgecolor='black', alpha=0.7, density=True)
        ax.set_title(f'Long simulation (p = {p})')
        ax.set_xlabel('Game length')
        ax.set_ylabel('Probability')
        ax.text(0.95, 0.95, f'Mean: {mean}\nStd dev: {stdev:.2f}', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.3', alpha=0.8))

    plt.suptitle('Distribution of the game lenght over p probability')
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
    plt.savefig('./images/ex-03')
