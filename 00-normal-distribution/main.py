import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def num_bins(sample: np.ndarray) -> int:

    '''
    Function for calculating the number of bins defined by Scott's reference rule
    Args:
        sample (np.ndarray): sample array of pseudo-random variables.
    Returns:
        int: recommended number of bins calculated with Scott's formula
    '''

    bin_width = (3.49 * np.std(sample)) / np.cbrt(len(sample))
    return int((max(sample) - min(sample)) / bin_width)


def generate_random_variables(sample_size: int = 1000000) -> tuple:

    '''
    Generate random variables using the Box-Muller transform.
    Args:
        sample_size (int): size of the sample
    Returns:
        tuple:
            - np.ndarray: first generated array of random numbers
            - np.ndarray: second generated array of random numbers
    '''

    np.random.seed(237)
    x1 = np.random.uniform(size=sample_size)
    x2 = np.random.uniform(size=sample_size)

    r = np.sqrt(-2 * np.log(x1))
    phi = 2 * np.pi * x2

    y1 = r * np.cos(phi)
    y2 = r * np.sin(phi)

    return y1, y2


def calculate_theoretical_cdf(sorted_array: np.ndarray) -> tuple:

    '''
    Calculate the theoretical cumulative distribution function (CDF) for a 
    standard normal distribution N(0,1), given a sorted array of data.

    Args:
        sorted_array (np.ndarray): a sorted array of data for which to compute the CDF
    Returns:
        tuple:
            - x_values (np.ndarray): an array of equally spaced x-values
            - cdf_values (np.ndarray): the corresponding theoretical CDF values
    '''

    x_values = np.linspace(min(sorted_array), max(sorted_array), len(sorted_array))
    return x_values, norm.cdf(x_values, loc=0, scale=1)


def calculate_empirical_cdf(sorted_array: np.ndarray) -> np.ndarray:
    
    '''
    Calculate the empirical cumulative distribution function (CDF) for a given 
    sorted array of data.
    Args:
        sorted_array (np.ndarray): a sorted array of data for which to compute the empirical CDF
    Returns:
        np.ndarray: an array representing the cumulative probabilities for each data point in the sorted array.
    '''

    return np.arange(1, len(sorted_array) + 1) / len(sorted_array)


def plot(sample_size: int):

    '''
    Generate and save histograms and CDF comparison plots for random variables 
    generated using the Box-Muller transform.
    Args:
        sample_size (int): the number of random variables to generate and use for plotting
    Returns:
        None: the function saves plots to disk but does not return any values
    '''

    # create a directory for saving output plots
    output_dir = f'./n-{sample_size}'
    os.makedirs(output_dir, exist_ok=True)

    # plot histograms
    y1, y2 = generate_random_variables(sample_size)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    temp = ax1.hist(y1, bins=num_bins(y1), density=True, alpha=0.6, color='#A88C8C')
    ax1.set_title('Histogram of Y1 (Box-Mueller)')

    temp = ax2.hist(y2, bins=num_bins(y2), density=True, alpha=0.6, color='#82799B')
    ax2.set_title('Histogram of Y2 (Box-Mueller)')

    plt.suptitle(f'Random number generator for n={sample_size}')
    plt.savefig(f'./{output_dir}/histogram')

    # plot the empirical CDF against the theoretical CDF
    sorted_array = np.sort(y1)
    empirical_cdf = calculate_empirical_cdf(sorted_array)
    x_values, theoretical_cdf = calculate_theoretical_cdf(sorted_array)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(sorted_array, empirical_cdf, label='Empirical CDF', color='b')
    ax.plot(x_values, theoretical_cdf, label='Theoretical CDF (N(0,1))', color='r', linestyle='--')

    ax.set_title('Empirical vs Theoretical CDF')
    ax.set_xlabel('Value')
    ax.set_ylabel('CDF')
    ax.legend()

    plt.savefig(f'{output_dir}/cdf-empirical-vs-theoretical.png')


if __name__ == '__main__':

    # argument parser to handle command line arguments
    parser = argparse.ArgumentParser(description='Generate random variables and compare CDFs.')
    parser.add_argument('-n', '--sample_size', type=int, default=1000000, help='Number of random variables to generate.')

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the provided sample size
    plot(args.sample_size)
