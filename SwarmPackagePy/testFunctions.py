from math import *


def ackley_function(x):
    return -exp(-sqrt(0.5*sum([i**2 for i in x]))) - \
           exp(0.5*sum([cos(i) for i in x])) + 1 + exp(1)


def bukin_function(x):
    return 100*sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)


def cross_in_tray_function(x):
    return round(-0.0001*(abs(sin(x[0])*sin(x[1])*exp(abs(100 -
                            sqrt(sum([i**2 for i in x]))/pi))) + 1)**0.1, 7)


def sphere_function(x):
    return sum([i**2 for i in x])


def bohachevsky_function(x):
    return x[0]**2 + 2*x[1]**2 - 0.3*cos(3*pi*x[0]) - 0.4*cos(4*pi*x[1]) + 0.7


def sum_squares_function(x):
    return sum([(i+1)*x[i]**2 for i in range(len(x))])


def sum_of_different_powers_function(x):
    return sum([abs(x[i])**(i+2) for i in range(len(x))])


def booth_function(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2


def matyas_function(x):
    return 0.26*sphere_function(x) - 0.48*x[0]*x[1]


def mccormick_function(x):
    return sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1


def dixon_price_function(x):
    return (x[0] - 1)**2 + sum([(i+1)*(2*x[i]**2 - x[i-1])**2
                                for i in range(1, len(x))])


def six_hump_camel_function(x):
    return (4 - 2.1*x[0]**2 + x[0]**4/3)*x[0]**2 + x[0]*x[1]\
           + (-4 + 4*x[1]**2)*x[1]**2


def three_hump_camel_function(x):
    return 2*x[0]**2 - 1.05*x[0]**4 + x[0]**6/6 + x[0]*x[1] + x[1]**2


def easom_function(x):
    return -cos(x[0])*cos(x[1])*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)


def michalewicz_function(x):
    return -sum([sin(x[i])*sin((i+1)*x[i]**2/pi)**20 for i in range(len(x))])


def beale_function(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + \
           (2.625 - x[0] + x[0]*x[1]**3)**2


def drop_wave_function(x):
    return -(1 + cos(12*sqrt(sphere_function(x))))/(0.5*sphere_function(x) + 2)



def default_all_functions_initialize() -> list:
        return [ackley_function, bukin_function, cross_in_tray_function,
                sphere_function, bohachevsky_function, sum_squares_function,
                sum_of_different_powers_function, booth_function,
                matyas_function, mccormick_function, dixon_price_function,
                six_hump_camel_function, three_hump_camel_function,
                easom_function, michalewicz_function, beale_function,
                drop_wave_function]


class FunctionPlotter():
    def __init__(self, function, lb, ub):
        self.function = function
        self.lb = lb
        self.ub = ub

    def plot(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import numpy as np

        side = np.linspace(self.lb, self.ub, 100)
        X, Y = np.meshgrid(side, side)
        Z = np.array([np.array([self.function([X[i][j], Y[i][j]])
                                for j in range(len(X))])
                      for i in range(len(X[0]))])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        # Save the figure as a PNG file with function.__name__ name 
        plt.savefig(self.function.__name__ + '.png')
        
