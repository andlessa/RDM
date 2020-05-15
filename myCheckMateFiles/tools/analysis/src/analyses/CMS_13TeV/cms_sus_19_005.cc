#include "cms_sus_19_005.h"
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
void Cms_sus_19_005::initialize() {
  setAnalysisName("cms_sus_19_005");
  setInformation(""
    "# CMS search, inclusive hadronic search, with mT2.\n"
    "# Signal regions with disappearing tracks have not been implemented.\n"
  "");
  setLuminosity(137.0*units::INVFB);
  bookSignalRegions("2jloose;2jtight;4jloose;4jtight;7jloose;7jtight;10jloose;10jtight;2bloose;2btight;3bloose;3btight;4bloose;4btight;7j3bloose;7j3btight;7j4bloose;7j4btight;10j4bloose;10j4btight;monoPhi");
  // You can also book cutflow regions with bookCutflowRegions("CR1;CR2;..."). Note that the regions are
  //  always ordered alphabetically in the cutflow output files.

  // You should initialize any declared variables here
}

void Cms_sus_19_005::analyze() {

    //Basic object definitions:
    //Jets:
    jets = filterPhaseSpace(jets, 20., -2.4, 2.4);
    std::vector<Jet*> bjets;
    std::vector<Jet*> cjets;
    std::vector<Jet*> lightjets;
    std::vector<bool> bTagsMedium;
    std::vector<bool> cTagsMedium;
    for (int i = 0; i < jets.size(); ++i){
        if (tagBJet(jets[i],"medium"))
          bTagsMedium.push_back(true);
        else  bTagsMedium.push_back(false);
        if (tagCJet(jets[i]) && !(bTagsMedium[i]))
           cTagsMedium.push_back(true);
        else cTagsMedium.push_back(false);

        if (bTagsMedium[i]){
           bjets.push_back(jets[i]);
        }
        else if (cTagsMedium[i])){
           cjets.push_back(jets[i]);
        }
        else if (jets[i]->PT > 30.0){
           lightjets.push_back(jets[i]);
        }
  }

  //Leptons:
  //Muons and Electrons:
  vector<Electron*> electrons;
  vector<Muon*> muons;
  electrons = filterIsolation(electronsLoose, 0);
  electrons = filterPhaseSpace(electrons, 10., -2.4, 2.4);
  muons = filterIsolation(muonsLoose, 0);
  muons = filterPhaseSpace(muons, 10., -2.4, 2.4);

  //Isolated tracks:
  nIsolated = 0;
  for(int t = 0; t < tracks.size(); t++) {
      if (tracks[t]->PT < 10.) continue;
      if (fabs(tracks[t]->Eta) > 2.5) continue;
      double Isol = 0;
      for(int tj = 0; tj < tracks.size(); tj++) {
          if (tj == t) continue;
          //Compute amount of track activity around track
          if (tracks[tj]->P4().DeltaR(tracks[t]->P4()) < 0.3){
              Isol += tracks[tj]->PT;
          }
      }
      if (Isol < 0.1*tracks[t]->PT){
          ++nIsolated;
      }
  }

  //Kinematical variables:
  missingET->addMuons(muonsCombined);  // Adds muons to missing ET.
  std::vector<double> HTmissV = {0.0,0.0};
  std::vector<Jet*> alljets;
  alljets.insert(alljets.end(), lightjets.begin(), lightjets.end());
  alljets.insert(alljets.end(), cjets.begin(), cjets.end());
  alljets.insert(alljets.end(), bjets.begin(), bjets.end());
  double HT = 0;0;
  double maxJetPT = 0.0;
  for (int i = 0; alljets.size(); ++i){
      HTmissV[0] -= alljets[i]->P4().X();
      HTmissV[1] -= alljets[i]->P4().Y();
      HT += alljets[i]->PT;
      if (alljets[i]->PT > maxJetPT) maxJetPT = alljets[i]->PT;
  }
  double HTmiss = sqrt(pow(HTmissV[0],2)+pow(HTmissV[1],2));
  double pTmiss = missingET->P4().Pt();

  double mT2jet = 0.;
  if (alljets.size() >= 2){
      //Compute 4-momentum of pseudo-jets
      std::vector<TLorentzVector> pseudoJets;
      pseudoJets = getPseudoJets(alljets);
      //Compute MT2 with pseudoJets:
      mT2jet = mT2(pseudoJets[0], pseudoJets[1], 0., missingET->P4());
  }


 //Event selection
 bool passTrigger = false;
 //Trigger (2017-2018)
 if (pTmiss > 120.0 && HTmiss > 120.) passTrigger = true;
 if (HT > 60.0 && pTmiss > 120.0 && HTmiss > 120.) passTrigger = true;
 if (HT > 500.0 && pTmiss > 100.0 && HTmiss > 100.) passTrigger = true;
 if (HT > 800.0 && pTmiss > 75.0 && HTmiss > 75.) passTrigger = true;
 if (HT > 1050.0 || maxJetPT > 500.0) passTrigger = true;

 if (!passTrigger) return;

 


}

