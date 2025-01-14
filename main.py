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
    alh = SwarmPackagePy.pso(15, function, -10, 10, 2, 20)
    # Show animation
    animation3D(alh.get_agents(), function, -100, 100)