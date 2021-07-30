#!/usr/bin/env python3

"""Simple code for running CheckMATE over a set of SLHA files."""

#Uses an input file to loop over input files and run CheckMATE over them.
#The calculation goes through the following steps
# 1) Generate input steering cards for CheckMATE
# 2) Run CheckMATE for each card
# 3) Move results to output folder

#First tell the system where to find the modules:
import sys,os,glob,shutil
import logging
import time,datetime

FORMAT = '%(levelname)s in %(module)s.%(funcName)s() in %(lineno)s: %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def main(inputFolder,outputFolder):

    inputFolder = os.path.abspath(inputFolder)
    outputFolder = os.path.abspath(outputFolder)
    if not os.path.isdir(outputFolder):
        os.makedirs(outputFolder)

    for f in glob.glob(os.path.join(inputFolder,'*.slha')):
        with open(f,'r') as ff:
            data  = ff.readlines()
        for i,l in enumerate(data):
            if '3    5  16  5000522' in l:
                l = l.replace('3    5  16  5000522','2    5  5000522')
            elif '3    4  15  5000522' in l:
                l = l.replace('3    4  15  5000522','2    15  5000522')

            elif 'XSECTION' in l:
                if '~chi1~ ~chi1' in l:
                    l = l.replace('~chi1~ ~chi1','-5000521 5000521')
                elif 'lq~ lq' in l:
                    l = l.replace('lq~ lq','-42 42')
                elif 'lq ta' in l:
                    l = l.replace('lq ta','42 -15')
                elif 'lq~ ta' in l:
                    l = l.replace('lq~ ta','-42 15')
            elif 'BLOCK QNUMBERS 42 #  lq' in l:
                data[i+5] = '      5 1 # Z2-parity\n'
            data[i] = l
        with open(f.replace(inputFolder,outputFolder),'w') as ff:
            for l in data: ff.write(l)


if __name__ == "__main__":

    import argparse
    ap = argparse.ArgumentParser( description=
            "Modify SLHA files for running with SModelS." )
    ap.add_argument('-f', '--inputFolder', default='slha_BS1p',
            help='path to the input folder containing the SLHA files to be modified.')
    ap.add_argument('-o', '--oututFolder', default='slha_BS1p_smodels',
            help='path to the output folder, where the modified files will be stored.')


    t0 = time.time()

    args = ap.parse_args()

    t0 = time.time()

    args = ap.parse_args()
    output = main(args.inputFolder,args.oututFolder)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
