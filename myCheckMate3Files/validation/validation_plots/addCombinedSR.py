#!/usr/bin/env python

"""
Simple code for adding the combined signal region to CheckMate results in total_results.txt

It assumes the simplified likelihood framework, using
the covariant matrix for all signal regions.
"""

# %% Imports
from getCombinedLimit import addCombined
import sys,os,glob
import numpy as np


# %% Add to CMS-SUS-16-032 results:
analysis = 'cms_sus_16_032'
#Order of the bins in the covariance matrix for the non-compressed signal regions:
orderSRs = {'1' : 'HT_200_MCT_150', '2' : 'HT_200_MCT_250', '3' : 'HT_200_MCT_350', '4' : 'HT_200_MCT_450',
            '5' : 'HT_500_MCT_150', '6' : 'HT_500_MCT_250', '7' : 'HT_500_MCT_350', '8' : 'HT_500_MCT_450',
            '9' : 'HT_500_MCT_600', '10' : 'HT_1000_MCT_150', '11' : 'HT_1000_MCT_250', '12' : 'HT_1000_MCT_350',
            '13' : 'HT_1000_MCT_450', '14' : 'HT_1000_MCT_600', '15' : 'HT_1000_MCT_800'}
#File and histogram containing the covariance matrix
histoname = 'Canvas_1/Cov'
covmatrix = './CMS_data/CMS-SUS-16-032_Figure-aux_003.root'
label = 'Combined_noncomp'


# %% Loop over files and add the combination for the non-compressed SRs
folder = '../validation_results/cms_sus_16_032/'
for subdir in os.listdir(folder):
    filename = os.path.abspath(os.path.join(folder,subdir,'evaluation','total_results.txt'))
    if not os.path.isfile(filename):
        print('File %s not found' %filename)
        continue
    addCombined(filename,analysis,covmatrix,histoname,orderSRs,label)




# %% Order of the bins in the covariance matrix for the compressed signal regions:
orderSRs = {'1' : '1b_ETmiss_250', '2' : '1b_ETmiss_300', '3' : '1b_ETmiss_500', '4' : '1b_ETmiss_750', '5' : '1b_ETmiss_1000',
 '6' : '2b_ETmiss_250', '7' : '2b_ETmiss_250_HT_100', '8' : '2b_ETmiss_300', '9' : '2b_ETmiss_300_HT_100', '10' : '2b_ETmiss_500', '11' : '2b_ETmiss_500_HT_100',
 '12' : '1c_ETmiss_250', '13' : '1c_ETmiss_300', '14' : '1c_ETmiss_500', '15' : '1c_ETmiss_750', '16' : '1c_ETmiss_1000',
 '17' : '2c_ETmiss_250', '18' : '2c_ETmiss_250_HT_100', '19' : '2c_ETmiss_300', '20' : '2c_ETmiss_300_HT_100', '21' : '2c_ETmiss_500', '22' : '2c_ETmiss_500_HT_100', '23' : '2c_ETmiss_750', '24' : '2c_ETmiss_750_HT_100',
 '25' : 'NSV_ETmiss_250', '26' 'NSV_ETmiss_300': , '27' : 'NSV_ETmiss_500', '28' : 'NSV_ETmiss_750', '29' : 'NSV_ETmiss_1000',
 '30' : '0b_ETmiss_300', '31' : '0b_ETmiss_500', '32' : '0b_ETmiss_750', '33' : '0b_ETmiss_1000', '34' : '0b_ETmiss_1250'}
#File and histogram containing the covariance matrix
histoname = 'Canvas_1/Cov'
covmatrix = './CMS_data/CMS-SUS-16-032_Figure-aux_004.root'
label = 'Combined_comp'


# %% Loop over files and add the combination for the non-compressed SRs
folder = '../validation_results/cms_sus_16_032/'
for subdir in os.listdir(folder):
    filename = os.path.abspath(os.path.join(folder,subdir,'evaluation','total_results.txt'))
    if not os.path.isfile(filename):
        print('File %s not found' %filename)
        continue
    addCombined(filename,analysis,covmatrix,histoname,orderSRs,label)
