
import numpy as np
import matplotlib.pyplot as plt
from simulation_multiplayer import *


if __name__ == '__main__':
    
    # ex-01 for 5 players
    players_capitals = [20 for i in range(5)]

    p_values = np.array([
        [
            [0.0, 0.02, 0.02, 0.02, 0.02],
            [0.04, 0.0, 0.04, 0.04, 0.04],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.06, 0.06, 0.06, 0.0, 0.06],
            [0.08, 0.08, 0.08, 0.08, 0.0]
        ],
        [
            [0.0, 0.05, 0.05, 0.05, 0.05],
            [0.05, 0.0, 0.05, 0.05, 0.05],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.05, 0.05, 0.05, 0.0, 0.05],
            [0.05, 0.05, 0.05, 0.05, 0.0]
        ],
        [
            [0.0, 0.08, 0.08, 0.08, 0.08],
            [0.06, 0.0, 0.06, 0.06, 0.06],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.04, 0.04, 0.04, 0.0, 0.04],
            [0.02, 0.02, 0.02, 0.02, 0.0]
        ],
    ])
    
    # run the short simulation (averaging over 10 games)
    ruin_count_short = [estimate_ruin_probability_multiplayer(NUM_GAMES_SHORT,  players_capitals, p) for p in p_values]

    # run the long simulation (averaging over 1000 games)
    ruin_count_long = [estimate_ruin_probability_multiplayer(NUM_GAMES_LONG, players_capitals, p) for p in p_values]

    plt.figure(figsize=(10, 6))

    plt.plot([sum(p[0]) for p in p_values], ruin_count_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C')
    plt.plot([sum(p[0]) for p in p_values], ruin_count_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B')

    plt.xlabel('Cumulative p value for Player A')
    plt.ylabel('P(ruin A)')
    plt.title('Probability of ruin A over p probability')
    plt.legend()
    plt.grid()

    plt.savefig('./images/ex-07-1')


    # ex-02 for 5 players
    players_capitals = np.array([
        [10, 15, 20, 25, 30],
        [20, 20, 20, 20, 20],
        [30, 25, 20, 15, 10]
    ])

    p_values = np.array([
        [0.0, 0.05, 0.05, 0.05, 0.05],
        [0.05, 0.0, 0.05, 0.05, 0.05],
        [0.05, 0.05, 0.0, 0.05, 0.05],
        [0.05, 0.05, 0.05, 0.0, 0.05],
        [0.05, 0.05, 0.05, 0.05, 0.0]
    ])

    # run the short simulation (averaging over 10 games)
    ruin_count_short = [estimate_ruin_probability_multiplayer(NUM_GAMES_SHORT,  capital, p_values) for capital in players_capitals]

    # run the long simulation (averaging over 1000 games)
    ruin_count_long = [estimate_ruin_probability_multiplayer(NUM_GAMES_LONG, capital, p_values) for capital in players_capitals]

    plt.figure(figsize=(10, 6))

    plt.plot([capital[0] for capital in players_capitals], ruin_count_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C')
    plt.plot([capital[0] for capital in players_capitals], ruin_count_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B')

    plt.xlabel('Initial capital of Player A')
    plt.ylabel('P(ruin A)')
    plt.title('Probability of ruin A over initial capital')
    plt.legend()
    plt.grid()

    plt.savefig('./images/ex-07-2')
    

    # ex-03 for 5 players
    players_capitals = [20 for i in range(5)]
    p_values = np.array([
        [
            [0.0, 0.02, 0.02, 0.02, 0.02],
            [0.04, 0.0, 0.04, 0.04, 0.04],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.06, 0.06, 0.06, 0.0, 0.06],
            [0.08, 0.08, 0.08, 0.08, 0.0]
        ],
        [
            [0.0, 0.05, 0.05, 0.05, 0.05],
            [0.05, 0.0, 0.05, 0.05, 0.05],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.05, 0.05, 0.05, 0.0, 0.05],
            [0.05, 0.05, 0.05, 0.05, 0.0]
        ],
        [
            [0.0, 0.08, 0.08, 0.08, 0.08],
            [0.06, 0.0, 0.06, 0.06, 0.06],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.04, 0.04, 0.04, 0.0, 0.04],
            [0.02, 0.02, 0.02, 0.02, 0.0]
        ],
    ])

    # run the short simulation (averaging over 10 games)
    num_rounds_short = []
    num_rounds_mean_short = []
    num_rounds_stdev_short = []
    
    for p in p_values:
        num_rounds, mean_length, stdev_length = estimate_game_length_multiplayer(NUM_GAMES_SHORT, players_capitals, p)
        num_rounds_short.append(num_rounds)
        num_rounds_mean_short.append(mean_length)
        num_rounds_stdev_short.append(stdev_length)

    # run the long simulation (averaging over 1000 games)
    num_rounds_long = []
    num_rounds_mean_long = []
    num_rounds_stdev_long = []

    for p in p_values:
        num_rounds, mean_length, stdev_length = estimate_game_length_multiplayer(NUM_GAMES_LONG, players_capitals, p)
        num_rounds_long.append(num_rounds)
        num_rounds_mean_long.append(mean_length)
        num_rounds_stdev_long.append(stdev_length)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    for ax, p, lengths, mean, stdev in zip(axes[0], p_values, num_rounds_short, num_rounds_mean_short, num_rounds_stdev_short):
        ax.hist(lengths, bins=50, color='#A88C8C', edgecolor='black', alpha=0.7, density=True)
        ax.set_title(f'Short simulation (cumulative p = {sum(p[0])})')
        ax.set_xlabel('Game length')
        ax.set_ylabel('Probability')
        ax.text(0.95, 0.95, f'Mean: {mean}\nStd dev: {stdev:.2f}', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.3', alpha=0.8))
        
    for ax, p, lengths, mean, stdev in zip(axes[1], p_values, num_rounds_long, num_rounds_mean_long, num_rounds_stdev_long):
        ax.hist(lengths, bins=50, color='#82799B', edgecolor='black', alpha=0.7, density=True)
        ax.set_title(f'Long simulation (cumulative p = {sum(p[0])})')
        ax.set_xlabel('Game length')
        ax.set_ylabel('Probability')
        ax.text(0.95, 0.95, f'Mean: {mean}\nStd dev: {stdev:.2f}', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round, pad=0.3', alpha=0.8))

    plt.suptitle('Distribution of the game lenght over p probability')
    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
    plt.savefig('./images/ex-07-3')
    

    # ex-06 for 5 players
    players_capitals = np.array([
        [10, 15, 20, 25, 30],
        [20, 20, 20, 20, 20],
        [30, 25, 20, 15, 10]
    ])

    p_values = np.array([
        [
            [0.0, 0.02, 0.02, 0.02, 0.02],
            [0.04, 0.0, 0.04, 0.04, 0.04],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.06, 0.06, 0.06, 0.0, 0.06],
            [0.08, 0.08, 0.08, 0.08, 0.0]
        ],
        [
            [0.0, 0.05, 0.05, 0.05, 0.05],
            [0.05, 0.0, 0.05, 0.05, 0.05],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.05, 0.05, 0.05, 0.0, 0.05],
            [0.05, 0.05, 0.05, 0.05, 0.0]
        ],
        [
            [0.0, 0.08, 0.08, 0.08, 0.08],
            [0.06, 0.0, 0.06, 0.06, 0.06],
            [0.05, 0.05, 0.0, 0.05, 0.05],
            [0.04, 0.04, 0.04, 0.0, 0.04],
            [0.02, 0.02, 0.02, 0.02, 0.0]
        ],
    ])

    # initialize an empty list to store lost trajectories
    a_lost = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in players_capitals]
    b_lost = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in players_capitals]
    c_lost = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in players_capitals]
    d_lost = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in players_capitals]
    e_lost = [[[0 for _ in range(NUM_GAMES_LONG)] for _ in p_values] for _ in players_capitals]

    for i, capitals in enumerate(players_capitals):
        for j, p in enumerate(p_values):
            for k in range(NUM_GAMES_LONG):
                a_lost[i][j][k] = a_lost[i][j][k-1]
                b_lost[i][j][k] = b_lost[i][j][k-1]
                c_lost[i][j][k] = c_lost[i][j][k-1]
                d_lost[i][j][k] = d_lost[i][j][k-1]
                e_lost[i][j][k] = e_lost[i][j][k-1]
                bankrupt_player = simulate_ruin_multiplayer(capitals, p)[0]
                if bankrupt_player == 0:
                    a_lost[i][j][k] += 1
                elif bankrupt_player == 1:
                    b_lost[i][j][k] += 1
                elif bankrupt_player == 2:
                    c_lost[i][j][k] += 1
                elif bankrupt_player == 3:
                    d_lost[i][j][k] += 1
                elif bankrupt_player == 4:
                    e_lost[i][j][k] += 1

    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    fig.suptitle('Lose trajectories for different initial capitals and probabilities\np - an array of cumulative p values for each player', fontsize=16)

    for i, capital in enumerate(players_capitals):
        for j, p in enumerate(p_values):
            ax = axes[i, j]
            ax.plot(a_lost[i][j], color='#A88C8C', label='Player A')
            ax.plot(b_lost[i][j], color='#82799B', label='Player B')
            ax.plot(c_lost[i][j], color='#F77B72', label='Player C')
            ax.plot(d_lost[i][j], color='#761A3D', label='Player D')
            ax.plot(e_lost[i][j], color='#A5C392', label='Player E')
            ax.set_title(f'Initial capitals: A = {capitals[0]}, B = {capitals[1]}, C = {capitals[2]}, D = {capitals[3]}, E = {capitals[4]}\n' +
                        f'p = {[float(sum(row)) for row in p]}')
            ax.set_xlabel('Game number')
            ax.set_ylabel('Cumulative loses')
            ax.grid()
            ax.legend()

    plt.tight_layout(pad=3.0)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
    plt.savefig('./images/ex-07-6')
