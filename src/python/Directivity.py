#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from SetupPlots import SetupPlots
import numpy as np
from matplotlib import pyplot as plt
from io import StringIO
from scipy.interpolate import interp1d

def read_cniihm_data(filename, frequency):
    with open(filename, 'r') as fd:
        freq_list = np.loadtxt(StringIO(unicode(fd.readline().strip())))    

    index = np.where(freq_list == frequency)[0][0]

    ang, D = np.loadtxt(filename, skiprows = 1, usecols = (0, 1+2*index), unpack = True)
    ang -= 180.0

    return ang, D

def run():
    SetupPlots()
    calc_D = np.loadtxt('data/directivity_calculated.csv',
                        skiprows = 1,
                        delimiter = ',')

    raw_ang = calc_D[:, 0].reshape(-1)
    calc_ang = np.concatenate((-raw_ang[1:][::-1], raw_ang))
    raw_LHCPp = calc_D[:, 1].reshape(-1)
    raw_LHCPn = calc_D[:, 2].reshape(-1)
    calc_LHCP = np.concatenate((raw_LHCPn[1:][::-1], raw_LHCPp))
    raw_RHCPp = calc_D[:, 3].reshape(-1)
    raw_RHCPn = calc_D[:, 4].reshape(-1)
    calc_RHCP = np.concatenate((raw_RHCPn[1:][::-1], raw_RHCPp))

    fcenter = 2070.0
    Friis = 52.14

    meas_ang_LHCP, meas_LHCP = read_cniihm_data('data/0029.txt', fcenter)
    meas_ang_RHCP, meas_RHCP = read_cniihm_data('data/0028.txt', fcenter)
    meas_LHCP += Friis
    meas_RHCP += Friis

    plt.plot(calc_ang, calc_LHCP, label = 'calculated LHCP')
    plt.plot(meas_ang_LHCP, meas_LHCP, label = 'measured LHCP')
    plt.plot(calc_ang, calc_RHCP, label = 'calculated RHCP')
    plt.plot(meas_ang_RHCP, meas_RHCP, label = 'measured RHCP')
    plt.xlim([-180, 180])
    plt.ylim([-45, 5])
    plt.legend()
    plt.grid(True)
    plt.xlabel('Elevation angle $\\theta$, deg')
    plt.ylabel('Directivity $D$, dBi')
    plt.xticks([-180, -135, -90, -45, 0, 45, 90, 135, 180])
    plt.gcf().set_size_inches([7.1, 4])
    plt.tight_layout()
    plt.savefig('../images/Directivity.pdf')
    
if __name__ == '__main__':
    run()
