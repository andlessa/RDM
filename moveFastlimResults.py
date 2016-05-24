#!/usr/bin/python

""" A script that splits up the results into official and fastlim.
    (maybe later even more packages ) """

import os
import commands

def run ( cmd ):
    commands.getoutput ( cmd )

## first we copy ourself to /tmp
cmd="cp ./moveFastlimResults.py /tmp/"
commands.getoutput ( cmd )

## then make the fastlim dir
fastlimdir = "../smodels-fastlim"
if os.path.exists ( fastlimdir ):
    cmd = "rm -r %s" % fastlimdir
    run ( cmd )

cmd="mkdir %s" % fastlimdir 
run ( cmd )

## now traverse the *TeV dirs
for i in os.listdir("."):
    if not os.path.isdir ( i ) or i in [ ".git" ]:
        continue
    for j in os.listdir ( i ):
        print i,j
