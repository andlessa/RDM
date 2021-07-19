#!/usr/bin/env python

"""
Simple code for computing the combined upper limit for a given signal over several signal regions (bins).

It assumes the simplified likelihood framework, using
the covariant matrix for all signal regions.
"""

from simplifiedLikelihoods import Data, UpperLimitComputer
import sys,os
import numpy as np


def getCombinedR(data,cov,orderSRs,deltas_rel=0.):
    """
    Compute a combined r-value using the covariance matrix.

    :param data: 2-d numpy array with number of observed events (obs),
                 number of signal events (s),
                 number of expected background events (bkg) for each
                 signal region (sr)
    :param cov: covariace matrix (CovarianceHandler object)
    :param orderSRs: dictionary with the bin labels as keys and the SR labels as values
                     according to the order defined in the covariance matrix.
    :param deltas_rel: Relative uncertainty for the number of signal events.

    :return: Combined r-value (sum(nsig)/ul_combined)
    """

    #Get bin order and set the dataset order according to the bin order
    bins = cov.datasetOrder
    order = [orderSRs[b] for b in bins]

    nobs = [0]*len(order)
    nsig = [0]*len(order)
    bg = [0]*len(order)
    # Get ordered data for the specified SRs
    for pt in data:
        if not pt['sr'] in order:
            continue
        i = order.index(pt['sr'])
        nobs[i] = int(pt['obs'])
        nsig[i] = pt['s']
        bg[i] = pt['bkg']

    #In case no SRs are found:
    if sum(nsig) == 0 or sum(bg) == 0:
        return 0.0,0.0

    #Compute the combined upper limit
    ulObs,ulExp = getCombinedUpperLimitFor(nobs, bg, nsig,
                    cov.covariance, deltas_rel)

    #Compute the new r-value:
    robs = sum(nsig)/ulObs
    rexp = sum(nsig)/ulExp

    return robs,rexp

def getCombinedUpperLimitFor(nobs, bg, nsig, cov, deltas_rel=0.2):
    """
    Get combined upper limit.

    :param nobs: list of observed events in each signal region. The list
                    should obey the ordering in the covariance matrix.
    :param bg: list of expected BG events in each signal region. The list
                    should obey the ordering in the covariance matrix.
    :param nsig: list of signal events in each signal region. The list
                    should be consistent with the covariance matrix.
    :param deltas_rel: relative uncertainty in signal (float). Default value is 20%.
    :returns: upper limit on the number of signal events summed over all signal regions
    """
    computer = UpperLimitComputer(ntoys=10000)

    ulObs = computer.ulSigma(Data(observed=nobs, backgrounds=bg, covariance=cov,
                                 third_moment=None, nsignal=nsig, deltas_rel=deltas_rel),
                           marginalize=False, expected=False)

    ulExp = computer.ulSigma(Data(observed=nobs, backgrounds=bg, covariance=cov,
                                 third_moment=None, nsignal=nsig, deltas_rel=deltas_rel),
                           marginalize=False, expected=True)


    return ulObs,ulExp

