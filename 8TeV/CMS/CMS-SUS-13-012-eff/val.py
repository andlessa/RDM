import os,sys

def Line_Remove(File, kick,new):
        a = open(File,'r')
        lines = a.readlines()
        a.close()

        n = open(File,'w')
        for line in lines:
            if (kick in line):
               line = line.replace(kick, new)
            n.write(line)
        n.close()


kick = 'validated: None'
new  = 'validated: True'
        

lista = [ name for name in os.listdir(os.getcwd()) if 'Jet' in name ]

topo = ['TChiWZ','TChiWW','TChiZZ','T1btbt','T2tt','T2ttoff','T2bb','T1bbbb','T5','T5WW','T5WWoff','T5ZZ','T6bbWW']
for name in lista:
  for TOPO in topo:
    Line_Remove(name+'/'+TOPO+'.txt', kick, new)
                                                                           
