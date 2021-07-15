# RDM: Dark Matter and R<sub>D anomalies

This branch holds the main code for obtaining the constraints for the RDM Les Houches 2019 project.
The searches used for obtaining the exclusion curves are:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)


More information about the CheckMATE implementation and validation can be found [here](./myCheckMateFiles/README.md)
and more details about the results can be found in [results](./results).

## Basic Installation ##

The following codes must be installed:

  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8](http://home.thep.lu.se/Pythia/)
  * [HepMC](http://lcgapp.cern.ch/project/simu/HepMC/) (optional)
  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [ufo2slha](https://github.com/andlessa/ufo2slha)
  * [smodels](https://smodels.github.io/) (optional)
  * [CheckMATE3](https://checkmate.hepforge.org/)

The script installer.sh will try to fetch the appropriate tarballs and install them. The required versions of smodels and ufo2slha are already included in this repository.


### Creating SLHA files ###

To create SLHA files from a UFO model run:

```
./ufo2slha/createSLHA.py -p <parameter_file>
```

For a parameter file example see [ufo2slha_LQ.ini](./ufo2slha_LQ.ini).
The parameter file sets the parameters to be used and looped over.

## Running ##

### Sbottom Analysis (SModelS) ###

The results for the BM2 benchmark using SModelS can be obtained running smodels over the set of modified files
[data/smodels_slha_BM2.tar.gz](data/smodels_slha_BM2.tar.gz), where the chi1->b+nu+chi0 decay is artificially modified to chi1->b+chi0, so the T2bb resutls can be used.
The output is stored in [data/smodels_output_BM2.tar.gz](data/smodels_output_BM2.tar.gz)

### Sbottom Analysis (CheckMATE) ###

The results for the BM2 benchmark using CheckMATE can be obtained running CheckMATE over the set of BM2 SLHA files
[data/slha_BM2.tar.gz](data/slha_BM2.tar.gz):

The results for the tau + MET analysis can be obtained running CheckMATE2. The code

```
./runCheckMateScan.py -p <parameter_file>
```

The output is stored in [data/checkmate_BM2.tar.gz](data/checkmate_BM2.tar.gz).
The result for the combination of signal regions for the  [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
analysis can be obtained running:


```
./results/addCombinedLimit.py -f <checkmate output folder>
```

A line will then be added to CheckMATE output (total_results.txt) with the result for the combination of signal regions (label as Combined).

### Stau Analysis ###

The results for the tau + MET analysis can be obtained running CheckMATE2. The code

```
./runCheckMateScan.py -p <parameter_file>
```

runs CheckMATE using a set of SLHA files as parameter cards for MadGraph and Pythia.
For a parameter file example see [checkmate_parameters.ini](./checkmate_parameters.ini).
The output is stored in [data/checkmate_BM1.tar.gz](data/checkmate_BM1.tar.gz).


## Plotting and Results ##

The exclusion curves for the distinct benchmarks as well as plotting examples are available in the [results](results) folder.
