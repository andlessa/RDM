#!/usr/bin/env python3

import math

f=open("HEPData-ins1630632-v2-Table_9.csv" )
lines=f.readlines()
f.close()

expected=False
obsValues,expValues=[],[]

for line in lines:
    if line[0]=='#':
        continue
    if "Observed" in line:
        continue
    if "Expected" in line:
        expected = True
        continue
    line = line.strip()
    tokens = line.split(",")
    if len(tokens)<2:
        continue
    values = [ float(tokens[1]),10**(float(tokens[0])) ]
    if expected:
        expValues.append ( values)
    else:
        obsValues.append ( values )

f=open("obs9.csv","w")
for i in obsValues:
    f.write ( "%.2f,%f\n" % (i[0],i[1]) )
f.close()
f=open("exp9.csv","w")
for i in expValues:
    f.write ( "%.2f,%f\n" % (i[0],i[1]) )
f.close()
