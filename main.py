import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import aba, ba, bfo, ca, chso, cso, fa, fwa, gsa, gwo, hs, nonswarm_sa, pso, ssa, wsa, nonswarm_tabu
import pandas as pd
import time
import numpy as np
import matplotlib as plt
from SwarmPackagePy import convergence

# alh = SwarmPackagePy.pso(50, tf.easom_function, -10, 10, 3, 20,
#                          w=0.5, c1=1, c2=1)
# animation(alh.get_agents(), tf.easom_function, -10, 10)
# animation3D(alh.get_agents(), tf.easom_function, -10, 10)

if __name__ == "__main__":
    # plot all test functions in 2D
    list_of_functions = tf.default_all_functions_initialize()
    list_of_algorithms = [aba, ba, bfo, ca, cso, fa, fwa, gsa, gwo, hs, pso, ssa, wsa]
    # List of population sizes
    list_of_population = [10, 20, 30]

    # All functions will be evaluated in a [-10, 10] space
    lb = -100
    ub = 100
    # List of dimensions to be evaluated. Dimensions means, that the function will be evaluated in a n-dimensional space if its possible
    # For example, dixon_price_function can be evaluated in 2, 5, 10, 20, 30, 50, 100 dimensions.
    # Each algorithm handles the dimensions and generates a random population in the specified dimension

    list_of_dimensions = [100, 150]
    
    # Then evaulate the algorithms in the functions and dimensions. 
    # It's important to store the results in a file, so we can analyze the results later.
    # So we will store the results in a pandas DataFrame to analyze the results later as CSV file.

    # The DataFrame will have the following columns:
    # Algorithm, Function, Dimension, Population, Best Value, Execution Time, Best Agent
    # The DataFrame will be stored in a CSV file called results.csv

    # The principal data that we want to analyze is the Best Value, the mean population, the mean execution time and the mean best agent.
    results = []
    agents_by_algorithm = {}
    for function in list_of_functions:
        # print(f'Function: {function.__name__}')
        for algorithm in list_of_algorithms:
            # print(f'Algorithm: {algorithm.__name__}')
            for dimension in list_of_dimensions:
                # print(f'Dimension: {dimension}')
                for n in list_of_population:
                    # Execute the algorithm
                    # alh = algorithm(n, function, lb, ub, dimension, 20)
                    # Generate convergence plot
                    # convergence.convergence_plot(alh.get_agents(), function, algorithm.__name__, dimension)
                    pass
    

    for function in list_of_functions:
    # print(f'Function: {function.__name__}')
        for algorithm in list_of_algorithms:
            # print(f'Algorithm: {algorithm.__name__}')
                # Execute the algorithm
                alh = algorithm(20, function, lb, ub, 100, 35)
                # Generate convergence plot
                agents_by_algorithm[algorithm.__name__] = alh.get_agents()
                # convergence.convergence_plot(alh.get_agents(), function, algorithm.__name__, dimension)
        # Generate a grouped convergence plot
        convergence.generate_grouped_convergence_plots(agents_by_algorithm, function)