from math import ceil, exp, floor
import numpy as np
from random import random

from . import intelligence

class sa(intelligence.sw):
    """
    Simulated Annealing

    This class implements the Simulated Annealing optimization algorithm.
    Author: Aldair Cortes (AfroMonkey)
    """

    def __init__(self, n, function, lb, ub, dimension, iteration, T0=1000, alpha=0.85):
        """
        Initializes the Simulated Annealing algorithm.

        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: the number of iterations
        :param T0: initial temperature (default is 1000)
        :param alpha: temperature reduction coefficient (default is 0.85)
        """

        super(sa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self.__best_agent = np.copy(self.__agents)
        self.__best_value = np.array([function(x) for x in self.__agents]).min()

        T = T0

        for t in range(iteration):
            
            for i in range(n):

                x_new = self.__agents[i] + np.random.normal(0, 1, dimension)
                x_new = np.clip(x_new, lb, ub)

                f_new = function(x_new)
                f_old = function(self.__agents[i])

                if f_new < f_old or random() < exp(-(f_new - f_old) / T):
                    self.__agents[i] = x_new

                if f_new < self.__best_value:
                    self.__best_agent = np.copy(x_new)
                    self.__best_value = f_new

            T = alpha * T

            self._points(self.__agents)
        
        