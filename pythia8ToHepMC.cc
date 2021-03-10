// main42.cc is a part of the PYTHIA event generator.
// Copyright (C) 2019 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL v2 or later, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// Author: Mikhail Kirsanov, Mikhail.Kirsanov@cern.ch.
// This program illustrates how a file with HepMC events
// can be generated by Pythia8.
// Input and output files are specified on the command line, e.g. like
// ./main42.exe main42.cmnd hepmcout42.dat > out
// The main program contains no analysis; this is intended to happen later.
// It therefore "never" has to be recompiled to handle different tasks.

// WARNING: typically one needs 25 MB/100 events at the LHC.
// Therefore large event samples may be impractical.

#include "Pythia8/Pythia.h"
#include "Pythia8Plugins/HepMC2.h"
#include <iostream>
#include <string>
#include <cstring>
#include "Pythia8Plugins/aMCatNLOHooks.h"


using namespace Pythia8;

int run(const string & infile, int nevents, const string & cfgfile, const string & outputfile, int njets)
{

  //Set output file names
  string outname, histname;
  if (outputfile == ""){
	  size_t lastindex = infile.find_last_of(".");
	  outname = infile.substr(0, lastindex)+".hepmc";
  }
  else{outname = outputfile;}

  // Interface for conversion from Pythia8::Event to HepMC event.
  HepMC::Pythia8ToHepMC ToHepMC;

  // Specify file where HepMC events will be stored.
  HepMC::IO_GenEvent ascii_io(outname, std::ios::out);

  // Generator. Shorthand for the event.
  Pythia pythia("",false); //Set printBanner to false
  pythia.readFile( cfgfile );
  std::vector<std::string> inFiles;
  if ( (njets < 0) && (infile.find(".slha") != std::string::npos) ){
    cout << "Using SLHA file " << infile << " as input" << endl;
    pythia.readString("SLHA:file = " + infile);
    if ( nevents < 0) {
    	nevents = 100;
    	cout << "Negative number of events for SLHA input. Setting nevents to " << nevents << endl;
    }
  }
  else{
    cout << "Using LHE file " << infile << " as input" << endl;
    pythia.readString("Beams:frameType = 4");
    if (njets < 0){
        njets = 1;
        inFiles.push_back(infile);
    }
    else{
        for (int ijet = 0; ijet < njets; ijet++){
           // From njet, choose LHE file
           stringstream in;
           in   << "_" << ijet << ".lhe";
           string LHEfile = infile + in.str();
           inFiles.push_back(LHEfile);
        }
    }
  }

  for (int ijet = 0; ijet < njets; ijet++){

      // Get process and events from LHE file, initialize only the
      // first time
      if(ijet > 0) pythia.readString("Main:LHEFskipInit = on");
      pythia.readString("Beams:frameType = 4");
      pythia.readString("Beams:LHEF = " + inFiles[ijet]);
      pythia.init();

      int iAbort = 0;
      // Begin event loop.
      int iEvent = 0;

      cout << "READING " << inFiles[ijet] << endl;

      while (iEvent < nevents or nevents < 0){

          cout << "   ievt = " << iEvent << endl;

          // Generate event.
          if (!pythia.next()) {

            // If failure because reached end of file then exit event loop.
            if (pythia.info.atEndOfFile()) {
              break;
            }

            // First few failures write off as "acceptable" errors, then quit.
            if (++iAbort < 10) continue;
            cout << " Event generation aborted prematurely, owing to error!\n";
            break;
          }
          cout << "     filling  ievt = " << iEvent << endl;
//        double weight = pythia.info.mergingWeight();
//        if(weight <= 0.){continue;}
        // Construct new empty HepMC event and fill it.
        // Units will be as chosen for HepMC build, but can be changed
        // by arguments, e.g. GenEvt( HepMC::Units::GEV, HepMC::Units::MM)
        HepMC::GenEvent* hepmcevt = new HepMC::GenEvent();
        ToHepMC.fill_next_event( pythia, hepmcevt );
        // Set event weight
//        hepmcevt->weights().push_back(weight*normhepmc);


        // Write the HepMC event to file. Done with it.
        ascii_io << hepmcevt;
        delete hepmcevt;

        ++iEvent;

      // End of event loop. Statistics.
      }
      pythia.stat();
  }
pythia.stat();

  // Done.
  return 0;
}


void help( const char * name )
{
	  cout << "syntax: " << name << " [-h] [-f <input file>] [-o <output file>] [-n <number of events>] [-c <pythia cfg file>]" << endl;
	  cout << "        -f <input file>:  pythia input LHE or SLHA file" << endl;
	  cout << "        -c <pythia config file>:  pythia config file [pythia8_hepmc.cfg]" << endl;
	  cout << "        -o <output file>:  output HepMC filename [<input file>.hepmc]" << endl;
	  cout << "        -n <number of events>:  Number of events to be generated [100]. If n < 0, it will run over all events in the LHE file" << endl;
	  cout << "        -j <number of jet samples>:  Number of LHE samples [-1]. If n < 0, it will assume a single file" << endl;
  exit( 0 );
};

int main( int argc, const char * argv[] ) {
  int nevents = -1;
  string cfgfile = "pythia8_hepmc.cfg";
  string outfile = "";
  string infile = "";
  int njets = -1;
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

    if ( s== "-j" )
    {
      if ( argc < i+2 ) help ( argv[0] );
      njets = atoi(argv[i+1]);
      i++;
      continue;
    }

    cout << "Error. Argument " << argv[i] << " unknown." << endl;
    help ( argv[0] );
  };

  int r = run(infile, nevents, cfgfile, outfile, njets);

  return 0;
}
