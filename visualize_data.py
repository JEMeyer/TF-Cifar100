import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import tkinter


def load_points(path):
    '''
    Input: 
      path: String. Path to csv file
    Returns:
      data: np.ndarray. Matrix of data
    '''
    data = np.loadtxt(path)
    return data


def plot_points(data):
    '''
    Input:
      data: np.ndarray. Matrix of data where each col is a dimension (x or y)
    Returns:
      Nothing
    '''
    numCols = data.shape[1]
    x, y1 = np.split(data, numCols, axis=1)

    plt.plot(x, y1)

    plt.xlabel('Number of Iterations', fontsize=14)
    plt.ylabel('Loss', fontsize=14)
    plt.title('Base Network', fontsize=18)

    plt.legend(['Average Loss'], loc='upper left')
    plt.show()


def plot_1D_points(points):
    '''
    where 'points' is a list of [y_1...y_n] points,
    plot them in 2D space, using their index in the list as
    the x value, and the point, y_n, as the y value
    '''
    fig = plt.figure()
    x, y = zip(*[(x, y) for x, y in enumerate(points)])
    ax = fig.gca()
    ax.plot(x, y)
    ax.legend()
    plt.show()


def save_graph(data, title, output):
    '''
    Input:
      data: np.ndarray. Matrix of data where each col is a dimension (x or y)
    Returns:
      Nothing
    '''
    numCols = data.shape[1]
    x, y1 = np.split(data, numCols, axis=1)

    plt.plot(x, y1)

    plt.xlabel('Number of Iterations', fontsize=14)
    plt.ylabel('Loss', fontsize=14)
    plt.title(title, fontsize=18)

    plt.legend(['Loss'], loc='upper left')
    plt.savefig(output, bbox_inches='tight')


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    title = sys.argv[2]
    output = sys.argv[3]
    data = load_points(path)
    save_graph(data, title, output)
