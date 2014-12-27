# Guttag and Grimson, MITx 6.00.2x Introduction to computational thinking, Lect 4

import random, pylab

#   flipPlot2() is the default option: it displays more graphs than flipPlot()
#   both plot results of 2**minExp to 2**maxExp coin flips
runFlipPlot2 = True
#    flipPlot displays only two basic graphs
runFlipPlot = False

#set line width
pylab.rcParams['lines.linewidth'] = 2
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5


def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return numHeads, numTails

def flipPlot(minExp, maxExp, numTrials, displayOp='bo'):
    meanRatios = []
    meanDiffs = []
    ratiosSDs =  []
    diffsSDs =  []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))

    pylab.figure(1)    
    # Mean Heads/Tails Ratiosdot representaton
    pylab.plot(xAxis, meanRatios, displayOp)
    
    pylab.title('Mean Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips (log scale)')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.show()    
    
    # plot StdDev 
    pylab.figure(2)        
    pylab.plot(xAxis, ratiosSDs, displayOp)
    pylab.title('SD Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()
    
    pass


def flipPlot2(minExp, maxExp, numTrials, displayOp='bo'):
    """
    Displays additional graphs 
    """
    meanRatios = []
    meanDiffs = []
    ratiosSDs =  []
    diffsSDs =  []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    
    pylab.figure(3)
    pylab.plot(xAxis, meanRatios, displayOp)
    
    pylab.title('Mean Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.show()    

    pylab.figure(4)
    pylab.plot(xAxis, ratiosSDs, displayOp)
    pylab.title('SD Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()    
    
    #Additional code to look at difference in abolute
    #number of heads and tails
    pylab.figure(5)
    pylab.title('Mean abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean abs(#Heads - #Tails')
    pylab.plot(xAxis, meanDiffs, displayOp)
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

    pylab.figure(6)
    pylab.plot(xAxis, diffsSDs, displayOp)
    pylab.title('SD abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

if runFlipPlot == True:
    # Display data points as blue dots
#    flipPlot(4, 20, 20, displayOp='bo')
    # Display data points as a line
    flipPlot(4, 20, 20, displayOp='')    

if runFlipPlot2 == True:
    # Display data points as blue dots
#
    # Display data points as a line
    flipPlot2(4, 20, 20, displayOp='')    
