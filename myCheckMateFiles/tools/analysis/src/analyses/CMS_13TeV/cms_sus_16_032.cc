#include "cms_sus_16_032.h"
#include <algorithm>
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
void Cms_sus_16_032::initialize() {
  setAnalysisName("cms_sus_16_032");
  setInformation(""
    "# cms\n"
    "# cms-sus-16-032\n"
    "# b-jets and c-jets plus MET\n"
  "");
  setLuminosity(35.9*units::INVFB);
  bookSignalRegions("HT_200_MCT_150;HT_200_MCT_250;HT_200_MCT_350;HT_200_MCT_450;HT_500_MCT_150;HT_500_MCT_250;HT_500_MCT_350;HT_500_MCT_450;HT_500_MCT_600;HT_1000_MCT_150;HT_1000_MCT_250;HT_1000_MCT_350;HT_1000_MCT_450;HT_1000_MCT_600;HT_1000_MCT_800;1b_ETmiss_250;1b_ETmiss_300;1b_ETmiss_500;1b_ETmiss_750;1b_ETmiss_1000;2b_ETmiss_250;2b_ETmiss_250_HT_100;2b_ETmiss_300;2b_ETmiss_300_HT_100;2b_ETmiss_500;2b_ETmiss_500_HT_100;1c_ETmiss_250;1c_ETmiss_300;1c_ETmiss_500;1c_ETmiss_750;1c_ETmiss_1000;2c_ETmiss_250;2c_ETmiss_250_HT_100;2c_ETmiss_300;2c_ETmiss_300_HT_100;2c_ETmiss_500;2c_ETmiss_500_HT_100;2c_ETmiss_750;2c_ETmiss_750_HT_100;0b_ETmiss_300;0b_ETmiss_500;0b_ETmiss_750;0b_ETmiss_1000;0b_ETmiss_1250;NSV_ETmiss_250;NSV_ETmiss_300;NSV_ETmiss_500;NSV_ETmiss_750;NSV_ETmiss_1000");
  // You can also book cutflow regions with bookCutflowRegions("CR1;CR2;..."). Note that the regions are
  //  always ordered alphabetically in the cutflow output files.

  // You should initialize any declared variables here
}