void Cms_sus_19_005::finalize() {
  // Whatever should be done after the run goes here
}

//B-tagging based on CSVv2 algorithm
//(from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency)
bool Cms_sus_19_005::tagBJetMedium(Jet *cand) {

    const double DR_B_TRUTH = 0.2;
    const double PTMIN_B_TRUTH = 10.0;
    const double ETAMAX_B_TRUTH = 2.4;

    vector<vector<double>> bTagEffMedium = {{30.0,35.0,0.5735},
        {35.0,40.0,0.5872},{40.0,50.0,0.5999},{50.0,60.0,0.6159},
        {60.0,70.0,0.6277},{70.0,80.0,0.6352},{80.0,90.0,0.6402},
        {90.0,100.0,0.6415},{100.0,125.0,0.6429},{125.0,150.0,0.6457},
        {150.0,175.0,0.6353},{175.0,200.0,0.6165},{200.0,225.0,0.6051},
        {225.0,250.0,0.5938},{250.0,275.0,0.5871},{275.0,300.0,0.5771},
        {300.0,350.0,0.5663},{350.0,400.0,0.5425},{400.0,450.0,0.5296},
        {450.0,500.0,0.5085},{500.0,600.0,0.4840},{600.0,700.0,0.4820},
        {700.0,800.0,0.4663},{800.0,1000.0,0.4663}};

    double prob = rand()/(RAND_MAX+1.);
    double eff = 0.0;
    /* Loop over bs and try to find an overlap.
    * If there is one, use b signal efficiency*/
    for(int b = 0; b < true_b.size(); b++) {
      if(true_b[b]->PT > PTMIN_B_TRUTH &&
        fabs(true_b[b]->Eta) < ETAMAX_B_TRUTH &&
         true_b[b]->P4().DeltaR(cand->P4()) < DR_B_TRUTH) {
            eff = getEffFromData(bTagEffMedium,cand->PT);
            break;
      }
    }
    // If no b overlap, test with truth c's and maybe use c-efficiency
    if (eff == 0.0) {
      for(int c = 0; c < true_c.size(); c++) {
          if(true_c[c]->PT > PTMIN_B_TRUTH &&
             fabs(true_c[c]->Eta) < ETAMAX_B_TRUTH &&
             true_c[c]->P4().DeltaR(cand->P4()) < DR_B_TRUTH) {
                eff = 0.15; //medium mistagging
                break;
            }
      }
    }
    // If no b and no c overlap, use light jet Rej
    if (eff == 0.0) eff = 0.02; // medium light jet mistagging

    if (prob < eff)  return true;
    else return false;
}

