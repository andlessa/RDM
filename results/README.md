# RDM Results

This folder contains the results for the RDM model. The recasting tools SModelS and CheckMATE (with new analyses added) have been used to identify the most relevant analyses for the two main benchmark scenarios:

 * BS1': (&lambda;<sub>L</sub>)<sub>33</sub> = 0.875, (&lambda;<sub>R</sub>)<sub>33</sub> = 0.375, m<sub>S<sub>1</sub></sub> = 1.25 TeV
 * BS2': (&lambda;<sub>L</sub>)<sub>33</sub> = 0.3, (&lambda;<sub>R</sub>)<sub>23</sub> = 1.25, m<sub>S<sub>1</sub></sub> = 1.25 TeV

The first benchmark (BS1') has the &chi;<sub>1</sub> decaying to &chi;<sub>0</sub> + b  + &nu; (40-80%), to &chi;<sub>0</sub> + t  + &tau; (0-30%) and to &chi;<sub>0</sub> + c  + &tau; (0-30%), while BS2' has &chi;<sub>1</sub> decaying almost 100% to &chi;<sub>0</sub> + c + &tau;.
In both benchmarks the &chi;<sub>1</sub> and &chi;<sub>0</sub> masses are free parameters.


## LHC MET Searches ##

### Relevant Searches ###

MET searches for final states containing b's, c's, tau's, multijets and monojet searches can be used to test the pair production of &chi;<sub>1</sub>.

The latest searches containing jets, b-jets or taus plus MET in the final state are listed below. The following notation is used:

 * <ins>underlined</ins>: the search is included in the paper
 * **bold**: the search can be re-interpreted using CheckMATE
 * *italic*: the search has be re-interpreted using SModelS
 * otherwise: the search is missing

#### b or c-jets plus MET ####

  * <ins>**b-jets or c-jets plus MET (35.9/fb)**</ins>: [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/) (arXiv:1707.07274)
  * <ins>*b-jet plus MET (139/fb)*</ins>: [ATLAS-SUSY-2018-34](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/) (arXiv:2101.12527)

#### tau plus MET ####  
  * <ins>**Tau plus MET (139/fb)**</ins>: [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/) (arXiv:1911.06660)

#### Monojet ####

  * <ins>**Monojet (139/fb)**</ins>: [ATLAS-EXOT-2018-06](http:/atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/) (arXiv:2102.10874)
  * <ins>Monojet (36.1/fb)</ins>: [ATLAS-EXOT-2016-27](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2016-27/) (arXiv:1711.03301)

#### Multijets plus MET ####

* <ins>**Multijets plus MET (139/fb)**</ins>: [ATLAS-SUSY-2018-22](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-22/) (arXiv:2010.14293) (only the CONF-NOTE version of this search, [CONF-2019-040](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2019-040/) is implemented in CheckMATE)
* *Multijets plus MET (137/fb)*: [CMS-SUS-19-006](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/index.html) (arXiv:1908.04722)
* **Hadronic MT2 (137/fb)**: [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) (arXiv:1909.03460)
* *Hadronic MT2 (35.9/fb)*: [CMS-SUS-16-036](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-036/index.html) (arXiv:1705.04650)



### BS1' Results ###

#### SModelS Exclusion ####

The exclusion obtained by SModelS **relies on the assumption that the efficiencies for  &chi;<sub>1</sub> &chi;<sub>1</sub> production followed by &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + b  + &nu;  are the same as for sbottom production followed by a decay to bottom plus MET**.
The result is shown below (the big oscillations in the exclusion curve between 700 GeV and 800 GeV are due to gaps in the ATLAS upper limit map):

![Alt text](BS1p_SModelS.png?raw=true "BS1p exclusion SModelS")

Most of the results are limited to mass differences above 10-20 GeV, resulting in the sudden cut of the exclusion curves. However [ATLAS-SUSY-2018-34](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/) goes all the way down to 5 GeV, providing the strongest constraints for the compressed region.

We also point out that [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032) only provide results for a mass difference larger than 25 GeV, so the compressed region is not tested by the upper limit map.

#### CheckMATE Exclusion ####

The  [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/), [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) and [ATLAS-EXOT-2018-06](http:/atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/) analyses have been added to CheckMATE in order to test this scenario.

For the [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/) the covariance matrices provided by CMS were also used to combine the signal regions and obtain stronger limits (following the SModelS implementation and [CMS-NOTE-2017-001](https://cds.cern.ch/record/2242860?ln=en)).

The results are shown below:

![Alt text](BS1p_CheckMate.png?raw=true "BS1p exclusion CheckMATE")


The limits are comparable to the ones obtained by SModelS. However the [ATLAS-SUSY-2018-34](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/) analysis is not available in CheckMATE. In addition, the [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/) available in SModelS only extends down to 25 GeV mass difference. The extremely compressed region, however, can be tested by this analysis due to the signal regions which test very soft b's.

We also point out that the strong limits obtained by [ATLAS-CONF-2019-040](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2019-040/) in the compressed region might not be reliable (see the compressed region in this [validation plot](../myCheckMate3Files/validation/validation_plots/atlas_conf_2019_040_T2_delta.png)). Hence this analysis will not be considered.

### Combined Exclusion ###

The combined SModelS and CheckMATE exclusion is shown below. The exclusion curve has been smoothed out a bit to avoid interpolation issues.

![Alt text](BS1p_exclusion.png?raw=true "BS1p exclusion")

### BS2' ###


#### SModelS Exclusion ####

The exclusion obtained by SModelS **relies on the assumption that the efficiencies for  &chi;<sub>1</sub> &chi;<sub>1</sub> production followed by &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + c  + &tau;  are the same as for stau production followed by a decay to &tau; plus MET**.
The upper limit maps for staus end around 450 GeV, so the
exclusion is limited to these values, as shown below:

![Alt text](BS2p_SModelS.png?raw=true "BS1p exclusion SModelS")


There is also a small region excluded by the (suppressed) decays to b plus MET.


#### CheckMATE Exclusion ####

The [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/),  [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) and [ATLAS-EXOT-2018-06](http:/atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/) analyses have been added to CheckMATE in order to test this scenario. The [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/) has a veto for hadronically decaying taus, which reduces its efficiency for the signal.
The results are shown below:

![Alt text](BS2p_CheckMate.png?raw=true "BS1p exclusion CheckMATE")

As it can be seen the mono-jet ([ATLAS-EXOT-2018-06](http:/atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/)) and hadronic MT2 ([CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)) searches are sensitive to the compressed region, while the soft lepton search ([CMS-SUS-16-048](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-048/index.html)) and the tau plus MET search ([ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)) exclude larger mass differences.

Once again the [ATLAS-CONF-2019-040](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2019-040/) analysis in the compressed region might not be reliable (see the compressed region in this [validation plot](../myCheckMate3Files/validation/validation_plots/atlas_conf_2019_040_T2_delta.png)). Hence this analysis is not considered.
