from common import *
from matplotlib import pyplot as plt

NUM_SIMULATIONS = 10000

num_iter = find_steady_state(transition_matrix, pi_0)[2]

steady_states_simulated = []
num_states = transition_matrix.shape[0]

for initial_state in range(num_states):
    estimated_state = simulate_agent(transition_matrix, initial_state, num_iter, NUM_SIMULATIONS)
    steady_states_simulated.append(estimated_state)

steady_states_simulated = np.array(steady_states_simulated)
steady_state_theoretical = np.array([0.5102, 0.4082, 0.0816])

print(steady_states_simulated, steady_state_theoretical)

states = [0, 1, 2]
bar_width = 0.2

x = np.arange(len(states))

plt.figure(figsize=(10, 6))

plt.bar(x - 1.5 * bar_width, steady_state_theoretical, width=bar_width, label="Theoretical", color="#4C6D86")
plt.bar(x - 0.5 * bar_width, steady_states_simulated[0], width=bar_width, label="Start: State 0", color="#9BC1BC")
plt.bar(x + 0.5 * bar_width, steady_states_simulated[1], width=bar_width, label="Start: State 1", color="#E6B89C")
plt.bar(x + 1.5 * bar_width, steady_states_simulated[2], width=bar_width, label="Start: State 2", color="#A992BB")

plt.xlabel("States")
plt.ylabel("Probability")
plt.title("Comparison of simulated and theoretical stationary states")
plt.xticks(x, labels=[f"State {i}" for i in states])
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig('../images/ex-09.png')