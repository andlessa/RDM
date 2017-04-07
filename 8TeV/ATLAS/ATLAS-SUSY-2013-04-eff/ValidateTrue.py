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

lista = [ name for name in os.listdir(os.getcwd()) if 'Grid' in name ]
TOPO = ['T1bbbb.txt','T1btbt.txt','T1tttt.txt','T2ttoff.txt','T2tt.txt','T5.txt','T5WWoff.txt','T5WW.txt','T5ZZ.txt','T6bbWW.txt']
for name in lista:
  for topo in TOPO:
    Line_Remove(name+'/'+topo, kick, new)
