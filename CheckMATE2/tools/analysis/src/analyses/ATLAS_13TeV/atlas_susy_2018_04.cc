#include "atlas_susy_2018_04.h"
// AUTHOR: Andre Lessa
//  EMAIL: andre.lessa@ufabc.edu.br
void Atlas_susy_2018_04::initialize() {
  setAnalysisName("atlas_susy_2018_04");          
  setInformation(""
    "# ATLAS\n"
    "# ATLAS-SUSY-2018-04\n"
    "# 2 hadronic taus, etmiss, no b-jets\n"
    "# sqrt(s) = 13 TeV\n"
    "# int(L) = 139 fb^-1\n"
  "");
  setLuminosity(139.0*units::INVFB);      
  bookSignalRegions("SR-lowMass;SR-highMass");
  // You can also book cutflow regions with bookCutflowRegions("CR1;CR2;..."). Note that the regions are
  //  always ordered alphabetically in the cutflow output files.

  // You should initialize any declared variables here
}

void Atlas_susy_2018_04::analyze() {
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


	  jets = filterPhaseSpace(jets, 20., -2.8, 2.8);
	  electronsLoose = filterPhaseSpace(electronsLoose, 17., -2.47, 2.47);
	  electronsLoose = filterIsolation(electronsLoose);
	  muonsCombinedPlus = filterPhaseSpace(muonsCombinedPlus, 14., -2.7, 2.7);
	  muonsCombinedPlus = filterIsolation(muonsCombinedPlus);

	  int nTightTaus = 0;
	  int nMediumTaus = 0;
	  std::vector<Jet*> taujets;
	  std::vector<Jet*> bjets;
	  std::vector<Jet*> lightjets;
	  for (int i = 0; i < jets.size(); i++){
		if (!(checkTauTag(jets[i], "medium") || checkTauTag(jets[i], "tight") || checkBTag(jets[i], 0))){
			lightjets.push_back(jets[i]);
		}
		else if (fabs(jets[i]->Eta) < 2.5 && jets[i]->PT > 20.){
			if(checkTauTag(jets[i], "tight") || checkTauTag(jets[i], "medium")){
				taujets.push_back(jets[i]);
				if (checkTauTag(jets[i], "tight")) ++nTightTaus;
				if (checkTauTag(jets[i], "medium")) ++nMediumTaus;
			}
			else if(checkBTag(jets[i], 0) ) bjets.push_back(jets[i]);
	    }
	  }

	  electronsLoose  = overlapRemoval(electronsLoose, electronsLoose, 0.05);
	  taujets   = overlapRemoval(taujets, electronsLoose, 0.2);
	  taujets   = overlapRemoval(taujets, muonsCombinedPlus, 0.2);
	  electronsLoose  = overlapRemoval(electronsLoose, muonsCombinedPlus, 0.01);
	  lightjets		  = overlapRemoval(lightjets, electronsLoose, 0.2);
	  electronsLoose  = overlapRemoval(electronsLoose, lightjets, 0.4);
	  lightjets       = overlapRemoval(lightjets, muonsCombinedPlus, 0.2);
	  muonsCombinedPlus  = overlapRemoval(muonsCombinedPlus, jets, 0.4);
	  lightjets       = overlapRemoval(lightjets, taujets, 0.2);

	  missingET->addMuons(muonsCombinedPlus);  // Adds muons to missing ET. This should almost always be done which is why this line is not commented out.
  
	  //Event selection:
	  countCutflowEvent("0_Total");
	  if (nMediumTaus != 2 || (taujets[0]->Charge)*(taujets[1]->Charge) > 0) return;
	  countCutflowEvent("1_two_medium_taus_(OS)");
	  if (!bjets.empty()) return;
	  countCutflowEvent("2_b-jet_veto");
	  if (!electronsLoose.empty() || !muonsCombinedPlus.empty()) return;
	  countCutflowEvent("3_light_lepton_veto");
	  double mtautau = (taujets[0]->P4() + taujets[1]->P4()).M();
	  if (mtautau < 120.) return;
	  countCutflowEvent("4_Z/H-veto");

	  double met = missingET->P4().Et();
	  double deltaPhi = fabs(taujets[0]->P4().DeltaPhi(taujets[1]->P4()));
	  double deltaR = taujets[0]->P4().DeltaR(taujets[1]->P4());
	  double mT2tautau = mT2(taujets[0]->P4(), taujets[1]->P4(), 0., missingET->P4());

	  //Overall trigger eff:
	  double triggerEff = 0.8;
	  double random_trigger = (double) rand()/ (double) (RAND_MAX + 1.);
	  bool passTrigger = (random_trigger < triggerEff);


	  //SR-lowMass
	  //di-tau trigger:
	  if (taujets[0]->PT > 95.0 && taujets[0]->PT > 75.0 && passTrigger){
		  countCutflowEvent("lm_1_SRlowMassTrigger");
		  if ((75. < met) && (met < 150.)){
			  countCutflowEvent("lm_2_SRlowMassMET");
			  if (nTightTaus == 2){
				  countCutflowEvent("lm_3_SRlowMass2taus");
				  if (deltaPhi > 0.8){
					  countCutflowEvent("lm_4_SRlowMassDeltaphi");
					  if (deltaR < 3.2){
						  countCutflowEvent("lm_5_SRlowMassDeltaR");
						  if (mT2tautau > 70.){
							  countCutflowEvent("lm_6_SRlowMass");
							  countSignalEvent("SR-lowMass");
						  }
					  }
				  }
			  }
		  }
	  }

	  //SR-highMass
	  //di-tau+MET trigger:
	  if (taujets[0]->PT > 75.0 && taujets[0]->PT > 40.0 && met > 150. && passTrigger){
		  countCutflowEvent("hm_1_SRhighMassTrigger");
		  if (nTightTaus >= 1){
			  countCutflowEvent("hm_2_SRhighMass1tau");
			  if (deltaPhi > 0.8){
				  countCutflowEvent("hm_3_SRhighMassDeltaphi");
				  if (deltaR < 3.2){
					  countCutflowEvent("hm_4_SRhighMassDeltaR");
					  if (mT2tautau > 70.){
						  countCutflowEvent("hm_5_SRhighMass");
						  countSignalEvent("SR-highMass");
					  }
				  }
			  }
		  }
	  }

	  return;
}

void Atlas_susy_2018_04::finalize() {
  // Whatever should be done after the run goes here
}       
