import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D


# alh = SwarmPackagePy.pso(50, tf.easom_function, -10, 10, 3, 20,
#                          w=0.5, c1=1, c2=1)
# animation(alh.get_agents(), tf.easom_function, -10, 10)
# animation3D(alh.get_agents(), tf.easom_function, -10, 10)

if __name__ == "__main__":
    # plot all test functions in 2D

    list_of_functions = tf.default_all_functions_initialize()
    for function_benchmark in list_of_functions:
        plotter = tf.FunctionPlotter(function_benchmark, -20, 20)
        plotter.plot()