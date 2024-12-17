import matplotlib.pyplot as plt

from common import transition_matrix, pi_0, find_steady_state

pi, diff_norms, num_iter = find_steady_state(transition_matrix, pi_0)

plt.plot(diff_norms, color="#674E86")
plt.xlim(0, num_iter-1)
plt.xlabel('Iteration index')
plt.ylabel('|P^n - P^(n-1)|')
plt.title(f'Convergence of infinity norms: {num_iter} iterations')
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig('../images/ex-08.png')
