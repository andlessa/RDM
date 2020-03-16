#ifndef ATLAS_SUSY_2018_04_H_
#define ATLAS_SUSY_2018_04_H_
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
#include "AnalysisHandlerATLAS_13TeV.h"

class Atlas_susy_2018_04 : public AnalysisBase {
  public:
    Atlas_susy_2018_04() : AnalysisBase()  {}
    ~Atlas_susy_2018_04() {}

    void initialize();
    void analyze();
    void finalize();
    vector<bool> getTauFlatTags(<Jet*> jet,
                                double looseEffSingle,
                                double mediumEffSingle,
                                double tightEffSingle,
                                double looseEffMulti,
                                double mediumEffMulti,
                                double tightEffMulti);

  private:
};

#endif
