#ifndef ATLAS_SUSY_2018_04_H_
#define ATLAS_SUSY_2018_04_H_
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
#include "AnalysisBase.h"

class Atlas_susy_2018_04 : public AnalysisBase {
  public:
    Atlas_susy_2018_04() : AnalysisBase()  {}
    ~Atlas_susy_2018_04() {}

    void initialize();
    void analyze();
    void finalize();

  private:

    std::vector<bool> getFlatTauTags(Jet* cand,
                                    std::vector<Track*> tracks,
		                            std::vector<GenParticle*> true_tau);
};

#endif
