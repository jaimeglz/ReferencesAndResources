import pylab

def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX = False, logY = False):
    """Plots xVals vs. yVals with supplied titles and labels."""
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.legend(loc = 'best') 
    pylab.xlim(0,10)
    pylab.ylim(0,10)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy() 
