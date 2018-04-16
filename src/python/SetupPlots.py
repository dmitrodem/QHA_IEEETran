#!/usr/bin/env python2

def SetupPlots():
    from cycler import cycler
    monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
                  cycler('linestyle', ['-', '--', ':', '-.']))
    from matplotlib import rc
    rc('font',**{'family':'serif'})
    rc('text', usetex=True)
    rc('text.latex',unicode=True)
    rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
    rc('text.latex',preamble='\usepackage[russian]{babel}')
    rc('axes', prop_cycle=monochrome)
