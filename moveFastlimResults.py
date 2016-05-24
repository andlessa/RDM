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

def isFastlim ( path ):
    print "%s is fastlim!" % path
    cmd = "mv %s %s" % ( path, fastlimdir )
    # commands.getoutput ( cmd )

## now traverse the *TeV dirs
for i in os.listdir("."):
    if not os.path.isdir ( i ) or i in [ ".git" ]:
        continue
    for j in os.listdir ( i ):
        fulldir = os.path.join ( i, j )
        if not os.path.isdir ( fulldir ):
            continue
        for analysis in os.listdir ( fulldir ):
            fullpath = os.path.join ( fulldir, analysis )
            gif=open ( fullpath + "/globalInfo.txt" )
            lines=gif.readlines()
            for line in lines:
                if "fastlim" in line:
                    isFastlim ( fullpath )
                    break
            gif.close()