//B-tagging based on CSVv2 algorithm
//(from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency)
bool Cms_sus_19_005::tagCJet(Jet *cand) {

    const double DR_C_TRUTH = 0.2;
    const double PTMIN_C_TRUTH = 10.0;
    const double ETAMAX_C_TRUTH = 2.4;

    double prob = rand()/(RAND_MAX+1.);
    double eff = 0.0;
    /* Loop over cs and try to find an overlap.
    * If there is one, use c signal efficiency*/
    for(int c = 0; c < true_c.size(); c++) {
        if(true_c[c]->PT > PTMIN_C_TRUTH &&
           fabs(true_c[c]->Eta) < ETAMAX_C_TRUTH &&
           true_c[c]->P4().DeltaR(cand->P4()) < DR_C_TRUTH) {
               eff = 0.4; //medium mistagging
               break;
          }
    }
    // If no c overlap, test with truth b's and maybe use b-efficiency
    if (eff == 0.0) {
        for(int b = 0; b < true_b.size(); b++) {
          if(true_b[b]->PT > PTMIN_C_TRUTH &&
            fabs(true_b[b]->Eta) < ETAMAX_C_TRUTH &&
            true_b[b]->P4().DeltaR(cand->P4()) < DR_C_TRUTH) {
                eff = 0.2; //b-jet mistagging
                break;
          }
       }
    }
    // If no b and no c overlap, use light jet Rej
    if (eff == 0.0){
        eff = 0.2; // medium light jet mistagging
    }
    if (prob < eff)  return true;
    else return false;

}

//Get efficiency for a given pT for a binned data set.
double Cms_sus_19_005::getEffFromData(vector<vector<double>> effData,
                                                double pt){

    int npts = effData.size();

    for (int i = 0; i < npts; ++i){
        if (pt > effData[i][0] && pt <= effData[i][1])
            return effData[i][2];
     }
     return 0.0;
}

//Group jets into two pseudo jets using the Lund distance measure
std::vector<TLorentzVector> Cms_sus_19_005::getPseudoJets(std::vector<Jet*> jets){

    //Get initial seed jets
    std::vector<std::vector<int>> clusters = {{0},{1}};
    double mjj, mjjmax;
    for (int i = 0; i < alljets.size(); ++i){
        for (int j = 0; j < alljets.size(); ++j){
            if (i == j) continue;
            mjj = (alljets[i]->P4()+alljets[j]->P4()).M();
            if (mjj > mjjmax){
                mjjmax = mjj;
                clusters[0] = i;
                clusters[1] = i;
            }
        }
    }

    nint = 0;
    std::vector<std::vector<int>> newclusters = {{},{{}}};
    while (newclusters != clusters && nint < 20){
        //Update clusters:
        if (nint != 0) clusters = newclusters;
        //Cluster all jets into each seed jet according to Lund distance
        double d0i = 0;
        double d1i = 0;
        TLorentzVector p1(0.,0.,0.,0.);
        TLorentzVector p2(0.,0.,0.,0.);
        //Compute total momentum for each cluster:
        for (int i = 0; i < clusters[0].size(); ++i){
            p1 += jets[i]->P4();
        }
        for (int i = 0; i < clusters[1].size(); ++i){
            p2 += jets[i]->P4();
        }
        p1Abs = p1.P();
        p2Abs = p2.P();
        for (int i = 0; i < alljets.size(); ++i){
            p = alljets[i]->P4();
            pAbs = pi.P();
            p1p = p1.X()*p.X()+p1.Y()*p.Y()+p1.Z()*p.Z();
            p2p = p2.X()*p.X()+p2.Y()*p.Y()+p2.Z()*p.Z();
            d1 = 2*(p1Abs*pAbs - p1p)*p1Abs*pAbs/pow(p1Abs+pAbs,2); // Lund distance
            d2 = 2*(p2Abs*pAbs - p2p)*p2Abs*pAbs/pow(p2Abs+pAbs,2);
            if (d1 < d2) newclusters[0].push_back(i);
            else newclusters[1].push_back(i);
        }
        ++nint;
    }

    if (nint == 20) cout << "Error clustering pseudo-jets";

    //Compute total momentum for each cluster:
    TLorentzVector p1(0.,0.,0.,0.);
    TLorentzVector p2(0.,0.,0.,0.);
    for (int i = 0; i < clusters[0].size(); ++i){
        p1 += jets[i]->P4();
    }
    for (int i = 0; i < clusters[1].size(); ++i){
        p2 += jets[i]->P4();
    }
    std::std::vector<TLorentzVector> pJets = {p1,p2};

    return pJets;

}
