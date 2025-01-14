import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D


# alh = SwarmPackagePy.pso(50, tf.easom_function, -10, 10, 3, 20,
#                          w=0.5, c1=1, c2=1)
# animation(alh.get_agents(), tf.easom_function, -10, 10)
# animation3D(alh.get_agents(), tf.easom_function, -10, 10)

if __name__ == "__main__":
    function_2 = SwarmPackagePy.aba(50, tf.three_hump_camel_function, -60, 60, 2, 100)
    animation(function_2.get_agents(),tf.three_hump_camel_function, -60, 60 )
    
