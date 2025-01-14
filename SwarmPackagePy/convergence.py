from matplotlib import pyplot as plt
import numpy as np
import os 
import signal


def convergence_plot(agents, function, algorithm_name, dimension):
    """
    Given all the agents evaluated in len(agents) iterations, this function generates a convergence line chart image of the agents
    The X axis represents the iterations and the Y axis represents the value of the function.
    Plot the best and the average value of the agents for each iteration.
    And stores the plot in a file with the name of the function, the number of agents, and the number of iterations and dimension.

    :param agents: agents
    :param function: function
    :param lb: lower bound
    :param ub: upper bound
    :param algorithm_name: name of the algorithm
    """
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # Create a folder to store the convergence plots
    if not os.path.exists(f'convergence_plots/{algorithm_name}'):
        os.makedirs(f'convergence_plots/{algorithm_name}')
    # Create the figure
    fig = plt.figure()

    # Set the title of the plot
    plt.title("{} with function {} with {} elements".format(algorithm_name, function.__name__,len(agents[0])), loc='left')

    # Create the convergence line chart
    best_values = [np.min([function(j) for j in i]) for i in agents]
    average_values = [np.mean([function(j) for j in i]) for i in agents]

    # Plot the best values
    plt.plot(best_values, color='blue', label='Best Value')

    # Plot the average values
    plt.plot(average_values, color='red', label='Average Value')

    # Set the labels
    plt.xlabel('Iterations')
    plt.ylabel('Function Value')

    # Set the legend
    plt.legend()
    # Save the plot without showing it
    plt.savefig('convergence_plots/{}/convergence_{}_{}_{}_agents_{}_dimensions.png'.format(algorithm_name,algorithm_name, function.__name__, len(agents[0]), dimension))


def generate_grouped_convergence_plots(agents_by_algorithm: dict, function):

    """
    Given a dict of agents evaluated by algorithm, this function generates a grouped convergence line chart image of the agents
    with the name of the given algorithm.
    The X axis represents the iterations and the Y axis represents the value of the function.

    Adds only the best value of the agents for each iteration and add a label of the algorithm name.
    """
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Create the figure
    fig = plt.figure()

    # Set the title of the plot
    plt.title("Convergence of the algorithms with function {}".format(function.__name__), loc='left')

    # Create the convergence line chart
    for algorithm, agents in agents_by_algorithm.items():
        best_values = [np.min([function(j) for j in i]) for i in agents]
        # Plot the best values
        plt.plot(best_values, label=algorithm)

    # Set the labels
    plt.xlabel('Iterations')
    plt.ylabel('Function Value')

    # Set the legend
    plt.legend()
    # Save the plot without showing it
    plt.savefig('convergence_plots/grouped_convergence_{}.png'.format(function.__name__))
    # plt.show()