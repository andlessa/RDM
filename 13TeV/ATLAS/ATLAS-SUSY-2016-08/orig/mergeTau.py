#!/usr/bin/env python3

import glob
from smodels_utils.dataPreparation.dataHandlerObjects import hbar

data, expdata = {}, {}

f=open("HEPData-ins1630632-v2-Table_21.csv" )
lines=f.readlines()
f.close()

for line in lines:
    if line[0]=='#' or 'Observed' in line:
        continue
    line = line.strip()
    if line=="":
        continue
    tokens = line.split(",")
    mgluino = float(tokens[0]) ## ns
    mneutralino = float(tokens[1]) ## GeV
    limit = float(tokens[2])/1000. ## pb
    if not mgluino in data.keys():
        data[mgluino]={}
    data[mgluino][mneutralino]=limit
#    f.write ( "%f,%f,%f\n" % ( mgluino, mneutralino, limit ) )
#f.close()


files = { 1400: "HEPData-ins1630632-v2-Table_13.csv", 2000: "HEPData-ins1630632-v2-Table_14.csv" }

expected = False

for mgluino,filename in files.items():
    if not mgluino in data.keys():
        data[mgluino]={}
    f=open(filename)
    lines=f.readlines()
    f.close()
    for line in lines:
        if line[0]=='#':
            continue
        if 'sigma' in line: ## currently we ignore the +- 1 sigma
            break
        if 'expected' in line:
            expected = True
        if "Neutrali" in line:
            continue
        line = line.strip()
        if len(line)==0:
            continue
        tokens = line.split(",")
        neutralino,limit = float(tokens[0]),float(tokens[1])
        if expected:
            expdata[mgluino][neutralino]=limit
        else:
            data[mgluino][neutralino]=limit

f=open("mTau.csv","w" )
f.write ( "# mgluino (GeV), mneutralino (GeV), limit (pb)\n" ) 
for mgluino, values in data.items():
    for neutralino, limit in values.items():
        f.write ( "%f,%f,%f\n" % ( mgluino, neutralino, limit ) )

f.close()
f=open("mTauExp.csv","w" )
f.write ( "# mgluino (GeV), mneutralino (GeV), limit (pb)\n" ) 
for mgluino, values in expdata.items():
    for neutralino, limit in values.items():
        f.write ( "%f,%f,%f\n" % ( mgluino, neutralino, limit ) )

f.close()
