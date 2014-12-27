#   Draws some basic histograms with different probability distributions

import pylab, random

# Run the function after running the current file?
runTestErrors = True

def testErrors(ntrials=10000, npts=100, numBins=50):
    # Generate plot for triangular distribution
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.triangular(-1,1)
        results[i] =s

    # plot in a histogram
    pylab.hist(results,bins=numBins,alpha=0.25,color='b', label='Triangular')

    # Generate and plot a normal distribution
    normalDResults = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.uniform(-1,1) 
        normalDResults[i] =s

    # Plot the normal distribution data, and get the data in arrays
    barYSize02, bins, patches = pylab.hist(normalDResults,bins=50,alpha=0.25,
                                            color='c', label='Uniform')
    
    # Set limits in the x axis
    pylab.xlim(-40,70)

    # Generate and plot a beta distribution
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0   # sum of random points
        for j in xrange(npts):
            s += random.betavariate(1,1)
        results[i] =s
    pylab.hist(results,bins=50,alpha=0.25,color='m',label='Beta')
    pylab.title('Plot random points for different distributions')
    pylab.text(  -38.0, 5.0, (' Trials: ' + str(ntrials) )  )
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')
    pylab.legend(loc = 'best')
    pylab.show()

    return normalDResults, barYSize02, bins, patches

if runTestErrors == True:
    testErrors()
