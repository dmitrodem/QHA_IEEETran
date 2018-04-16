#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from SetupPlots import SetupPlots
import numpy as np
from matplotlib import pyplot as plt

def run():
    SetupPlots()
    kw = {'comments': ['#', '!']}
    meas = np.loadtxt("data/chum.s2p", **kw)
    meas_freq = meas[:, 0]
    meas_s11 = 10*np.log10(meas[:, 1]**2 + meas[:, 2]**2)

    calc = np.loadtxt("data/50_hfss.s1p", **kw)
    calc_freq = calc[:, 0]
    calc_s11  = 10*np.log10(calc[:, 1]**2)

    plt.plot(calc_freq, calc_s11, label = 'Calculated')
    plt.plot(meas_freq, meas_s11, label = 'Measured')
    plt.ylim([-50, 0])
    plt.xlim([1, 3])
    plt.xticks([1.0, 1.5, 2.0, 2.5, 3.0])
    plt.grid(True)
    plt.legend()
    plt.xlabel('Frequency, GHz')
    plt.ylabel('Return loss $S_{11}, dB')
    plt.gcf().set_size_inches([3.5, 3])
    plt.tight_layout()
    plt.savefig("../images/Sparam.pdf")
    plt.close()
    
    fmin, fmax = tuple(meas_freq[np.where(meas_s11 < -20)[0][[0,-1]]])
    print "Measured:   F_c = {:4.2f}GHz, bw = ±{:4.2f}%".format(0.5*(fmin+fmax), 100*(fmax - fmin)/(fmax + fmin))

    fmin, fmax = tuple(calc_freq[np.where(calc_s11 < -20)[0][[0,-1]]])
    print "Calculated: F_c = {:4.2f}GHz, bw = ±{:4.2f}%".format(0.5*(fmin+fmax), 100*(fmax - fmin)/(fmax + fmin))

if __name__ == "__main__":
    run()
