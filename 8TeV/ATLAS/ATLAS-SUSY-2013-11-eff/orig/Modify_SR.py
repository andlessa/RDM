import os,sys

here = os.getcwd()

lista = [files for files in os.listdir(here) if '.dat' in files]

print lista
for elem in lista:
    inn = open(elem,'r')
    lines = inn.readlines()
    inn.close()

    out = open(elem,'w')
    for line in lines:
        if ('#' not in line):
           out.write(line)


