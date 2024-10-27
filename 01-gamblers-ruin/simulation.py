import numpy as np


NUM_GAMES_SHORT = 10
NUM_GAMES_LONG = 1000


def simulate_ruin(a_initial: int, b_initial: int, p: float) -> tuple:

    '''
    Simulates the ruin process between two players with initial capital values.

    Parameters:
        a_initial (int): Initial capital of player A.
        b_initial (int): Initial capital of player B.
        p (float): Probability that player A wins $1 from player B.

    Returns:
        tuple:
            - bool: True if player A goes bankrupt (capital reaches 0), otherwise False.
            - int: Total number of rounds played before one player goes bankrupt.

    '''

    a, b = a_initial, b_initial
    count = 0

    while a > 0 and b > 0:

        count += 1
        if np.random.rand() < p:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
    
    return not a, count

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
    
    ruin_count = sum(simulate_ruin(a_initial, b_initial, p)[0] for _ in range(num_games))
    return ruin_count / num_games

def estimate_game_length(num_games: int, a_initial: int, b_initial: int, p: float) -> tuple:

    '''
    Estimates the average game length and its standard deviation over a specified number of games,
    providing the game length for each simulation.

    Parameters:
        num_games (int): Number of games to simulate for estimating game length statistics.
        a_initial (int): Initial capital of player A.
        b_initial (int): Initial capital of player B.
        p (float): Probability that player A wins $1 from player B in a round.

    Returns:
        tuple:
            - float: Average number of rounds played before one player goes bankrupt.
            - float: Standard deviation of game lengths over the simulations.
    '''

    game_lengths = [simulate_ruin(a_initial, b_initial, p)[1] for _ in range(num_games)]
    return game_lengths, np.mean(game_lengths), np.std(game_lengths)
