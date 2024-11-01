import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    # set initial capitals and define probabilities
    a_initial = [20, 50, 70]
    p_values = [0.2, 0.5, 0.7]

    # initialize an empty list to store win trajectories
    a_wins = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in a_initial]
    b_wins = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in a_initial]

    for i, a in enumerate(a_initial):
        for j, p in enumerate(p_values):
            for k in range(NUM_GAMES_LONG):
                a_wins[i][j][k] = a_wins[i][j][k-1]
                b_wins[i][j][k] = b_wins[i][j][k-1]
                if simulate_ruin(a, 100 - a, p)[0]:
                    b_wins[i][j][k] += 1
                else:
                    a_wins[i][j][k] += 1

    # plot win trajectories
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    fig.suptitle('Win trajectories for different initial capitals and probabilities', fontsize=16)

    for i, a in enumerate(a_initial):
        for j, p in enumerate(p_values):
            ax = axes[i, j]
            ax.plot(a_wins[i][j], color='#A88C8C', label='Player A')
            ax.plot(b_wins[i][j], color='#82799B', label='Player B')
            ax.set_title(f'Initial capitals: A = {a}, B = {100-a}\np = {p}')
            ax.set_xlabel('Game number')
            ax.set_ylabel('Cumulative wins')
            ax.grid(True)
            ax.legend()

    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
    plt.savefig('./images/ex-06')
    