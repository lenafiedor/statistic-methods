import numpy as np


NUM_GAMES_SHORT = 10
NUM_GAMES_LONG = 1000


def simulate_ruin_multiplayer(player_capitals: list, p: np.ndarray, stop: int = float('inf')) -> tuple:

    '''
    Simulates the ruin process among multiple players with initial capital values.

    Parameters:
        player_capitals (list): Initial capital of all players. Length defines the number of players.
        p (np.ndarray): Square matrix of probabilities. p[i][j] is the probability that player i receives $1 from player j.
        stop (int): Maximum number of rounds to simulate.

    Returns:
        tuple:
            - int: The index of the first player to go bankrupt (capital reaches 0), or -1 if none go bankrupt.
            - int: Total number of rounds played.
            - list: Remaining capital of all players after the simulation.
    '''

    initial_capitals = player_capitals.copy()
    num_players = len(player_capitals)
    count = 0

    while all(capital > 0 for capital in initial_capitals) and count < stop:
        count += 1
        players = np.random.choice(num_players*num_players, 1, p=p.flatten())
        receiver, giver = divmod(players[0], num_players)
    
        if initial_capitals[giver] > 0:
            initial_capitals[giver] -= 1
            initial_capitals[receiver] += 1

    bankrupt_player = -1
    for i in range(num_players):
        if initial_capitals[i] == 0:
            bankrupt_player = i
    return bankrupt_player, count, initial_capitals

def estimate_ruin_probability_multiplayer(num_games: int, players_capitals: list, p: np.ndarray) -> float:

    '''
    Estimates the probability of Player's A ruin over a specified number of games.

    Parameters:
        num_games (int): Number of games to simulate for averaging ruin probability.
        players_capitals (list): Initial capital of all players.
        p (np.ndarray): A square matrix of probabilities. p[i][j] is the probability that player i receives $1 from player j.

    Returns:
        float: Estimated probability of Player's A ruin based on simulation.
    '''

    ruin_count = 0

    for _ in range(num_games):
        bankrupt_player, _, _ = simulate_ruin_multiplayer(players_capitals, p)
        if bankrupt_player == 0:
            ruin_count += 1

    return ruin_count / num_games

def estimate_game_length_multiplayer(num_games: int, players_capitals: list, p: np.ndarray) -> tuple:

    '''
    Estimates the average game length and its standard deviation over a specified number of games,
    providing the game length for each simulation.

    Parameters:
        num_games (int): Number of games to simulate for estimating game length statistics.
        player_capitals (list): Initial capital of all players.
        p (np.ndarray): A square matrix of probabilities. p[i][j] is the probability that player i receives $1 from player j.

    Returns:
        tuple:
            - float: Average number of rounds played before one player goes bankrupt.
            - float: Standard deviation of game lengths over the simulations.
    '''

    game_lengths = [simulate_ruin_multiplayer(players_capitals, p)[1] for _ in range(num_games)]
    return game_lengths, int(np.mean(game_lengths)), np.std(game_lengths)
