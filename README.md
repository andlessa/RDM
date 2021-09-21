# RDM: A Common Solution to R<sub>D</sub> anomalies and Dark Matter

This branch holds the main code for obtaining the constraints for the RDM 2021 paper.
The searches used for obtaining the LHC exclusion rely on recasting through CheckMATE and SModelS:
 * **CheckMATE**:

   * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/) (1911.06660)

   * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html) (1707.07274)

   * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) (1909.03460)

   * Monojet (139/fb): [ATLAS-EXOT-2018-06](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/) (2102.10874)

   * Multi-jets plus MET (139/fb): [ATLAS-CONF-2019-040](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2019-040)/ATLAS-SUSY-2018-22 (2010.14293)

 * **SModelS**:

   * b-jets plus MET (139/fb): [ATLAS-SUSY-2018-34](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/) (2101.12527)



More information about the CheckMATE implementation and validation can be found [here](./myCheckMate3Files/validation/)
and more details about the results can be found in [results](./results).

## Basic Installation ##

The following codes must be installed:

  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [Pythia8](http://home.thep.lu.se/Pythia/)
  * [HepMC](http://lcgapp.cern.ch/project/simu/HepMC/) (optional)
  * [MadGraph5](https://launchpad.net/mg5amcnlo/)
  * [ufo2slha](https://github.com/andlessa/ufo2slha)
  * [smodels](https://smodels.github.io/)
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

The topologies from &chi;<sub>1</sub> production and decay are not present in SModelS. However, the  &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + b  + &nu; decay can be approximated by a T2bb topology (sbottom production and decay to b + MET). Furthermore,  the  &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + &tau;  + c decay can be approximated by a TStauStau topology (stau production and decay to &tau; + MET).
However this requires modifying the SLHA files so the decay entries for  &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + b  + &nu; do not include the neutrino and the decay  &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + &tau;  + c does not include the c quark.
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

## Data ##

The data used for the computing the LHC exclusion is stored in the [data](./data) folder. It contains:

  * [slha_BS1p.tar.gz](./data/slha_BS1p.tar.gz): SLHA files for the BS1' benchmark
  * [slha_BS2p.tar.gz](./data/slha_BS2p.tar.gz): SLHA files for the BS2' benchmark
  * [slha_BS1p_smodels.tar.gz](./data/slha_BS1p_smodels.tar.gz): modified SLHA files for the BS1' benchmark to be used with SModelS (see [above](#SModelS))
  * [slha_BS2p_smodels.tar.gz](./data/slha_BS2p_smodels.tar.gz): modified SLHA files for the BS2' benchmark to be used with SModelS (see [above](#SModelS))
  * [slha_BS1p_smodels.tar.gz](./data/slha_BS1p_smodels.tar.gz): modified SLHA files for the BS1' benchmark to be used with SModelS (see [above](#SModelS))
  * [checkmate_BS1p.tar.gz](./data/checkmate_BS1p.tar.gz): CheckMATE output for the BS1' benchmark (see [above](#CheckMATE))
  * [checkmate_BS2p.tar.gz](./data/checkmate_BS2p.tar.gz): CheckMATE output for the BS2' benchmark (see [above](#CheckMATE))  
  * [smodels_BS1p.tar.gz](./data/smodels_BS1p.tar.gz): SModelS output for the BS1' benchmark (see [above](#SModelS))
  * [smodels_BS2p.tar.gz](./data/smodels_BS2p.tar.gz): SModelS output for the BS2' benchmark (see [above](#SModelS))


## Plotting and Results ##

The data stored in the [data](./data) folder can be used to obtain the LHC exclusion. The exclusion curves for the distinct benchmarks as well as plotting examples are available in the [results](results) folder.
