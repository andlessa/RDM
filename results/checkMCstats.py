#!/usr/bin/env python3

"""
Check Monte Calor statistics in CheckMate output.
"""

import os
import numpy as np

def checkStats(checkmateOutput):
    """
    Check Monte Calor statistics in CheckMate output.

    :param checkmateOutput: CheckMate output file (total_results.txt)

    :return: True if succesful, False otherwise
    """

    if not os.path.isfile(checkmateOutput):
        print("Files %s not found" %checkmateOutput)
        return False

    # Get CMS-SUS-16-032 data:
    data = np.genfromtxt(checkmateOutput,names=True,
            dtype=None,encoding=None)

    data = np.delete(data,np.where(data['sr'] == 'Combined'))
    ibest = np.argmax(data['rexp'])
    pt = data[ibest]
    if not pt['s']:
        ratio = 100.0
    else:
        ratio = pt['signalsumofweights']/pt['s']
    nEvts = pt['signalsumofweights']

    return ratio,nEvts



if __name__ == "__main__":

    import argparse
    ap = argparse.ArgumentParser( description=
            "Compute combined limit and add to checkmate output" )
    ap.add_argument('-f', '--file', required = True,
            help='CheckMate output file (total_result.txt)')
    ap.add_argument('-v', '--verbose', default='error',
            help='verbose level (debug, info, warning or error). Default is error')

    args = ap.parse_args()
    rMC,nEvts = checkStats(os.path.abspath(args.file))
    print(os.path.abspath(args.file),rMC,nEvts)