void Cms_sus_16_032::analyze() {
  // Your eventwise analysis code goes here
  // The following objects are always defined unless they are 'ignored' above. They form std::vector objects of the respective Delphes class type (except for Etmiss which is a single object)
  // All std::vector members and etmiss have the common properties PT, Eta, Phi and P4() with the latter giving access to the full ROOT TLorentzVector.
  // Within a std::vector, all members are ordered with highest pt coming first.

  // electronsLoose, electronsMedium, electronsTight   are list of electrons that passed respective efficiency and reconstruction cuts
  // muonsCombinedPlus, muonsCombined                  as above for muons
  // photonsMedium                                     as above for photons
  // jets are all reconstructed jets                   as above for jets. Note that electrons are most certainly also reconstructed as a jet -> overlap removal do avoid double counting necessary!
  // tracks, towers                                    calorimeter and tracker information. Usually not needed.
  // missingET                                         rec missing ET EXCLUDING muons.


  // Here is a couple of useful functions and lines:
  //------------Phase Space Cuts (defined for jets, electronsXYZ, muonsXYZ, photonsXYZ)
  // jets = filterPhaseSpace(jets, 20., -2.8, 2.8)  // The vector 'jets' only contains jets with pt >= 20 GeV and -2.8 < eta < 2.8. This function is applicable to other particles too (electronsMedium, ... ).
  // jets = overlapRemoval(jets, electronsLoose, 0.2) Removes all jets for which there exists any electron in 'electronsLoose' with deltaR < 0.2.
  // jets = overlapRemovel(jets, 0.2) If two jets overlap within deltaR < 0.2, only the harder jet is stored.

  //------------Isolation Checks (defined for electronsXYZ, muonsXYZ, photonsXYZ
  //------------        For each object, if the user entered N isolation conditions, they can be
  //------------        checked individually be the second argument (running from 0 to N-1).
  // electronsMedium = filterIsolation(electronsMedium, 0)            Removes electrons that do not pass the first isolation condition entered into the AnalysisManager by the user
  // std::vector<int> flags; flags.push_back(0); flags.push_back(2);
  // electronsMedium = filterIsolation(electronsMedium, flags)        Same as above, but both the first and the third condition have to be fulfilled
  // electronsMedium = filterIsolation(electronsMedium)               Same as above, but all conditions have to be fulfilled.

  //-----------Flavour Tag Checks (defined for jets only)
  //----------          Tau tags "loose", "medium" or "tight" can be individually checked if the user enabled tau tagging in the AM.
  //----------          For b-tags, if N working points have been defined, the ith condition can be tested by putting i-1 into the second argument (if there is only one, the argument can be omitted)
  // if checkTauTag(jets[0], "tight") leadingJetIsTagged = True;
  // if checkBTag(jets[0], 0) leadingJetIsBTagged = True;


  //-----------Auxiliary Information
  // - Always ensure that you don't access vectors out of bounds. E.g. 'if(jets[1]->PT > 150)' should rather be if (jets.size() > 1 && jets[1]->PT > 150).
  // - Use rand()/(RAND_MAX+1.) for random numbers between 0 and 1. The random seed is determined from system time or by the RandomSeed parameter in CheckMATE.
  // - The 'return' statement will end this function for the current event and hence should be called whenever the current event is to be vetoed.
  // - Many advanced kinematical functions like mT2 are implemented. Check the manual for more information.
  // - If you need output to be stored in other files than the cutflow/signal files we provide, check the manual for how to do this conveniently.

  //Basic object definitions:
  //Jets:
  jets = filterPhaseSpace(jets, 25., -2.4, 2.4);
  std::vector<Jet*> bjets;
  std::vector<Jet*> cjets;
  std::vector<Jet*> lightjets;
  for (int i = 0; i < jets.size(); ++i){
      if (jets[i]->PT < 500. &&  checkBTag(jets[i], 1)){
          bjets.push_back(jets[i]);
      }
      else if (jets[i]->PT > 500. &&  checkBTag(jets[i], 0)){
          bjets.push_back(jets[i]);
      }
      else if (checkCTag(jets[i],0)){
          cjets.push_back(jets[i]);
      }
      else lightjets.push_back(jets[i]);
  }

  //SV (secondary vertex):
  int NSV = 0;
  double prob;
  double SVeff = 0.2;
  for (int i = 0; true_b.size(); ++i){
      if (true_b[i]->PT > 25) continue;
      prob = rand()/(RAND_MAX+1.);
      if (prob < SVeff) ++NSV;
  }

  //ISR system:
  vector<Jet*> ISR;
  if (bjets.size() and bjets[0] == jets[1])
        ISR.push_back(jets[0]);
  else if (cjets.size() and cjets[0] == jets[1])
        ISR.push_back(jets[0]);
  else if (!bjets.size() and !cjets.size()){
      ISR.push_back(jets[0]);
      if (jets[2]->PT > 50.)
        ISR.push_back(jets[1]);
  }

  //Muons and Electrons:
  vector<Electron*> electrons;
  vector<Muon*> muons;
  electrons = filterIsolation(electronsLoose, 0);
  electrons = filterPhaseSpace(electrons, 10., -2.4, 2.4);
  muons = filterIsolation(muonsLoose, 0);
  muons = filterPhaseSpace(muons, 10., -2.4, 2.4);
  //Taus:
  int ntaus = 0;
  for (int i = 0; i < tracks.size(); ++i){
      if (tracks[i]->PT < 10.0 || fabs(tracks[i]->Eta) > 2.5)
        continue;
      double Iso = 0.;
      for (int j = 0; j < tracks.size(); ++j){
          if (i == j) continue;
          if (tracks[i]->P4().DeltaR(tracks[j]->P4()) < 0.3)
            continue;
          Iso += tracks[j]->PT;
      }
      if (Iso < 0.1*tracks[i]->PT) ++ntaus;
  }

  missingET->addMuons(muonsCombined);  // Adds muons to missing ET.


  //Kinematical variables
  double HT = 0., HTb = 0., HTc = 0.;
  for (int i = 0; i < min(2,int(jets.size())); ++i){
      HT += jets[i]->PT;
  }
  for (int i = 0; i < min(2,int(bjets.size())); ++i){
      HTb += bjets[i]->PT;
  }
  for (int i = 0; i < min(2,int(cjets.size())); ++i){
      HTc += cjets[i]->PT;
  }
  double deltaPhiMin = 0.;
  double deltaPhi, mT;
  for (int i = 0; i < min(3,int(jets.size())); ++i){
      deltaPhi = fabs(jets[i]->P4().DeltaPhi(missingET->P4()));
      if (i == 0) deltaPhiMin = deltaPhi;
      else deltaPhiMin = min(deltaPhiMin,deltaPhi);
  }
  double mTmin = 0.;
  for (int i = 0; i < min(2,int(jets.size())); ++i){
      deltaPhi = fabs(jets[i]->P4().DeltaPhi(missingET->P4()));
      mT = sqrt(2.*jets[i]->PT*missingET->P4().Et()*(1.-cos(deltaPhi)));
      if (i == 0) mTmin = mT;
      else mTmin = min(mTmin,mT);
  }
  double mCT = 0;
  if (jets.size() >= 2){
      deltaPhi = fabs(jets[0]->P4().DeltaPhi(jets[1]->P4()));
      mCT = sqrt(2.*jets[0]->PT*jets[1]->PT*(1.+cos(deltaPhi)));
  }
  double MET = missingET->P4().Et();

  //Signal Regions
  //Event Pre-Selection:
  //Non-compressed region:
  bool NCselection = true;
  //Compressed region
  bool Cselection = true;
  if (jets.size() < 2) {
      NCselection = false;
      Cselection = false;
  }
  if (jets[1]->PT < 30.0) {
      NCselection = false;
  }
  if (jets.size() >= 5 && jets[4]->PT > 75.0) {
      NCselection = false;
      Cselection = false;
  }
  if (muons.size() > 0 || electrons.size() > 0 || ntaus > 0){
      NCselection = false;
      Cselection = false;
  }
  if (MET < 250.) {
      NCselection = false;
      Cselection = false;
  }
  if (deltaPhiMin < 0.4) {
      NCselection = false;
      Cselection = false;
  }
  //Noncompressed region specific selection:
  if (NCselection){
      if (jets[0]->PT < 100.) NCselection = false;
      if (jets[1]->PT < 75.) NCselection = false;
      if (bjets.size() < 2) NCselection = false;
      else if (bjets[0]->PT != jets[0]->PT)
          NCselection = false;
      else if (bjets[1]->PT != jets[1]->PT)
          NCselection = false;
      if (mTmin < 250.0) NCselection = false;
      if (mCT < 150.0) NCselection = false;
  }

  //Compressed region specific selection:
  if (Cselection){
      if (jets[0]->PT < 100.) Cselection = false;
      if (jets[1]->PT < 25.) Cselection = false;
      if (bjets.size() > 0 && bjets[0]->PT == jets[0]->PT)
          Cselection = false;
      if (cjets.size() > 0 && cjets[0]->PT == jets[0]->PT)
          Cselection = false;
      if ((bjets.size() > 0 && jets[1]->PT == bjets[0]->PT)
          || (cjets.size() > 0 && jets[1]->PT == cjets[0]->PT)){
              if (jets[1]->PT < 25.0) Cselection = false;
      }
      else if (jets[1]->PT < 50.0) Cselection = false;
      double pTISR = 0.;
      TLorentzVector p4 = missingET->P4();
      for(int iISR = 0; iISR < ISR.size(); ++ iISR){
          pTISR += ISR[iISR]->PT;
          p4 += ISR[iISR]->P4();
      }
      if (pTISR < 250.0) Cselection = false;
      if (p4.Et()/MET > 0.5)
          Cselection = false;
  }

  //Noncompressed signal regions:
  if (NCselection){
      vector<double> SR_HT = {200,500,1000};
      vector<double> SR_MCT = {150,250,350,450,600,800};
      for (int iht = 0; iht < SR_HT.size(); ++iht){
          if (HT < SR_HT[iht]) continue;
          if (iht < SR_HT.size()-1 && HT >= SR_HT[iht+1])
              continue;
          for (int imct = 0; imct < iht+4; ++imct){
              if (mCT < SR_MCT[imct]) continue;
              if (imct < iht+3 && mCT < SR_MCT[imct+1]) continue;
              // countSignalEvent("HT_xx_MCT_xx");
          }
      }
  }


}

void Cms_sus_16_032::finalize() {
  // Whatever should be done after the run goes here
}

//c-tagging check
bool Cms_sus_16_032::checkCTag(Jet *jet, int ilevel) {
  return false;
}
