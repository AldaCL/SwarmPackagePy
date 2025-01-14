import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D


# alh = SwarmPackagePy.pso(50, tf.easom_function, -10, 10, 3, 20,
#                          w=0.5, c1=1, c2=1)
# animation(alh.get_agents(), tf.easom_function, -10, 10)
# animation3D(alh.get_agents(), tf.easom_function, -10, 10)

if __name__ == "__main__":
    # Compute the algorithm
    function = SwarmPackagePy.testFunctions.easom_function
    alh = SwarmPackagePy.pso(n=50, function=function, lb=-10, ub=10, dimension=2, iteration=20, w=0.5, c1=1, c2=1)
    # Show animation
    animation(alh.get_agents(), function, 10, -10)
