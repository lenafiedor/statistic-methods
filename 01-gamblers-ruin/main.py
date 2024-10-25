import numpy as np
import matplotlib.pyplot as plt


def simulate_ruin(a_initial: int, b_initial: int, p: float) -> bool:

    '''
    Simulates the ruin process between two players with initial capital values.

    Parameters:
        a_initial (int): Initial capital of player A.
        b_initial (int): Initial capital of player B.
        p (float): Probability that player A wins $1 from player B.

    Returns:
    bool: True if player A goes bankrupt (capital reaches 0), otherwise False.
    '''

    a, b = a_initial, b_initial

    while a > 0 and b > 0:

        if np.random.rand() < p:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
    return not a

def estimate_ruin_probability(num_games: int, a_initial: int, b_initial: int, p: float) -> float:

    '''
    Estimates the probability of player A's ruin over a specified number of games.

    Parameters:
        num_games (int): Number of games to simulate for averaging ruin probability.
        a_initial (int): Initial capital of player A.
        b_initial (int): Initial capital of player B.
        p (float): Probability that player A wins $1 from player B.

    Returns:
        float: Estimated probability of player A's ruin based on simulation.
    '''
    
    ruin_count = sum(simulate_ruin(a_initial, b_initial, p) for _ in range(num_games))
    return ruin_count / num_games


if __name__ == '__main__':

    NUM_GAMES_SHORT = 10
    NUM_GAMES_LONG = 1000
    NUM_GAMES_EXTRA_LONG = 1000000

    # # EXERCISE 1
    # # set initial capitals and define probabilities
    # a_initial = 50
    # b_initial = 50
    # p_values = np.arange(0.0, 1.0, 0.1)

    # # run the short simulation (averaging over 10 games)
    # ruin_count_short = [estimate_ruin_probability(NUM_GAMES_SHORT, a_initial, b_initial, p) for p in p_values]

    # # run the long simulation (averaging over 1000 games)
    # ruin_count_long = [estimate_ruin_probability(NUM_GAMES_LONG, a_initial, b_initial, p) for p in p_values]

    # # plot the probabilites
    # plt.figure(figsize=(12, 6))

    # plt.plot(p_values, ruin_count_short, label=f'{NUM_GAMES_SHORT} games (low averaging)', marker='o', color='#A88C8C')
    # plt.plot(p_values, ruin_count_long, label=f'{NUM_GAMES_LONG} games (high averaging)', marker='o', color='#82799B')

    # plt.xlabel('Probability value (p)')
    # plt.ylabel('P(ruin A)')
    # plt.legend()
    # plt.grid()
    # plt.title('Probability of ruin A over p probability')
    
    # plt.savefig('./images/ex-01')

    # EXERCISE 2
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
