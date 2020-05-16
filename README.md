# RDM: Dark Matter and R<sub>D anomalies

This branch holds the main code for obtaining the constraints for the RDM Les Houches 2019 project.
The searches used are:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/) (added to CheckMATE2)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-036](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-036/index.html) and [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html) (SModels and CheckMATE)

More information about the CheckMATE implementation and validation can be found [here](./myCheckMateFiles/README.md)

## Basic Installation ##

The following codes must be installed:

  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8](http://lcgapp.cern.ch/project/simu/HepMC/)
  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [ufo2slha](https://github.com/andlessa/ufo2slha)
  * [smodels](https://smodels.github.io/)
  * [CheckMATE2](https://checkmate.hepforge.org/)

The script installer.sh will try to fetch the appropriate tarballs and install them.


### Creating SLHA files ###

To create SLHA files from a UFO model run:

```
./ufo2slha/createSLHA.py -p <parameter_file>
```

For a parameter file example see [ufo2slha_LQ.ini](./ufo2slha_LQ.ini).
The parameter file sets the parameters to be used and looped over.

## Running ##

### Sbottom Analysis ###

The results for the b-jet analysis can be obtained running smodels over the set of modified files
[data/smodels_slha_BM2.tar.gz](data/smodels_slha_BM2.tar.gz), where the chi1->b+nu+chi0 decay is artificially modified to chi1->b+chi0, so the T2bb resutls can be used.
The output is stored in [data/smodels_output_BM2.tar.gz](data/smodels_output_BM2.tar.gz)

### Stau Analysis ###

The results for the tau + MET analysis can be obtained running CheckMATE2. The code

```
./runCheckMateScan.py -p <parameter_file>
```

runs CheckMATE using a set of SLHA files as parameter cards for MadGraph and Pythia.
For a parameter file example see [checkmate_parameters.ini](./checkmate_parameters.ini).
The output is stored in [data/checkmate_BM1.tar.gz](data/checkmate_BM1.tar.gz).


## Plotting ##

Plotting examples are available in the [results](results) folder.
An example of the exclusion curve obtaining from recasting the tau analysis is shown below:

![Alt text](results/TStauStau_exclusion_BM1.png?raw=true "ATLAS-SUSY-2018-04 exclusion")





