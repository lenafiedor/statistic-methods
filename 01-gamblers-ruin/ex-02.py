import matplotlib.pyplot as plt
from simulation import *


if __name__ == '__main__':    

    # set initial capitals and probability
    a_initial = np.arange(10, 100, 10)
    p = 0.5

    # run the short simulation (averaging over 10 games)
    ruin_count_short = [estimate_ruin_probability(NUM_GAMES_SHORT, a, 100 - a, p) for a in a_initial]

    # run the long simulation (averaging over 1000 games)
    ruin_count_long = [estimate_ruin_probability(NUM_GAMES_SHORT, a, 100 - a, p) for a in a_initial]

    # plot the probabilites
    plt.figure(figsize=(12, 6))

    plt.plot(a_initial, ruin_count_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C')
    plt.plot(a_initial, ruin_count_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B')

    plt.xlabel('Initial capital of Player A')
    plt.ylabel('P(ruin A)')
    plt.legend()
    plt.grid()
    plt.title('Probability of ruin A over initial capital')
    
    plt.savefig('./images/ex-02')
