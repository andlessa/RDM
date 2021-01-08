#!/usr/bin/python3

# %% Load required modules
import os,sys,time
import numpy as np
from scipy.interpolate import interp1d, LinearNDInterpolator,griddata
from scipy.spatial import ConvexHull,Delaunay
import progressbar


def trim1D(zpts,xpts,ypts,maxDiff = 5e-2,minY=1e-10):

    t0 = time.time()
    y = np.array(ypts)
    x = np.array(xpts)
    z = np.array(zpts)
    # #Now replace all values below minY by 0.0:
    y = np.where(y > minY,y,0.0)

    #Slice data according to x coordinates:
    dataDict = {}
    for i,xval in enumerate(x):
        xx = tuple(xval)
        if not xx in dataDict:
            dataDict[xx] = []
        dataDict[xx].append([z[i],y[i],i])

    #Sort data
    for xx in dataDict:
        dataDict[xx] = np.array(sorted(dataDict[xx],reverse=True))

    # Now walk along z direction for each combination of x values
    # and check which points in the z-axis can be dropped without affecting the interpolation
    keepLines = []
    for xx in dataDict:
        trimmedData = []
        for i,pt in enumerate(dataDict[xx]):
            if i == 0 or i == len(dataDict[xx])-1:
                trimmedData.append(pt) #Always keep first and last points
                keepLines.append(int(pt[-1]))
                continue
            zcurrent = pt[0]
            ycurrent = pt[1]
            #Add next point to trimmedData
            zy = np.array(trimmedData + [dataDict[xx][i+1]])
            #Check if the interpolatation at all previous points and at the current point is accepatble:
            fInterp = interp1d(zy[:,0],zy[:,1],kind='linear')
            valsInterp = fInterp(dataDict[xx][:i+1,0])
            vals = dataDict[xx][:i+1,1]


            #Compare interpolation with correct values
            valsN = np.where(vals > 0.0, vals, minY) #replace zero effs by minY for division
            relDiff = np.where(vals > 0.0,np.abs(vals-valsInterp)/valsN,maxDiff*(valsInterp/minY))

            #If maximum relative difference is higher than relDiff, keep point:
            if relDiff.max() > maxDiff:
                trimmedData.append(pt)
                keepLines.append(pt[-1])

    #Make sure all the points in the convexHull are included:
    cHull = ConvexHull(np.insert(x,len(x[0]),values=z,axis=1))
    keepLines += cHull.vertices.tolist()
    keepLines = list(set([int(kl) for kl in keepLines]))

    print('Data successfully trimmed down to %1.0f%% (%i/%i) in %1.1f min' %(100.0*len(keepLines)/len(x),
                                                                                  len(keepLines),len(x),
                                                                                  (time.time()-t0)/60.))


    return keepLines

def testTrimmedGrid(fullData,trimmedData,minY=1e-10):

    #Finally, check quality of trimming:
    diffs = []
    fdata = np.array(fullData)
    tdata = np.array(trimmedData)
    if len(trimmedData) < len(fullData):
        x = fdata[:,:-1]
        y = fdata[:,-1]
        x_trim = tdata[:,:-1]
        y_trim = tdata[:,-1]

        #Compute interpolation at all the original points
        y_interpF = LinearNDInterpolator(x_trim,y_trim)
        y_interp = y_interpF(x)

        #For some reason interpolating at many points at once return NaN even
        #when all the points are inside the grid. Re-compute for these cases:
        for i in np.where(np.isnan(y_interp))[0]:
            y_interp[i] = y_interpF(x[i])

        #Replace all NaN values to the original values (ignore outside grid evaluations)
        outsideInterp = np.where(np.isnan(y_interp))[0]

        if len(outsideInterp) > 0:
            print('Interpolation outside trimmed grid happened %i times'
                                %(len(outsideInterp)))
        y_interp = np.where(np.isnan(y_interp),y,y_interp)

        #Set all values below minY to minY:
        y = np.where(y > minY, y, minY)
        y_interp = np.where(y_interp > minY, y_interp, minY)

        diff = np.abs(y_interp-y)/y

        print('Maximum relative difference = ',diff.max())

    return diff

def removeWidth(data):

    #Get minimum width:
    minWidth = min(data['width'])
    #Get lines with minimum width:
    minLines = np.where(data['width'] == minWidth)[0]

    print('Removing widths reduced data down to %1.0f%% (%i/%i)' %(100.0*len(minLines)/len(data),
                                                                         len(minLines),len(data)))

    return data[minLines]

def trimGrid(points,values,minY = 1e-2,maxDiff = 5e-2,random=True):

    t0 = time.time()

    #Replace all small values by zero:
    values = np.where(values > minY,values,0.0)
    #Get triangulation:
    tri = Delaunay(points)
    #Get convex hull
    cHullvertices = list(set(tri.convex_hull.flatten()))
    #Get infor about neighbors:
    indptr,indices = tri.vertex_neighbor_vertices

    indexKeep = []
    rmvPts = set()

    #If random = True, randomly walk through the grid:
    if random:
        indexList = np.random.permutation(len(tri.points))
    else:
        indexList = np.arange(len(tri.points))

    pb = progressbar.ProgressBar(widgets=["checking point ",progressbar.Counter(),
            "/%d " % len(indexList), progressbar.Percentage(),
            progressbar.Bar( marker=progressbar.RotatingMarker() ),
            progressbar.AdaptiveETA()])
    pb.maxval = len(indexList)
    pb.start()

    for counter,i in enumerate(indexList):
        pb.update(counter)
        if i in cHullvertices or i in rmvPts:
            indexKeep.append(i)
            continue #Do not remove pts in the convexhull or of simplices which already had a point removed

        #Get the neighbors to the point
        neighbors = indices[indptr[i]:indptr[i+1]]
        #Using a linear interpolator with neighbors check interpolation value at point i
        y_interp = griddata(tri.points[neighbors],values[neighbors],tri.points[i],method='linear')[0]
        y = values[i]

        if y < minY:
            diff = max(0,(y_interp-minY)/minY) #For values smaller than minY, just require y_interp < (1+maxDiff)*minY
        else:
            diff = abs(y_interp-y)/y #Relative difference

        if diff > maxDiff:
            keepPoint = True
        else:
            keepPoint = False

        if keepPoint:
            indexKeep.append(i)
        else:
            rmvPts.add(i)
            rmvPts = rmvPts.union(neighbors)

    pb.finish()
    print('Data successfully trimmed down to %1.0f%% (%i/%i) in %1.1f min' %(100.0*len(indexKeep)/len(points),
                                                                                  len(indexKeep),len(points),
                                                                                  (time.time()-t0)/60.))


    return indexKeep
