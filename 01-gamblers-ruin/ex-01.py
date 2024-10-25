import numpy as np
import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':

    # set initial capitals and define probabilities
    a_initial = 50
    b_initial = 50
    p_values = np.arange(0.0, 1.0, 0.1)

    # run the short simulation (averaging over 10 games)
    ruin_count_short = [estimate_ruin_probability(NUM_GAMES_SHORT, a_initial, b_initial, p) for p in p_values]

    # run the long simulation (averaging over 1000 games)
    ruin_count_long = [estimate_ruin_probability(NUM_GAMES_LONG, a_initial, b_initial, p) for p in p_values]

    # plot the probabilites
    plt.figure(figsize=(12, 6))

    plt.plot(p_values, ruin_count_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C')
    plt.plot(p_values, ruin_count_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B')

    plt.xlabel('Probability value (p)')
    plt.ylabel('P(ruin A)')
    plt.legend()
    plt.grid()
    plt.title('Probability of ruin A over p probability')
    
    plt.savefig('./images/ex-01')