class CovarianceHandler:
    """Basic class to handle convariance matrices."""

    def __init__ ( self, filename, histoname, max_datasets=None,
                   aggregate = None , triangular=False):
        """Load the covariance matrix from ROOT file."""
        import ROOT
        f=ROOT.TFile(filename)
        h=self.getHistogram(f, histoname)
        xaxis = h.GetXaxis()
        self.n=h.GetNbinsX()+1
        if max_datasets:
            self.n=min(max_datasets+1,self.n)
        self.datasetOrder = []
        self.covariance = []
        self.blinded_regions = []
        for i in range ( 1, self.n ):
            if i in self.blinded_regions:
                continue
            self.datasetOrder.append(xaxis.GetBinLabel(i))
            row = []
            for j in range ( 1, self.n ):
                if j in self.blinded_regions:
                    continue
                el = h.GetBinContent(i,j)
                if i==j and el < 1e-4:
                   print( "variance in the covariance matrix at position %d has a very small (%g) value" % (i,el) )
                   el = 1e-4
                row.append(el)
            self.covariance.append(row)

        if aggregate != None:
            ## aggregate the stuff
            self.aggregateThis(aggregate)

        if triangular:
            c = np.array(self.covariance)
            if (np.triu(c) == c).all() or (np.tril(c) == c).all():
                self.covariance = c + c.transpose() - np.diag(np.diag(c))
                self.covariance = self.covariance.tolist()
        self.checkCovarianceMatrix()

    def computeAggCov(self, agg1, agg2 ):
        """Compute the covariance between agg1 and agg2."""
        C=0.
        for i in agg1:
            for j in agg2:
                C+=self.covariance[i-1][j-1]
        return C

    def checkCovarianceMatrix( self ):
        """Quick check if the covariance matrix is invertible."""
        from simplifiedLikelihoods import Data
        n=len(self.covariance)
        m=Data( [0.]*n, [0.]*n, self.covariance )
        # print( "Check %d-dim covariance matrix for positive definiteness." % n)
        try:
            I=(m.covariance)**(-1)
        except Exception as e:
            print( "Inversion failed. %s" % e)
            sys.exit()
        try:
            from scipy import stats
            l=stats.multivariate_normal.logpdf([0.]*n,mean=[0.]*n,cov=m.covariance)
        except Exception as e:
            import numpy
            print( "computation of logpdf failed: %s" % e )
            print( "the diagonal reads: %s " % ( numpy.diag ( m.covariance ) ) )
            sys.exit()

    def getHistogram( self, f, histoname ):
        """Retrieve histogram.

        :param f: filehandle
        """
        h=f.Get ( histoname )
        if h: return h
        if not "/" in histoname:
            print( "cannot find %s in %s" % (histoname, f.GetName()))
            sys.exit()
        tokens = histoname.split("/")
        if not len(tokens)==2:
            print("cannot interpret histoname %s in %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        c= f.Get ( tokens[0] )
        if not c:
            print( "cannot retrieve %s from %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        if c.ClassName() == "TCanvas":
            h=c.GetPrimitive ( tokens[1] )
            if h: return h
            print( "cannot retrieve %s from %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        print( "cannot interpret %s in %s" % \
                        ( histoname, f.name ) )
        sys.exit()


def addCombined(filename,analysis,covmatrix,histoname,orderSRs,label='Combined'):
    """
    Reads the output from CheckMATE (total_results.txt) and adds one line corresponding to the combined limit

    :param filename: path to the total_resuts.txt file
    :param analyis: analysis label for which the combined limit will be computed
    :param covmatrix: path to the covariance matrix (ROOT file)
    """


    if not os.path.isfile(filename):
        print('File %s not found' %filename)
        return False

    #Load results
    data = np.genfromtxt(filename,names=True,
                dtype=None,encoding=None)

    #Select the desired analysis
    delete_rows = np.where(data['analysis'] != analysis)
    if len(delete_rows) == len(data):
        print("Analysis %s not found in data" %analysis)
        return False
    data = np.delete(data,delete_rows,axis=0)

    #Get convariance matrix
    if not os.path.isfile(covmatrix):
        print('File %s not found' %covmatrix)
        return False

    cov = CovarianceHandler(covmatrix, histoname)

    #Compute observed and expected r:
    robs,rexp = getCombinedR(data,cov,orderSRs, deltas_rel=0.0)
    robscons,_ = getCombinedR(data,cov,orderSRs, deltas_rel=0.8)
    # robscons = (1.0-1.64*0.2)*robs
    print(robs,rexp,robscons)


    combPt = [0.]*len(data.dtype.names)
    combPt[data.dtype.names.index('robs')] = robs
    combPt[data.dtype.names.index('rexp')] = rexp
    if 'robscons' in data.dtype.names:
        combPt[data.dtype.names.index('robscons')] = robscons
    combPt[data.dtype.names.index('analysis')] = analysis
    combPt[data.dtype.names.index('sr')] = label

    data = np.append(data, np.array([tuple(combPt)], dtype=data.dtype))

    #Add combined result to total_results.txt:
    analysisSize = str(max([len(pt['analysis']) for pt in data])+2)
    srsSize = str(max([len(pt['sr']) for pt in data])+2)
    other = 9
    header = ''
    fmt = []
    for name in data.dtype.names:
        if name == 'analysis':
            header += '%-'+analysisSize+'s'
            fmt.append('%-'+analysisSize+'s')
        elif name == 'sr':
            header += '%-'+srsSize+'s'
            fmt.append('%-'+srsSize+'s')
        else:
            l = max(other,len(name))+2
            header += '%-'+str(l)+'s'
            fmt.append('%1.3e'+' '*(l-10))

    header = header %data.dtype.names

    np.savetxt(filename,data,header=header,fmt = fmt)
    return True


if __name__ == "__main__":

    filename='./total_results.txt'
    analysis = 'cms_sus_16_032'
    orderSRs = {'1' : 'HT_200_MCT_150', '2' : 'HT_200_MCT_250', '3' : 'HT_200_MCT_350', '4' : 'HT_200_MCT_450',
                '5' : 'HT_500_MCT_150', '6' : 'HT_500_MCT_250', '7' : 'HT_500_MCT_350', '8' : 'HT_500_MCT_450',
                '9' : 'HT_500_MCT_600', '10' : 'HT_1000_MCT_150', '11' : 'HT_1000_MCT_250', '12' : 'HT_1000_MCT_350',
                '13' : 'HT_1000_MCT_450', '14' : 'HT_1000_MCT_600', '15' : 'HT_1000_MCT_800'}

    histoname = 'Canvas_1/Cov'
    covmatrix = './CMS_data/CMS-SUS-16-032_Figure-aux_003.root'
    label = 'Combined_noncomp'

    addCombined(filename,analysis,covmatrix,histoname,orderSRs,label)

    orderSRs = {'1' : '1b_ETmiss_250', '2' : '1b_ETmiss_300', '3' : '1b_ETmiss_500', '4' : '1b_ETmiss_750', '5' : '1b_ETmiss_1000',
     '6' : '2b_ETmiss_250', '7' : '2b_ETmiss_250_HT_100', '8' : '2b_ETmiss_300', '9' : '2b_ETmiss_300_HT_100', '10' : '2b_ETmiss_500', '11' : '2b_ETmiss_500_HT_100',
     '12' : '1c_ETmiss_250', '13' : '1c_ETmiss_300', '14' : '1c_ETmiss_500', '15' : '1c_ETmiss_750', '16' : '1c_ETmiss_1000',
     '17' : '2c_ETmiss_250', '18' : '2c_ETmiss_250_HT_100', '19' : '2c_ETmiss_300', '20' : '2c_ETmiss_300_HT_100', '21' : '2c_ETmiss_500', '22' : '2c_ETmiss_500_HT_100', '23' : '2c_ETmiss_750', '24' : '2c_ETmiss_750_HT_100',
     '25' : 'NSV_ETmiss_250', '26' : 'NSV_ETmiss_300', '27' : 'NSV_ETmiss_500', '28' : 'NSV_ETmiss_750', '29' : 'NSV_ETmiss_1000',
     '30' : '0b_ETmiss_300', '31' : '0b_ETmiss_500', '32' : '0b_ETmiss_750', '33' : '0b_ETmiss_1000', '34' : '0b_ETmiss_1250'}
    #File and histogram containing the covariance matrix
    histoname = 'Canvas_1/Cov'
    covmatrix = './CMS_data/CMS-SUS-16-032_Figure-aux_004.root'
    label = 'Combined_comp'

    addCombined(filename,analysis,covmatrix,histoname,orderSRs,label)
