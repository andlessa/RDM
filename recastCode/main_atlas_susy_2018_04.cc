// Reads an input LHE or an input SLHA file and generate events using Pythia 8.
// It the given signal efficiency for the ATLAS-SUSY-2018-04 stau search.

#include <iostream>
#include "Pythia8/Pythia.h"
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <string>
#include <random>
#include "helperFunctions.h"



using namespace Pythia8;



int run(const string & infile, int nevents, const string & cfgfile, const string & outputfile)
{


  std::srand(500);
  string outname;
  if (outputfile == ""){
	  size_t lastindex = infile.find_last_of(".");
	  outname = infile.substr(0, lastindex)+".py";
  }
  else{outname = outputfile;}

  // Generator. Shorthand for the event.
  Pythia pythia("",false); //Set printBanner to false
  Event& event = pythia.event;
  pythia.readFile( cfgfile );
  if ( infile.find(".slha") != std::string::npos ){
    cout << "Using SLHA file as input" << endl;
    pythia.readString("SLHA:file = " + infile);
    if ( nevents < 0) {
    	nevents = 100;
    	cout << "Negative number of events for SLHA input. Setting nevents to " << nevents << endl;
    }
  }
  else{
    cout << "Using LHE file as input" << endl;
    pythia.readString("Beams:frameType = 4");
    pythia.readString("Beams:LHEF = " + infile);
  }

  int nEvts_Total_2FS = 0;
  int nEvts_SRhighMass = 0;
  int nEvts_SRlowMass = 0;

  //Define jet clustering
  fastjet::JetDefinition jetDef(fastjet::antikt_algorithm, Rjet);



  // Initialize.
  pythia.init();

  int nPass = 0;
  int iAbort = 0;
  // Begin event loop.
  int iEvent = 0;
  while (iEvent < nevents or nevents < 0){

    // If failure because reached end of file then exit event loop.
    if (pythia.info.atEndOfFile()) break;

    // Generate events. Quit if failure.
    if (!pythia.next()) {
      if (++iAbort < 10) continue;
      cout << " Event generation aborted prematurely, owing to error!\n";
      break;
    }


    std::vector<Particle*> baselineElectrons  = getElectrons(event,15, 2.47);
    std::vector<Particle*> baselineMuons      = getMuons(event,10, 2.7);
    std::vector<Particle*> baselineTaus       = getTaus(event,20., 2.5);
    std::vector<fastjet::PseudoJet> baselineJets  = getJets(event,jetDef,20., 2.8);
    std::vector<fastjet::PseudoJet> bjets     = getBJets(event,baselineJets, 20., 2.5);
	Vec4  				   metVec             = getMET(event);
	float 				   met                = metVec.pT();

	std::vector<Particle*> mediumtaus         = getMediumTaus(event,20., 2.5);
	std::vector<Particle*> tightaus           = getTightTaus(event,20., 2.5);

	// Extended SUSY overlap removal
	baselineElectrons  = overlapRemoval(baselineElectrons, baselineElectrons, 0.05);
	baselineTaus       = overlapRemoval(baselineTaus, baselineElectrons, 0.2);
	baselineTaus       = overlapRemoval(baselineTaus, baselineMuons, 0.2);
	baselineElectrons  = overlapRemoval(baselineElectrons, baselineMuons, 0.01);
	baselineJets       = overlapRemoval(baselineJets, baselineElectrons, 0.2);
	baselineElectrons  = overlapRemoval(baselineElectrons, baselineJets, 0.4);
	baselineJets       = overlapRemoval(baselineJets, baselineMuons, 0.2);
	baselineMuons      = overlapRemoval(baselineMuons, baselineJets, 0.4);
	baselineJets       = overlapRemoval(baselineJets, baselineTaus, 0.2);

	if (baselineTaus.size() != 2) return;
	if (mediumtaus.size() != 2) return;
	bool isOS = baselineTaus[0].charge()!=baselineTaus[1].charge();
	if (!isOS) return;
	if (baselineTaus[0].pT() < 50 || baselineTaus[1].pT() < 40) return;
	if (baselineElectrons.size() > 0 || baselineMuons.size() > 0) return; //lightlepton veto
	int njets_B20 = bjets.size();
	if (njets_B20 != 0) return;  //bVeto
	float mll = (baselineTaus[0]+baselineTaus[1]).M();
	if (mll < 120) return; //zHVeto

	bool trig1 = (baselineTaus[0].pT() >50 && baselineTaus[1].pT() >40 && met>150);
	bool trig2 = (baselineTaus[0].pT() >95 && baselineTaus[1].pT() >60);
	float mt2  = calcMT2(baselineTaus[0],baselineTaus[1],metVec);
	float dphi = fabs(baselineTaus[0].DeltaPhi(baselineTaus[1]));
	float dR   = baselineTaus[0].DeltaR(baselineTaus[1]);

	if ( trig1 && met>150 && tightaus.size()>=1 && dphi>0.8 && dR<3.2 && mt2>70 ) ++nEvts_SRhighMass;
	if ( trig2 && met<150 && met>75 && tightaus.size()==2 && dphi>0.8 && dR<3.2 && mt2>70 ) ++nEvts_SRlowMass;

  }
  // Done.
  return 0;
}


void help( const char * name )
{
	  cout << "syntax: " << name << " [-h] [-f <input file>] [-o <output file>] [-n <number of events>] [-c <pythia cfg file>]" << endl;
	  cout << "        -f <input file>:  pythia input LHE or SLHA file" << endl;
	  cout << "        -c <pythia config file>:  pythia config file [pythia8_Prompt-lepton.cfg]" << endl;
	  cout << "        -o <output file>:  pythia output file [<input file>.py]" << endl;
	  cout << "        -n <number of events>:  Number of events to be generated [100]. If n < 0, it will run over all events in the LHE file" << endl;
  exit( 0 );
};

int main( int argc, const char * argv[] ) {
  int nevents = -1;
  string cfgfile = "pythia8_Prompt-lepton.cfg";
  string outfile = "";
  string infile = "";
  for ( int i=1; i!=argc ; ++i )
  {
    string s = argv[i];
    if ( s== "-h" )
    {
      help ( argv[0] );
    }

    if ( s== "-c" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      cfgfile = argv[i+1];
      i++;
      continue;
    }


    if ( s== "-n" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      nevents = atoi(argv[i+1]);
      i++;
      continue;
    }

    if ( s== "-o" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      outfile = argv[i+1];
      i++;
      continue;
    }


    if ( s== "-f" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      infile = argv[i+1];
      i++;
      continue;
    }




    cout << "Error. Argument " << argv[i] << " unknown." << endl;
    help ( argv[0] );
  };

  int r = run(infile, nevents, cfgfile, outfile);

  return 0;
}
