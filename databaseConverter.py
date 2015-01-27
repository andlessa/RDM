#!/usr/bin/env python

"""
.. module:: databaseConverter
   :synopsis: uesed to create info.txt,sms.py,sms.root and newSms.py.

.. moduleauthor:: Michael Traub <michael.traub@gmx.at>

"""   

import sys
import os

sys.path.append(os.path.abspath('../smodels-utils'))
sys.path.append(os.path.abspath('8TeV/ATLAS/ATLAS_SUSY_2013_05'))

import convert