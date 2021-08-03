# CheckMATE Recasting Validation:

This folder contains the files necessary for validating the ATLAS and CMS analyses implemented in CheckMATE.

All the SLHA files used for validation are stored in [validation_slha.tar.gz](./validation_slha.tar.gz),
while the CheckMATE output for each file/analysis is stored in [validation_result.tar.gz](./validation_results.tar.gz).

The main steering cards for running CheckMATE (using [runCheckMateScan.py](../../runCheckMateScan.py) )
are:

 * [validation_atlas_susy_2018_04.ini](validation_atlas_susy_2018_04.ini)
 * [validation_cms_sus_16_032.ini](validation_cms_sus_16_032.ini)
 * [validation_cms_sus_19_005.ini](validation_cms_sus_19_005.ini)
 * [validation_atlas_exot_2018_06.ini](validation_atlas_exot_2018_06.ini)
 * [validation_atlas_conf_2019_040.ini](validation_atlas_conf_2019_040.ini)


The CMS-SUS-16-32 analysis provided the covariance matrices (see [CMS_data](./validation_plots/CMS_data)), which are used
for computing the exclusion curve in the validation plots.
The calculation of the combined results can be done running:

``
./addCombinedLimit.py -f <results folder>
``

where results_folder is the folder containing the CheckMATE results. The combination of signal regions will be added to the total_results.txt file as a new signal regions and can be used to compute the exclusion curve.


Although ATLAS-SUSY-2018-04 has provided likelihoods for computing a combined Stau limit, these *are not* used, thus the validation
compares the official exclusions for both signal regions.

## Validation Plots ##

The following plots can be obtained running  plotValidation_xxx.py in the [validation_plots](./validation_plots) folder
using the data stored in [validation_slha.tar.gz](./validation_slha.tar.gz) and  [validation_result.tar.gz](./validation_results.tar.gz):


* [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/) (arXiv:1911.06660):

![Alt text](validation_plots/atlas_susy_2018_04_Stau.png?raw=true "Validation Plot")

* [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/) (arXiv:1707.07274)

![Alt text](validation_plots/cms_sus_16_032_T2cc.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_16_032_T2bb.png?raw=true "Validation Plot")


* [CMS-SUS-19-005](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html) (arXiv:1909.03460)

![Alt text](validation_plots/cms_sus_19_005_T2bb.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T2tt.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T2cc.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T1.png?raw=true "Validation Plot")


* [ATLAS-EXOT-2018-06](http:/atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2018-06/) (arXiv:2102.10874)


![Alt text](validation_plots/atlas_exot_2018_06_T2bb.png?raw=true "Validation Plot")

![Alt text](validation_plots/atlas_exot_2018_06_T2cc.png?raw=true "Validation Plot")


* [ATLAS-CONF-2019-040](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2019-040/) (ATLAS-SUSY-2018-22):


![Alt text](validation_plots/atlas_conf_2019_040_T2.png?raw=true "Validation Plot")


![Alt text](validation_plots/atlas_conf_2019_040_T2_delta.png?raw=true "Validation Plot")
