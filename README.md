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
Given the initial capital for two players = 50 (const) and a **changing probability p** of passing $1 from Player A to Player B, estimate the probability of loosing the capital by Player A **depending on p probability**.<br>
Probability was estimated over 10 and 1000 games.
![probability of ruin A over p](./01-gamblers-ruin/images/ex-01.png)

### Exercise 2
Given the probability p of passing $1 from Player A to Player B = 0.5 (const) and a **changing capital of Players A and B** (such that `a + b = 100`), estimate the probability of loosing the capital by Player A **depending on initial capital**.<br>
Probability was estimated over 10 and 1000 games.
![probability of ruin A over initial capital](./01-gamblers-ruin/images/ex-02.png)


### Exercise 3
Given the initial capital for two players = 50 (const) and a **changing probability `p = [0.2, 0.5, 0.8]`** of passing $1 from Player A to Player B, estimate the average number of rounds and its standard deviation **depending on p probability**.<br>
