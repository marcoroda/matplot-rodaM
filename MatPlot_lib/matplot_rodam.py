import os
import matplotlib.pyplot as plt
import numpy as np

class MatPlot(object):
    """ class: matplot_rodam
    
    Provides various methods for plotting stuff
    """

    def __init__(self):
        """ init procedure """
        print("object matplot_rodam created")

    def plot_sin(self, freq, amp, len_seconds, plot_title, x_title, y_title):
        ''' Plot a Sin(x) for a given input frequency and amplitude ''' 
        time = np.arange(0, len_seconds, (1/1000))
        signal = np.sin(2 * np.pi * freq * time)
        plt.plot(time, signal)
        # Set titles
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.title(plot_title)
        # show plot
        plt.show()

    def plot_gp(self, y, plot_title, x_title, y_title):
        ''' Plots a General Purpose graph '''
        x = np.arange(0, len(y))
        plt.plot(x, y)
        # Set titles
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.title(plot_title)
        # show plot
        plt.show()


#### for testing MAIN ####
def main():
    mat_plot = MatPlot()

if __name__ == '__main__':
    main()
