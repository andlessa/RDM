import os,sys

'''
This scripts allows to write automatically the convert.py info for the implementation of the EM implementation
i.e. copy and paste the lines given as output by this script under the general information in convert.py
(see convert.py attached as reference).
F.A.
'''


Dataset = ['3NJet6_1000HT1250_200MHT300',
           '3NJet6_1000HT1250_300MHT450',
           '3NJet6_1000HT1250_450MHT600',
           '3NJet6_1000HT1250_600MHTinf',
           '3NJet6_1250HT1500_200MHT300',
           '3NJet6_1250HT1500_300MHT450',
           '3NJet6_1250HT1500_450MHTinf',
           '3NJet6_1500HTinf_200MHT300',
           '3NJet6_1500HTinf_300MHTinf',
           '3NJet6_500HT800_200MHT300',
           '3NJet6_500HT800_300MHT450',
           '3NJet6_500HT800_450MHT600',
           '3NJet6_500HT800_600MHTinf',
           '3NJet6_800HT1000_200MHT300',
           '3NJet6_800HT1000_300MHT450',
           '3NJet6_800HT1000_450MHT600',
           '3NJet6_800HT1000_600MHTinf',
           '6NJet8_1000HT1250_200MHT300',
           '6NJet8_1000HT1250_300MHT450',
           '6NJet8_1000HT1250_450MHTinf',
           '6NJet8_1250HT1500_200MHT300',
           '6NJet8_1250HT1500_300MHT450',
           '6NJet8_1250HT1500_450MHTinf',
           '6NJet8_1500HTinf_200MHT300',
           '6NJet8_1500HTinf_300MHTinf',
           '6NJet8_500HT800_200MHT300',
           '6NJet8_500HT800_300MHT450',
           '6NJet8_500HT800_450MHTinf',
           '6NJet8_800HT1000_200MHT300', 
           '6NJet8_800HT1000_300MHT450', 
           '6NJet8_800HT1000_450MHTinf', 
           '8NJetinf_1000HT1250_200MHTinf', 
           '8NJetinf_1250HT1500_200MHTinf', 
           '8NJetinf_1500HTinf_200MHTinf', 
           '8NJetinf_500HT800_200MHTinf', 
           '8NJetinf_800HT1000_200MHTinf']

Topo = [ {'Topo' :  'T1qqqq', 'P' : 'NO',      'T':'root'},
         {'Topo' :  'T1tttt', 'P' : 'NO',      'T':'root'},
         {'Topo' :  'T2qq',   'P' : 'NO',      'T':'root'},
         {'Topo' :  'T5WW',   'P':'x005',      'T':'txt'},
         {'Topo' :  'T5WW',   'P':'x05',       'T':'txt'},
         {'Topo' :  'T5WW',   'P':'x095',      'T':'txt'},
         {'Topo' :  'T5ZZ',   'P':'x005',      'T':'txt'},
         {'Topo' :  'T5ZZ',   'P':'x05',       'T':'txt'},
         {'Topo' :  'T5ZZ',   'P':'x095',      'T':'txt'} ]

