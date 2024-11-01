import numpy as np


NUM_GAMES_SHORT = 10
NUM_GAMES_LONG = 1000


def simulate_ruin(a_initial: int, b_initial: int, p: float, stop: float = float('inf')) -> tuple:

    '''
    Simulates the ruin process between two players with initial capital values.

    Parameters:
        a_initial (int): Initial capital of player A.
        b_initial (int): Initial capital of player B.
        p (float): Probability that player A wins $1 from player B.
        stop (float): Number of rounds after which to stop the game.

    Returns:
        tuple:
            - bool: True if player A goes bankrupt (capital reaches 0), otherwise False.
            - int: Total number of rounds played before one player goes bankrupt.
            - int: Capital of player A after n steps if stop value was specified.
    '''

    a, b = a_initial, b_initial
    count = 0

    while a > 0 and b > 0 and count < stop:

        count += 1
        if np.random.rand() < p:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
    
    return not a, count, a

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
    return game_lengths, int(np.mean(game_lengths)), np.std(game_lengths)

def estimate_capital_distribution(num_games: int, a_initial: int, b_initial: int, n_values: list, p_values: list):

    '''
    Simulates multiple games to estimate the distribution of final capital for Player A over a specified number of rounds 
    and for various probabilities of Player A's success.

    Parameters:
        num_games (int): The number of games to simulate for each combination of initial capital and probability.
        a_initial (int): The starting capital for Player A.
        b_initial (int): The starting capital for Player B.
        n_values (list): A list of tuples, each containing three round counts (n) for which final capital is estimated.
        p_values (list): A list of probabilities representing the likelihood of Player A winning each round.

    Returns:
        list: A 3D list containing the final capital values of Player A for each probability and each round count. 
            Structure: `final_capitals[i][j][k]` where:
            - `i` indexes the probability `p` from `p_values`,
            - `j` indexes the round count `n` from `n_values[i]`,
            - `k` indexes the individual game outcome for that combination.
    '''

    final_capitals = [[[simulate_ruin(a_initial, b_initial, p, n)[2] for _ in range(num_games)] for n in n_tuple] for p, n_tuple in zip(p_values, n_values)]
    return final_capitals
