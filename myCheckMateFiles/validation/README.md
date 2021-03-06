# CheckMATE Recasting Validation:

This folder contains the files necessary for validating the ATLAS and CMS analyses implemented in CheckMATE.

All the SLHA files used for validation are stored in [validation_slha.tar.gz](./validation_slha.tar.gz),
while the CheckMATE output for each file/analysis is stored in [validation_result.tar.gz](./validation_results.tar.gz).

The main steering cards for running CheckMATE (using [runCheckMateScan.py](../../runCheckMateScan.py) )
are:

 * [validation_atlas_susy_2018_04.dat](validation_atlas_susy_2018_04.dat)
 * [validation_cms_sus_16_032.dat](validation_cms_sus_16_032.dat)
 * [validation_cms_sus_19_005.dat](validation_cms_sus_19_005.dat)

The CMS-SUS-16-32 analysis provided the covariance matrices (see [CMS_data](./validation_plots/CMS_data)), which are used
for computing the exclusion curve in the validation plots.
Although ATLAS-SUSY-2018-04 has provided likelihoods for computing a combined Stau limit, these *are not* used, thus the validation
compares the official exclusions for both signal regions.

## Validation Plots ##

The following plots can be obtained running  plotValidation_xxx.py in the [validation_plots](./validation_plots) folder
using the data stored in [validation_slha.tar.gz](./validation_slha.tar.gz) and  [validation_result.tar.gz](./validation_results.tar.gz):


* ATLAS-SUSY-2018-04:

![Alt text](validation_plots/atlas_susy_2018_04_Stau.png?raw=true "Validation Plot")

* CMS-SUS-16-032:

![Alt text](validation_plots/cms_sus_16_032_Stop.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_16_032_T2bb.png?raw=true "Validation Plot")


* CMS-SUS-19-005:

![Alt text](validation_plots/cms_sus_19_005_T2bb.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T2tt.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T2cc.png?raw=true "Validation Plot")

![Alt text](validation_plots/cms_sus_19_005_T1.png?raw=true "Validation Plot")

