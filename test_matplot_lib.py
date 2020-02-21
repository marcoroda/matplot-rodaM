from MatPlot_lib.matplot_rodam import MatPlot
import numpy as np

FREQ = 5; # [Hz]
AMP  = 2;  # [Volts]
LEN_SEC = 2; # [seconds] 


def main():
    test_lib = MatPlot()
    test_lib.plot_sin(
        FREQ, AMP, 1, "sin plot", "time in [s]", "Amplitude i n [v]")

    # x = np.arange(0,10,0.01)
    y = np.arange(0,1,0.1)
    y2 = []
    for i in range(500):
        if i > 250:  
            y2.append(i*1)
        else:
            y2.append(i*0.5)



    test_lib.plot_gp(y2, "GP plot", "Number of Points", "y")

if __name__ == '__main__':
    main()


