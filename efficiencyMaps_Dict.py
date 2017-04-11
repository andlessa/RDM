'''
List of homegrown EM present in the develop branch of SModelS database as of April 11th 2017
'''

HomeGrown_EM = [ {'analysis':'CMS-SUS-13-012'    , 'homeGrown':['TChiWW','TChiWZ','TChiZZ',
                                                                 'T1bbbb','T1btbt',
                                                                 'T2bb','T2tt','T2ttoff',
                                                                 'T5WW','T5WWoff','T5ZZ','T5',
                                                                 'T6bbWW'],
                                                   'official' :['T1','T2','T1tttt','T1ttttoff']},
                  
                 {'analysis':'ATLAS-SUSY-2013-04', 'homeGrown':['T1btbt','T1bbbb','T2tt','T2ttoff','T5WW','T5WWoff','T5ZZ','T5'],
                                                   'official' :['T1tttt'] },

                 {'analysis':'ATLAS-SUSY-2013-11', 'homeGrown':['TSlepSlep','TChiWW','TChipChimSlepSnu'],
                                                   'official' :['']},
                 {'analysis':'ATLAS-SUSY-2013-05', 'homeGrown':['T2bb'],
                                                   'official' :['']}
              ]   


'''
for dic in HomeGrown_EM:
    print 'The analysis is ', dic['analysis'], ' the list of homegrown maps is ', dic['homeGrown'], ' while the official maps are ', dic['official']
'''
                
