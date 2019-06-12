#!/usr/bin/env python3

import glob

SRs= [ "c000", "c100", "c200", "c300" ]

def convert ( d ):
    files = glob.glob(d+"/*")
    print ( "dir", d, len(files),"files" )
    topo = d.replace("efficiencies_","")
    topo = topo.replace("T","")
    data = []
    for filename in files:
        with open(filename,"r") as f:
            lines=f.readlines() 
        for line in lines:
            tmp=line.split(" ")
            tokens=[]
            for t  in tmp:
                if t == "10000":
                    continue
                tokens.append ( float(t) ) 
            data.append ( tokens )
    write ( topo, data )

def write ( topo, data ):
    #print ( data )
    outfile = "efficiencies_%s.txt" % ( topo )
    f=open(outfile,"w")
    f.write ( "#  " )
    nmasses=len(data[0])-5
    for i in range(nmasses):
        f.write ( "Mass(GeV)  " )
    f.write ( "Width(GeV) " )
    f.write ( "  ".join ( SRs ) )
    f.write ( "\n" )
    for d in data:
        line=""
        for i in range(nmasses):
            line += "   %.1f" % d[i]
        for x in d[nmasses:]:
            line+="   %g" % x
        line += "\n" 
        f.write ( line )
    f.close() 

def writeOld ( topo, data ):
    #print ( data )
    for cSR,SR in enumerate(SRs):
        outfile = "eff_%s_%s.txt" % ( topo, SR )
        f=open(outfile,"w")
        f.write ( "## %s efficiencies\n" % topo )
        f.write ( "## x w effi\n" )
        for d in data:
            f.write ( "%.1f %g %g\n" % ( d[0], d[1], d[2+cSR] ) )
        f.close() 
            

def run():
    dirs = glob.glob("efficiencies_THSCP*")
    for d in dirs: ## [:1]:
        convert ( d )

if __name__ == "__main__":
    run()
