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

The exclusion obtained by SModelS relies on the assumption that the efficiencies for  &chi;<sub>1</sub> &chi;<sub>1</sub> production followed by &chi;<sub>1</sub> &#8594; &chi;<sub>0</sub> + b  + &nu;  are the same as for sbottom production followed by a decay to bottom plus MET.





--------Everything below needs to be updated-----------------

In this scenario we have BR(&chi;<sub>0</sub> + b + &nu;) ~ 50%, so the most relevant LHC searches are:

 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
 * Hadronic MT2 (35.9/fb): [CMS-SUS-16-036](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-036/index.html)

The hadronic MT2 analyses are relevant for large mass differences, while the b-jet analysis is more relevant at low mass gaps as shown below:

![Alt text](T2bb_SModelSexclusion_BM2.png?raw=true "BM1 exclusion")

The above curves are approximate, because they rely on the assumption that the &chi;<sub>0</sub> + b + &nu; decay presents the same
kinematics as the sbottom to bottom + neutralino (T2bb) decay. The [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
and [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html) analyses have been implemented
in CheckMATE (see [validation](../myCheckMateFiles/validation) ). Furthermore the [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
analysis has provided covariance matrices to allow for a combination of signal regions. This greatly improves the sensitivity of the analysis
and it performs better than the [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) (using the
best signal region only).

Therefore only the [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html) is considered,
using the combination of signal regions, following the SModelS implementation and [CMS-NOTE-2017-001](https://cds.cern.ch/record/2242860?ln=en):

![Alt text](BM2_exclusionAll.png?raw=true "BM2 exclusion")

The limits are somewhat weaker than the SModelS rescaling because we adopt a conservative estimate of the reach including a 20% signal uncertainty
according to the CheckMATE prescription.
On the other hand, the reach extends to smaller mass gaps when compared to the ones obtained by SModelS because the official CMS upper limit
grid for T2bb only goes down to 25 GeV.


![Alt text](exclusion_BM2.png?raw=true "BM2 exclusion")

### BS2' ###

In this scenario we have BR(&chi;<sub>0</sub> + c + &tau;) ~ 100%, so the most relevant LHC searches are:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
 * Soft OS leptons (35.9/fb): [CMS-SUS-16-048](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-048/index.html)


The ATLAS analysis dominate over most of parameter space, while the CMS ones are mostly relevant in the compressed region.
The [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
and [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) analyses have been implemented
in CheckMATE (see [validation](../myCheckMateFiles/validation) ).
However, since the mono-jet searches have equal or better coverage than the CMS analyses,
we only include the [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
result in the final exclusion curve:

![Alt text](BM1_exclusionAll.png?raw=true "BM1 exclusion")

![Alt text](exclusion_BM1.png?raw=true "BM1 exclusion curve")
