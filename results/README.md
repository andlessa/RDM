# RDM Results

This folder contains the results for the RDM model. The modified version of CheckMATE has been used to identify the most relevant analyses
for the two main benchmark scenarios:

 * BM1: (&lambda;<sub>L</sub>)<sub>33</sub> = 0.16, (&lambda;<sub>R</sub>)<sub>33</sub> = 2.0, m<sub>S<sub>1</sub></sub> = 1 TeV
 * BM2: (&lambda;<sub>L</sub>)<sub>33</sub> = 0.6, (&lambda;<sub>R</sub>)<sub>23</sub> = 0.5, m<sub>S<sub>1</sub></sub> = 1 TeV

The first benchmark (BM1) has the &chi;<sub>1</sub> decaying almost 100% to &chi;<sub>0</sub> + c + &tau;, while BM2 has
&chi;<sub>1</sub> decaying to &chi;<sub>0</sub> + b  + &nu; (40-60%), to &chi;<sub>0</sub> + t  + &tau; (0-30%) and to &chi;<sub>0</sub> + c  + &tau; (30%).
In both benchmarks the &chi;<sub>1</sub> and &chi;<sub>0</sub> masses are free parameters.


## LHC MET Searches ##

### BM1 ###

In this scenario we have BR(&chi;<sub>0</sub> + c + &tau;) ~ 100%, so the most relevant LHC searches are:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
 * Soft OS leptons (35.9/fb): [CMS-SUS-16-048](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-048/index.html)
 
The ATLAS analysis dominate over most of parameter space, while the CMS ones are mostly relevant in the compressed region.
However, since the mono-jet searches have equal or better coverage than the CMS analyses, 
we only include the [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
result in the final exclusion curve:

![Alt text](BM1_exclusionAll.png?raw=true "BM1 exclusion")


### BM2 ###

In this scenario we have BR(&chi;<sub>0</sub> + b + &nu;) ~ 50%, so the most relevant LHC searches are:

 * Hadronic MT2 (137/fb): [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
 
The hadronic MT2 analysis dominate over most of parameter space, while the b-jet plut MET is mostly relevant in the compressed region, due to the
tagging of soft b-jets using a secondary vertex algorithm.
Although the [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html) results do include
the combination of results through the covariance matrix provided by CMS, the [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)
rely only on the best (expected) signal region, so the limits are weaker than the ones obtained by a simple rescaling of the T2bb limits.


![Alt text](BM2_exclusionAll.png?raw=true "BM2 exclusion")
