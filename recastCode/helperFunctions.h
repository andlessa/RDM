//Some helper functions for computing relevant quantities
#include "dataReader.h"
#include "fastjet/PseudoJet.hh"
#include "fastjet/ClusterSequence.hh"


using namespace Pythia8;


std::vector<Particle*> overlapRemoval(std::vector<Particle*> ObjA, std::vector<Particle*> ObjB, float deltaR){

	std::vector<Particle*> newParticles;
	for (int i = 0; i < ObjA.size(); ++i){
		Particle pA = ObjA[i];
		for (int j = 0; j < ObjB.size(); ++j){
			Particle pB = ObjB[i];
			float dR = sqrt(pow(pA.y()-pB.y(),2)+pow(pA.phi()-pB.phi(),2));
			if (dR > deltaR){newParticles.push_back(pA);}
		}
	}
	return newParticles;
}


std::vector<Particle*> getElectrons(Event &event, float minPT, float maxEta){

	std::vector<Particle*> Electrons;
    for (int i = 0; i < event.size(); ++i) {
      // Final state only
      if (!event[i].isFinal()) continue; //Ignore intermediate states
      if (event[i].idAbs() != 11) continue;
      if (event[i].pT() < minPT) continue;
      if (fabs(event[i].eta()) > maxEta) continue;

      Electrons.push_back(event[i]);
    }

	return Electrons;
}

std::vector<Particle*> getMuons(Event &event, float minPT, float maxEta){

	std::vector<Particle*> Muons;
    for (int i = 0; i < event.size(); ++i) {
      // Final state only
      if (!event[i].isFinal()) continue; //Ignore intermediate states
      if (event[i].idAbs() != 13) continue;
      if (event[i].pT() < minPT) continue;
      if (fabs(event[i].eta()) > maxEta) continue;

      Muons.push_back(event[i]);
    }

	return Muons;
}

std::vector<Particle*> getTaus(Event &event, float minPT, float maxEta){

	std::vector<Particle*> Taus;
    for (int i = 0; i < event.size(); ++i) {
      if (event[i].idAbs() != 15) continue;
      if (event[i].pT() < minPT) continue;
      if (fabs(event[i].eta()) > maxEta) continue;

      //Make sure the tau is not an intermediate tau:
      bool intermediateTau = false;
      std::vector<int> daughters = event[i].daughterListRecursive();
      for (int j = 0; j < daughters.size(); ++j){
  		int idaughter = daughters[i];
  		if (event[idaughter].idAbs() == 15) intermediateTau = true;
      }

      if (!intermediateTau){Taus.push_back(event[i]);}
    }
	return Taus;
}


std::vector<fastjet::PseudoJet> getJets(Event &event, fastjet::JetDefinition jetDef, float minPT, float maxEta){

	//Get jets:
	vector <fastjet::PseudoJet> inclusiveJets, jets, finalJets;
	std::vector <fastjet::PseudoJet> fjInputs; //particles for applying jet clustering
	// Loop over particles in the event: kinematic distribution
	for (int i = 0; i < event.size(); ++i) {
		// Require visible particles inside detector.
		if (!event[i].isFinal()){continue;}
		fastjet::PseudoJet particleTemp(event[i].px(),event[i].py(),event[i].pz(),event[i].e());
		particleTemp.set_user_index(i);
		fjInputs.push_back(particleTemp);
	}
	fastjet::ClusterSequence clustSeq(fjInputs, jetDef);
	inclusiveJets = clustSeq.inclusive_jets(pTjet);
	jets    = sorted_by_pt(inclusiveJets);

	for(int i = 0; i < jets.size(); ++i){
		if (jets[i].pt() < minPT){continue;}
		if (fabs(jets[i].eta()) > maxEta){continue;}
		finalJets.push_back(jets[i]);

	}
	return finalJets;
}


std::vector<fastjet::PseudoJet> getBJets(Event &event, vector <fastjet::PseudoJet> jets, float minPT, float maxEta){

	vector <fastjet::PseudoJet> BJets;
	Particle jetParticle;
	//Get jets:
	for(int i = 0; i < jets.size(); ++i){
		bool hasBquark = false;
		if (jets[i].pt() < minPT){continue;}
		if (fabs(jets[i].eta()) > maxEta){continue;}
		vector<fastjet::PseudoJet> constituents = jets[i].constituents();
		for (int j = 0; j < constituents.size(); j++) {
			jetParticle = event[constituents[j].user_index()];
			if (jetParticle.idAbs() == 5){ hasBquark = true;}
		}

		if (hasBquark){BJets.push_back(jets[i]);}
	}
	return BJets;
}



Vec4 getMET(Event &event)
//Returns the missing 4-vector for the event (sums up neutralinos and neutrinos)
{
    Vec4 missingETvec;
    std::vector<int> metaStableMothers;
    //First check for all final particles:
    for (int i = 0; i < event.size(); ++i) {
    	Particle ptc = event[i];
    	if (!ptc.isFinal()) continue;
    	//Neutrinos are included in MET:
    	if (ptc.idAbs() == 12 || ptc.idAbs() == 14 || ptc.idAbs() == 16){
    		//cout << "Including: " << i << " " << ptc.name() << endl;
    		missingETvec += ptc.p();
    		continue;
    	}
    	if (ptc.isHadron()) continue;  //Ignore usual hadrons
    	if (ptc.idAbs() == 22) continue; //Ignore photons
    	if (ptc.isVisible() && ptc.m() < 10.) continue; //Ignore light visible particles

        //Add to missing momentum
    	//cout << "Including: " << i << " " << ptc.name() << endl;
        missingETvec += ptc.p();
    }


    return missingETvec;
}

