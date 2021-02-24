#ifndef CMS_SUS_16_032_H_
#define CMS_SUS_16_032_H_
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
#include "AnalysisBase.h"

class Cms_sus_16_032 : public AnalysisBase {
  public:
    Cms_sus_16_032() : AnalysisBase()  {}
    ~Cms_sus_16_032() {}

    void initialize();
    void analyze();
    void finalize();

  private:
      bool tagBJet(Jet *cand, string efficiency,
                        std::vector<GenParticle*> gen_b,
                        std::vector<GenParticle*> gen_c);
      bool tagCJet(Jet *cand,
                        std::vector<GenParticle*> gen_b,
                        std::vector<GenParticle*> gen_c);
      double getEffFromData(vector<vector<double>> effData,
                        double pt);
      // vector<TH1F*> hists;
};

#endif
