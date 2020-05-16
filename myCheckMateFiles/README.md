# CheckMATE Recasting

This folder contains the files for the CheckMATE recasting of the following analyses:

 * Hadronic taus plus MET (139/fb) : [ATLAS-SUSY-2018-04](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/)
 * b-jets plus MET (35.9/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-032/index.html)
 * Hadronic MT2 (137/fb): [CMS-SUS-16-032](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-005/index.html)

The CMS-SUS-16-32 recasting *does not* include the disappearing track search.

## Usage and Installation ##

The files in the [tools](./tools) and [data](./data) folders have to be copied to CheckMATE's folder
and CheckMATE has to be recompiled:

```
<CheckMATE folder>make
```

The files are consistent with the CheckMATE commit [e3caa70](https://github.com/CheckMATE2/checkmate2/commit/e3caa7051b741c85213ab879be33741a5c06ea2e) (Apr 8).



## Validation ##

All the files for validating the results as well as the validation results are stored in [validation](./validation).
See [validation/README](./validation/README.md) for details.

