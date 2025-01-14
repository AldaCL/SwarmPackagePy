from matplotlib import pyplot as plt
import matplotlib.animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

def animation(agents, function, lb, ub, sr=False):
    matplotlib.use("TkAgg")

    side = np.linspace(lb, ub, (ub - lb) * 5)
    X, Y = np.meshgrid(side, side)
    Z = np.array([np.array([function([X[i][j], Y[i][j]])
                            for j in range(len(X))])
                  for i in range(len(X[0]))])

    fig = plt.figure()
    plt.axes(xlim=(lb, ub), ylim=(lb, ub))
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.colorbar()

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    plt.title(function.__name__, loc='left')

    def an(i):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))
        plt.title('iteration: {}'.format(i), loc='right')

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(agents) - 1)

    if sr:

        ani.save('result.mp4')

    plt.show()


def animation3D(agents, function, lb, ub, sr=False):
    side = np.linspace(lb, ub, 45)
    X, Y = np.meshgrid(side, side)
    zs = np.array([function([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    fig = plt.figure()

    ax = Axes3D(fig)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet',
                           linewidth=0, antialiased=False)
    ax.set_xlim(lb, ub)
    ax.set_ylim(lb, ub)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    z = np.array([function(j) for j in agents[0]])
    sc = ax.scatter(x, y, z, color='black')

    def an(i):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        z = np.array([function(j) for j in agents[i]])
        sc._offsets3d = (x, y, z)
        plt.title('iteration: {}'.format(i), loc='right')

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(agents) - 1)
    
    if sr:
        ani.save('result.mp4')
    
    plt.show()

def convergence_plot(agents, function, lb, ub):
    """
    Generates a convergence plot image of the agents for all iterations
    And stores the plot in a file with the name of the function, the number of agents, and the number of iterations and dimension
    :param agents: agents
    :param function: function
    :param lb: lower bound
    :param ub: upper bound
    """

    side = np.linspace(lb, ub, 100)
    X, Y = np.meshgrid(side, side)
    Z = np.array([np.array([function([X[i][j], Y[i][j]])
                            for j in range(len(X))])
                  for i in range(len(X[0]))])

    fig = plt.figure()
    plt.axes(xlim=(lb, ub), ylim=(lb, ub))
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.colorbar()

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    plt.title(function.__name__, loc='left')

    for i in range(1, len(agents)):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))
        plt.title('iteration: {}'.format(i), loc='right')

        plt.savefig('convergence_{}_{}_{}_{}.png'.format(function.__name__, len(agents), len(agents[0]), i))

    plt.show()

   