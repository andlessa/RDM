import os,sys

'''
This scripts allows to write automatically the convert.py info for the implementation of the EM implementation
i.e. copy and paste the lines given as output by this script under the general information in convert.py
F.A.
'''


Dataset = ['mT2-150-DF', 'WWc-DF', 'mT2-120-DF', 'WWa-SF','mT2-150-SF', 'WWa-DF','WWb-SF','WWb-DF','mT2-90-SF','mT2-120-SF','WWc-SF','Zjets','mT2-90-DF']

Topo = [ {'Topo' :  'TSlepSlep',             'P' :'1',                            'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'x005',                          'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'x025',                          'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'x05',                           'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'x075',                          'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'x095',     			  'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTASleptonNeutralino5',       'T':'txt'}, 
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTASleptonNeutralino10',      'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTASleptonNeutralino15',      'T':'txt'},
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTACharginoSlepton5',         'T':'txt'}, 
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTACharginoSlepton10',        'T':'txt'}, 
         {'Topo' :  'TChipChimSlepSnu',      'P':'DELTACharginoSlepton15',        'T':'txt'}    ]

Data = [ {'SR':'mT2-90-SF'  ,'Events':'observedN=33, expectedBG=38.2, bgError=5.1'},
         {'SR':'mT2-90-DF'  ,'Events':'observedN=21, expectedBG=23.3, bgError=3.7'},
         {'SR':'mT2-120-SF' ,'Events':'observedN=5, expectedBG=8.9, bgError=2.1'},
         {'SR':'mT2-120-DF' ,'Events':' observedN=5, expectedBG=3.6, bgError=1.2'},
         {'SR':'mT2-150-SF' ,'Events':'observedN=3, expectedBG=3.2, bgError=0.7'},
         {'SR':'mT2-150-DF' ,'Events':'observedN=2, expectedBG=1.0, bgError= 0.5'},
         {'SR':'WWa-SF' ,'Events':'observedN=73, expectedBG=86.5, bgError=7.4'},
         {'SR':'WWa-DF' ,'Events':'observedN=70, expectedBG=73.6, bgError=7.9'},
         {'SR':'WWb-SF' ,'Events':'observedN=26, expectedBG=30.2, bgError=3.5'},
         {'SR':'WWb-DF' ,'Events':'observedN=17, expectedBG=18.1, bgError=2.6'},
         {'SR':'WWc-SF' ,'Events':'observedN=10, expectedBG=20.3, bgError=3.5'},
         {'SR':'WWc-DF' ,'Events':' observedN=11, expectedBG=9.0, bgError=2.2'},
         {'SR':'Zjets' ,'Events':'observedN=1, expectedBG=1.4, bgError=0.6'},
]

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
        orig = 'orig/atlas_susy_2013_11_'+TOPO
        files = '/MA5_EM_'+TOPO+'_'+dataset['SR']+ext+'"'
        orig = orig+files
    


    print TOPO+'.efficiencyMap.setSource("'+orig+', "'+type+'", objectName ="'+objectName +'", index = None, dataset="'+ dataset['SR']+'")'
    print TOPO+'.efficiencyMap.setStatistics('+dataset['Events']+')'


for datas in Data:
  for name in Topo:
    TOPO = name['Topo']
    Plane = name['P']
    Type = name['T']
    ConvertPy_Writer(TOPO, Plane, Type, datas)
  print 'databaseCreator.create()'

        
