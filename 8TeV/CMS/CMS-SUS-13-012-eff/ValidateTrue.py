kick = 'validated: None'
new  = 'validated: True'




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

lista = [ name for name in os.listdir(os.getcwd()) if 'NJet' in name ]
TOPO = ['T5bbbb','T5tttt','T6bbWW','T6bbWWoff']
for name in lista:
  for topo in TOPO:
    Line_Remove(name+'/'+topo+'.txt', kick, new)
