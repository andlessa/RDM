#ifndef CMS_SUS_19_005_H_
#define CMS_SUS_19_005_H_
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
#include "AnalysisBase.h"

class Cms_sus_19_005 : public AnalysisBase {
  public:
    Cms_sus_19_005() : AnalysisBase()  {}
    ~Cms_sus_19_005() {}

    void initialize();
    void analyze();
    void finalize();

  private:
    bool tagBJetMedium(Jet *cand,
                        std::vector<GenParticle*> gen_b,
                        std::vector<GenParticle*> gen_c);
    double getEffFromData(vector<vector<double>> effData,
                          double pt);
    std::vector<TLorentzVector> getPseudoJets(std::vector<Jet*> jets);
};

#endif
