#!/usr/bin/env python3

import glob
from smodels_utils.dataPreparation.dataHandlerObjects import hbar

f=open("HEPData-ins1630632-v2-Table_20.csv" )
lines=f.readlines()
f.close()
data, expdata = {}, {}

for line in lines:
    if line[0]=='#' or 'Observed' in line:
        continue
    line = line.strip()
    if line=="":
        continue
    tokens = line.split(",")
    lifetime = 10**float(tokens[0]) ## ns
    mgluino = float(tokens[1]) ## GeV
    limit = float(tokens[2])/1000. ## pb
    if not mgluino in data.keys():
        data[mgluino]={}
    data[mgluino][lifetime]=limit
f.close()

files = { 1400: "HEPData-ins1630632-v2-Table_10.csv", 2000: "HEPData-ins1630632-v2-Table_11.csv" }

expected = False

for mgluino,filename in files.items():
    data[mgluino]={}
    f=open(filename)
    lines=f.readlines()
    f.close()
    for line in lines:
        if line[0]=='#':
            continue
        if 'sigma' in line: ## currently we ignore the +- 1 sigma
            break
        if 'xpected' in line:
            expected = True
            continue
        if "Lifetime" in line:
            continue
        line = line.strip()
        if len(line)==0:
            continue
        tokens = line.split(",")
        lifetime,limit = float(tokens[0]),float(tokens[1])
        if expected:
            if not mgluino in expdata.keys():
                expdata[mgluino]={}
            expdata[mgluino][lifetime]=limit
        else:
            if not mgluino in data.keys():
                data[mgluino]={}
            data[mgluino][lifetime]=limit

f=open("mDelta100.csv","w" )
f.write ( "# mgluino (GeV), width (GeV), limit (pb)\n" ) 
for mgluino, values in data.items():
    for lifetime, limit in values.items():
        f.write ( "%f,%g,%f\n" % ( mgluino, hbar/lifetime, limit ) )
f.close()
f=open("mDelta100exp.csv","w" )
f.write ( "# mgluino (GeV), width (GeV), limit (pb)\n" ) 
for mgluino, values in expdata.items():
    for lifetime, limit in values.items():
        f.write ( "%f,%g,%f\n" % ( mgluino, hbar/lifetime, limit ) )

f.close()
