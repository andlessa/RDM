#
# Select graphs from a canvas and save selection to output files.
# Possible responses to list of input graphs:
#    <CR> or ^D : skip graph
#    "=": save graph with existing name
#    any other string: save graph & use the string as a new name
#
import ROOT
import os,sys

tf = ROOT.TFile(sys.argv[1])

canvases = [ ]
for k in tf.GetListOfKeys():
    o = k.ReadObj()
    if o.InheritsFrom(ROOT.TVirtualPad.Class()):
        canvases.append(o)

if len(canvases)!=1:
    print "No or >1 canvases!"
    print canvases
    sys.exit(1)

cnv = canvases[0]
cnv.Draw()
cnv.Update()

print 'ciao'
graphs = [ ]
for p in cnv.GetListOfPrimitives():
    if p.InheritsFrom(ROOT.TGraph.Class()):
        graphs.append(p)

print " "
outgraphs = [ ]
for g in graphs:
    sys.stdout.write("{0:15s} fcol={1:4d} lcol={2:4d} style={3:4d} width={4:4d}  ".format(g.GetName(),g.GetFillColor(),g.GetLineColor(),g.GetLineStyle(),g.GetLineWidth()))
    try:
        re = raw_input("Keep graph with name ...? ")
        if re!="":
            if re=="=":
                if g.GetName().strip()=="":
                    print "Existing name is empty - skipping graph"
                    continue
                re = g.GetName()
            outgraphs.append(g.Clone(re))
    except EOFError:
        print ""
        pass

if outgraphs:
    of = ROOT.TFile("federico-graphs.root","recreate")
    for g in outgraphs:
        g.Write()
    of.Close()
