#!/usr/bin/python

import ROOT
from smodels.tools.physicsUnits import fb,pb

execfile("T2bbWW_2Eqmotherx_Eqlspy.py")

xmin = min ( [ i["axes"][0] for i in validationData ] )
xmax = max ( [ i["axes"][0] for i in validationData ] )
ymin = min ( [ i["axes"][1] for i in validationData ] )
ymax = max ( [ i["axes"][1] for i in validationData ] )

xmin=150
xmax=200
ymin=0
ymax=60
n=1

h=ROOT.TH2F("h","h",100,xmin,xmax,100,ymin,ymax)
h.Draw()
for ctr,i in enumerate ( validationData ):
    if ctr % n  != 0: 
        continue
    print i["axes"],i["UL"]
    l=ROOT.TLatex()
    l.SetTextSize(.025)
    l.DrawLatex ( i["axes"][0], i["axes"][1], "%.1f" % i["UL"].asNumber(pb) )

ROOT.c1.Print ( "draw.png" )
