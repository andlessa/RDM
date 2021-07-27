# RDM: Dark Matter and R<sub>D anomalies

This branch holds the main code for obtaining the constraints for the RDM 2021 paper.
The searches used for obtaining the exclusion curves are:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)


More information about the CheckMATE implementation and validation can be found [here](./myCheckMateFiles3/README.md)
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

### SModelS ###

The topologies from &chi;<sub>1</sub> production and decay are not present in SModelS. However, the  &chi;<sub>1</sub> decay to &chi;<sub>0</sub> + b  + &nu; can be approximated by a T2bb topology (sbottom production and decay to b + MET).
However this requires modifying the SLHA files so the decay entries for  &chi;<sub>1</sub> -> &chi;<sub>0</sub> + b  + &nu; do not include the neutrino.
This can be done running [data/fixForSModelS.py](data/fixForSModelS.py) over the folder of original SLHA files.

In order to obtain the SModelS results for the modified files run (in the [./smodels](./smodels) folder):

```
./runSModelS.py -p ../smodels_parameters.ini -f <input_folder> -o <output_folder>
```


### CheckMATE ###

The results using CheckMATE can be obtained running

```
./runCheckMateScan.py -p <parameter_file>
```
where an example of the parameter_file can be found in [checkmate_parameters.ini](checkmate_parameters.ini).

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
