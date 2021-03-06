#!/usr/bin/env python3
# coding: utf-8

# In[1]:


import glob,sys


# In[2]:


for f in glob.glob(sys.argv[1]+'/*.slha'):
    with open(f,'r') as ff:
        data  = ff.readlines()
    for i,l in enumerate(data):
        if '3    5  16  5000522' in l:
            l = l.replace('3    5  16  5000522','2    5  5000522')            
        elif '3    4  15  5000522' in l:
            l = l.replace('3    4  15  5000522','2    15  5000522')            

        elif 'XSECTION' in l:
            if '~chi1~ ~chi1' in l:
                l = l.replace('~chi1~ ~chi1','-5000521 5000521')
            elif 'lq~ lq' in l:
                l = l.replace('lq~ lq','-42 42')
            elif 'lq ta' in l:
                l = l.replace('lq ta','42 -15')
            elif 'lq~ ta' in l:
                l = l.replace('lq~ ta','-42 15')
        elif 'BLOCK QNUMBERS 42 #  lq' in l:
            data[i+5] = '      5 1 # Z2-parity\n'
        data[i] = l
    with open(f.replace(sys.argv[1],sys.argv[2]),'w') as ff:
        for l in data: ff.write(l)


# In[ ]:




