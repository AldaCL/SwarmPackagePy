from math import exp
import numpy as np
from random import normalvariate, randint, random
from . import intelligence


class tabu(intelligence.sw):
    """
    Tabu Search Optimization, inspired by the work of Glover (1986)

    This class implements the Tabu Search optimization algorithm.
    addecuated to be compatible with intelligence.sw class from 
    SwarmPackagePy.
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, tabulen=5):
        """
        Initializes the Tabu Search algorithm.

        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: the number of iterations
        :param tabulen: length of the tabu list (default is 5)
        """

        super(tabu, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self.__best_agent = np.copy(self.__agents)
        self.__best_value = np.array([function(x) for x in self.__agents]).min()

        tabu_list = []

        for t in range(iteration):

            best_agent = np.copy(self.__agents[0])
            best_value = function(best_agent)

            for i in range(n):

                x_new = self.__agents[i] + np.random.normal(0, 1, dimension)
                x_new = np.clip(x_new, lb, ub)

                f_new = function(x_new)
                f_old = function(self.__agents[i])

                if f_new < f_old and x_new.tolist() not in tabu_list:
                    self.__agents[i] = x_new
                    tabu_list.append(x_new.tolist())

                    if len(tabu_list) > tabulen:
                        tabu_list.pop(0)

                if f_new < best_value:
                    best_agent = np.copy(x_new)
                    best_value = f_new

            if best_value < self.__best_value:
                self.__best_agent = np.copy(best_agent)
                self.__best_value = best_value

        self._set_Gbest(self.__best_agent)