from MatPlot_lib.matplot_rodam import *

FREQ = 20; # [Hz]
AMP  = 2;  # [Volts]
LEN_SEC = 2; # [seconds] 


def main():
    test_lib = MatPlot()
    test_lib.plot_sin(
        FREQ, AMP, 1, "sin plot", "time in [s]", "Amplitude i n [v]",)

    test_lib.plot_sin

if __name__ == '__main__':
    main()


