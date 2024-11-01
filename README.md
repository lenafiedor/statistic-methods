# statistic-methods

## 00-normal-distribution
Generate histograms and Cumulative Distribution Function for random variables generated using the Box-Muller transform.

### Histogram and CDF comparison
- For sample size `n=1000`
![histogram for n=1000](./00-normal-distribution/n-1000/histogram.png)
![cdf for n=1000](./00-normal-distribution/n-1000/cdf-empirical-vs-theoretical.png)
- For sample size `n=1000000`
![histogram for n=1000](./00-normal-distribution/n-1000000/histogram.png)
![cdf for n=1000000](./00-normal-distribution/n-1000000/cdf-empirical-vs-theoretical.png)

## 01-gamblers-ruin
Simulation of the Gambler's Ruin.

### Exercise 1
Given the initial capital for two players `a = b = 50` and a **changing probability p** of passing $1 from Player B to Player A, estimate the probability of loosing the capital by Player A **depending on p probability**.<br>
Probability was estimated over 10 and 1000 games.
![probability of ruin A over p](./01-gamblers-ruin/images/ex-01.png)

### Exercise 2
Given the probability of passing $1 from Player A to Player B `p = 0.5` and a **changing capital of Players A and B** (such that `a + b = 100`), estimate the probability of loosing the capital by Player A **depending on initial capital**.<br>
Probability was estimated over 10 and 1000 games.
![probability of ruin A over initial capital](./01-gamblers-ruin/images/ex-02.png)

### Exercise 3
Given the initial capital for two players `a = b = 50` and a **changing probability `p = [0.2, 0.5, 0.8]`** of passing $1 from Player B to Player B, create the distribution of game length probabilities **depending on p probability**.
![game length probability distribution](./01-gamblers-ruin/images/ex-03.png)

### Exercise 4
Given the initial capital for two players `a = b = 50` and a **changing probability p** of passing $1 from Player A to Player B, estimate the average game length **depending on p probability**.
![average game length over p](./01-gamblers-ruin/images/ex-04.png)

### Exercise 5
Given the initial capital for two players `a = b = 50`, **changing probability p `p = [0.2, 0.5]`** of passing $1 from Player A to Player B and **three cases of number of steps `n = [10, l_mean / 2, 0.9 * l_mean]`, where `l_mean` is the mean game length for given p value**, generate the distribution of the final capital of Player A **depending on p and n values**.
![final capital over p and n](./01-gamblers-ruin/images/ex-05.png)

### Exercise 6
Given a sample of **chosen intitial capitals (such that `a + b = 100`) and p probabilities**, generate **trajectories of wins for both players over the number of games (counting processes)**.
![trajectories of wins for a and b](./01-gamblers-ruin/images/ex-06.png)
