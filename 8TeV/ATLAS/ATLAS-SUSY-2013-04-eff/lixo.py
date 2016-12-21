#!/usr/bin/env python


import glob,sys

for i in glob.glob('./*/T5ZZ.txt'):
   f = open(i,'r')
   data = f.readlines()
   f.close()
   f = open(i,'w')
   for il,l in enumerate(data):
      if 'axes' in l:
          l  = "axes: 2*Eq(mother,x)_Eq(inter0,0.05*x+0.95*y)_Eq(lsp,y);2*Eq(mother,x)_Eq(inter0,0.5*x+0.5*y)_Eq(lsp,y);2*Eq(mother,x)_Eq(inter0,0.95*x+0.05*y)_Eq(lsp,y)\n"
      f.write(l)
   f.close()

