import os, sys

thisDirectory = os.getcwd()
fileInFolder = os.listdir(thisDirectory)

mapsList = []
for file in fileInFolder:
    if '.txt' in file  and 'Eff' in file and '~' not in file:   # skipping the weird ~ objects
        mapsList.append(file)
mapsList.sort()                          # Sort Alphabetically


accList = []
for file in fileInFolder:
    if '.txt' in file  and 'Acc' in file and '~' not in file:   # skipping the weird ~ objects
        accList.append(file)
accList.sort()

regionsList = []
for nome in mapsList:
    Nome = nome[4:-4]
    regionsList.append(Nome)




def converting_Acc_Eff(name) :
    accMap = 'Acc_'+ name + '.txt'
    print accMap
    effMap = 'Eff_' + name + '.txt'
    print effMap
    mappaAcc = open(accMap,"r")
    mappaEff = open(effMap,"r")
    

    finalList =[]
    finalListAcc = []
    motherMass= []
    daughterMass = []
    acceptance =[]
    acceptance_real = []
    efficiency = []
    efficiency_real =[]
    

    for line in mappaEff:
    
        lineElement = line.split('\t')
        convertedLineElement1 = []
        for element in lineElement:
            if '\n' in element:
                element = element.replace('\n','')
            if element and element !='\n':
                if 'x' not in element and 'y' not in element:
                    convertedLineElement1.append(element)
        finalList.append(convertedLineElement1)

    for line in finalList:
        if (len(line)>2):
            motherMass.append(line[0])
            daughterMass.append(line[3])
            efficiency.append(line[6])





    for line in mappaAcc:
        lineElement = line.split('\t')
        convertedLineElement2 = []
        for element in lineElement:
            #print element
            if '\n' in element:
                element = element.replace('\n','')

            if element and element !='\n':
                if 'x' not in element and 'y' not in element:
                    convertedLineElement2.append(element)
        finalListAcc.append(convertedLineElement2)

    for line in finalListAcc:
        if (len(line)>2):
            acceptance.append(line[6])

    for eff in efficiency:
        eff_num = float(eff)
        eff_num = eff_num / 100.
        efficiency_real.append(eff_num)
        
    for acc in acceptance:
        acc_num = float(acc)
        acc_num = acc_num /100.
        acceptance_real.append(acc_num)

    convertedMap = open(name+'.txt',"w")     #  Output name
    for i in range(0,len(motherMass)):
        convertedMap.write(str(motherMass[i]) +'  '+ str(daughterMass[i]) + '  ' + str(efficiency_real[i]*acceptance_real[i])+'\n')

    convertedMap.close()



print regionsList
for region in regionsList:
    print region
    converting_Acc_Eff(region)










'''

helper_to_Convert = open('helper_to_Convert.txt','w')

listOfTopo = ['T1tttt']

for dataFile in mapsList:
    dataset = dataFile.replace(".txt","").replace("HEPdata.","").replace(".","_")
    for topo in listOfTopo:
        helper_to_Convert.write( topo + '.efficiencyMap.setSource( ' + dataFile + ', "txt" , objectName =  "' + dataFile + '", index = None , dataset = "' + dataset + '" ) ' + '\n')
        helper_to_Convert.write( topo + '.efficiencyMap.setStatistics( observedN=  ,  expectedBG=   , bgError=   )'  + '\n' + '\n'+ '\n')

helper_to_Convert.close()


'''