Data = [ {'SR':'3NJet6_500HT800_200MHT300','Events':'observedN=6159, expectedBG=6088, bgError=665' },
         {'SR':'3NJet6_500HT800_300MHT450' ,'Events':'observedN=2305, expectedBG=2278, bgError=266 '},
        {'SR':'8NJetinf_1500HTinf_200MHTinf' ,'Events':'observedN=2, expectedBG=3.3, bgError=4.7'},
        {'SR':'8NJetinf_1250HT1500_200MHTinf' ,'Events':'observedN=5, expectedBG=7.1, bgError=3.8 '},
        {'SR':'8NJetinf_1000HT1250_200MHTinf' ,'Events':' observedN=8, expectedBG=5.6, bgError=2.3 '},
        {'SR':'8NJetinf_800HT1000_200MHTinf' ,'Events':'observedN=9, expectedBG=8.3, bgError=3.4'},
        {'SR':'8NJetinf_500HT800_200MHTinf' ,'Events':'observedN=8, expectedBG=4.8, bgError=2.3'},
        {'SR':'6NJet8_1500HTinf_300MHTinf' ,'Events':'observedN=3, expectedBG=7.9, bgError=3.6'},
        {'SR':'6NJet8_1500HTinf_200MHT300' ,'Events':'observedN=18, expectedBG=21.1, bgError=8.1'},
        {'SR':'6NJet8_1250HT1500_450MHTinf' ,'Events':'observedN=2, expectedBG=0.5, bgError=2.6'},
        {'SR':'6NJet8_1250HT1500_300MHT450' ,'Events':'observedN=5, expectedBG=9.4, bgError=3.6'},
        {'SR':'6NJet8_1250HT1500_200MHT300' ,'Events':'observedN=24, expectedBG=28.0, bgError=8.2'},
        {'SR':'6NJet8_1000HT1250_450MHTinf' ,'Events':'observedN=4, expectedBG=2.2, bgError=3.8'},
        {'SR':'6NJet8_1000HT1250_300MHT450' ,'Events':'observedN=20, expectedBG=21.6, bgError=5.8'},
        {'SR':'6NJet8_1000HT1250_200MHT300' ,'Events':'observedN=67, expectedBG=70, bgError=16'},
        {'SR':'6NJet8_800HT1000_450MHTinf' ,'Events':'observedN=4, expectedBG=6.0, bgError=2.8'},
        {'SR':'6NJet8_800HT1000_300MHT450' ,'Events':'observedN=35, expectedBG=28.6, bgError=6.9'},
        {'SR':'6NJet8_800HT1000_200MHT300' ,'Events':'observedN=111, expectedBG=124, bgError=29'},
        {'SR':'6NJet8_500HT800_450MHTinf' ,'Events':'observedN=9, expectedBG=0.8, bgError=3.3'},
        {'SR':'6NJet8_500HT800_300MHT450' ,'Events':'observedN=62, expectedBG=52, bgError=12'},
        {'SR':'6NJet8_500HT800_200MHT300' ,'Events':'observedN=266, expectedBG=290, bgError=65'},
        {'SR':'3NJet6_1500HTinf_300MHTinf' ,'Events':'observedN=39, expectedBG=29.7, bgError=5.8'},
        {'SR':'3NJet6_1500HTinf_200MHT300' ,'Events':'observedN=94, expectedBG=86, bgError=17'},
        {'SR':'3NJet6_1250HT1500_450MHTinf' ,'Events':'observedN=23, expectedBG=17.6, bgError=4.1'},
        {'SR':'3NJet6_1250HT1500_300MHT450' ,'Events':'observedN=38, expectedBG=42.8, bgError=9.5'},
        {'SR':'3NJet6_1250HT1500_200MHT300' ,'Events':'observedN=98, expectedBG=109, bgError=18'},
        {'SR':'3NJet6_1000HT1250_600MHTinf' ,'Events':'observedN=32, expectedBG=22.8, bgError=5.2'},
        {'SR':'3NJet6_1000HT1250_450MHT600' ,'Events':'observedN=34, expectedBG=32.3, bgError=6.1'},
        {'SR':'3NJet6_1000HT1250_300MHT450' ,'Events':'observedN=129, expectedBG=137, bgError=20'},
        {'SR':'3NJet6_1000HT1250_200MHT300' ,'Events':'observedN=335, expectedBG=305, bgError=41'},
        {'SR':'3NJet6_800HT1000_450MHT600inf' ,'Events':'observedN=52, expectedBG=54.8, bgError=9.7'},
        {'SR':'3NJet6_800HT1000_450MHT600' ,'Events':'observedN=124, expectedBG=108, bgError=15'},
        {'SR':'3NJet6_800HT1000_300MHT450' ,'Events':'observedN=305, expectedBG=330, bgError=40'},
        {'SR':'3NJet6_800HT1000_200MHT300' ,'Events':'observedN=808, expectedBG=777, bgError=107'},
        {'SR':'3NJet6_500HT800_600MHTinf' ,'Events':'observedN=62, expectedBG=57.4, bgError=11.2'},
        {'SR':'3NJet6_500HT800_450MHT600' ,'Events':'observedN=454, expectedBG=418, bgError=66'}, ]
    
Data = [ {'SR':'3NJet6_1000HT1250_200MHT300' ,'Events':'observedN=335, expectedBG=305, bgError=41'},
         {'SR':'3NJet6_800HT1000_450MHT600inf' ,'Events':'observedN=52, expectedBG=54.8, bgError=9.7'},]
def ConvertPy_Writer(topology, plane, type, dataset):
    objName = ''
    TOPO = ''
    ext =''
    orig = ''
    if plane == 'NO':
            TOPO = topology
    else:
            TOPO = topology+"_"+plane

    if (type == 'root'):
        objectName='h_EffAcc_'+dataset['SR']
        ext = '.root'
        orig = 'orig/SUS13012_XsecLimits_'+TOPO+ext+'"'
    else:
        objectName='None'
        ext = '.dat'
        orig = 'orig/'+TOPO
        files = '/MA5_EM_'+TOPO+'_'+dataset['SR']+ext+'"'
        orig = orig+files.replace('x005','Glu005Neu095').replace('x095','Glu095Neu005')
    


    print TOPO+'.efficiencyMap.setSource("'+orig+', "'+type+'", objectName ="'+objectName +'", index = None, dataset="'+ dataset['SR']+'")'
    print TOPO+'.efficiencyMap.setStatistics('+dataset['Events']+')'


for datas in Data:
  for name in Topo:
    TOPO = name['Topo']
    Plane = name['P']
    Type = name['T']
    ConvertPy_Writer(TOPO, Plane, Type, datas)
  print 'databaseCreator.create()'

        
