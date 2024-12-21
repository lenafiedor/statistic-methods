import numpy as np


transition_matrix = np.array([
    [0.64, 0.32, 0.04],
    [0.4, 0.5, 0.1],
    [0.25, 0.5, 0.25]
])
pi_0 = np.array([0, 0, 1])

def find_steady_state(transition_matrix: np.array, pi_0: np.array, max_iter: int=1000, epsilon: float=1e-5):

    """
    Computes the steady-state distribution of a Markov chain using an iterative approach.

    Parameters:
        transition_matrix (np.array):
            A square matrix of shape (n, n) representing the transition probabilities
            between states in a Markov chain, where n is the number of states.
        pi_0 (np.array):
            The initial probability distribution over the states.
            Shape: (n,), where n is the number of states.
        max_iter (int, optional):
            Maximum number of iterations to perform. Default is 1000.
        epsilon (float, optional):
            The convergence threshold for the difference between consecutive distributions
            (using the infinity norm). Default is 1e-5.

    Returns:
        tuple: A tuple containing:
            - pi (np.array): The steady-state distribution (probability vector).
            - diff_norms (list): A list of differences (norms) between consecutive distributions.
            - num_iter (int): The number of iterations performed before convergence.
    """
    pi = pi_0
    diff_norms = []
    num_iter = 0

    for n in range(max_iter):
        pi_next = np.dot(transition_matrix, pi)
        diff = np.linalg.norm(pi_next - pi, ord=np.inf) # infinity norm
        diff_norms.append(diff)

        if diff < epsilon:
            num_iter = n + 1
            break

        pi = pi_next
    return pi, diff_norms, num_iter

def simulate_agent(transition_matrix, start_state, num_steps, num_simulations):

    """
    Simulates a Markov chain process and estimates the stationary distribution
    by analyzing the states reached after a specified number of steps.

    Parameters:
        transition_matrix (np.ndarray):
            A square matrix of shape (n, n) representing the transition probabilities
            between states in a Markov chain, where n is the number of states.
        start_state (int):
            The initial state index from which the agent starts. Must be an integer
            between 0 and n-1, where n is the number of states.
        num_steps (int):
            The number of steps (transitions) the agent performs in each simulation.
        num_simulations (int):
            The total number of independent simulations to run. Each simulation starts
            from the specified `start_state` and runs for `num_steps` transitions.

    Returns:
        np.ndarray
            A 1D numpy array of shape (n,) representing the estimated distribution
            of states. Each element corresponds to the proportion of simulations
            that ended in a particular state after `num_steps` steps.
    """

    num_states = transition_matrix.shape[0]
    state_counts = np.zeros(num_states)

    for _ in range(num_simulations):
        current_state = start_state
        for _ in range(num_steps):
            current_state = np.random.choice(num_states, p=transition_matrix[current_state])
        state_counts[current_state] += 1

    return state_counts / num_simulations
