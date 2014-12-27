# Plots data and runs regressions either from supplied file name, lists or arrays
# Developed as a result of excercises, data and some code supplied in
# Guttag and Grimson, MITx 6.00.2x Introduction to computational thinking, Lect 7

import pylab, random

# Create a plot with plotData() and/or plotAndFitData() after running this script?


# plotData() only plots the data
runPlotData = False

# plotAndFitData() plots the data and runs the specified regressions
# If True, make sure that file "spingData.txt" exists in the working directory
runPlotAndFitData = True

#set line width
pylab.rcParams['lines.linewidth'] = 2

def getData(fileName, returnHeader=False):
    """
    Reads two columns from a flat text file (begining in line 2 of the file)
    Returns lists with data in column 1 and column 2 of the file.
    Optionally, returnthe first line of the file in a separate variable
    """
    dataFile = open(fileName, 'r')
    col1 = []
    col2 = []
    header = dataFile.readline()
    for line in dataFile:
        c1, c2 = line.split()
        col1.append(float(c1))
        col2.append(float(c2))
    dataFile.close()
    if returnHeader == True:
        return (col2, col1),header
    else:
        return (col2, col1)

def simpLinRegressn(X,Y):
    """
    Obtains the simple least square estimate of the xValues and yValues in X and Y 
    X and Y have to be arrays
    Returns: 
        m = the slope
        b = the y intercept
    """
    
    def mean(X):
    #    Returns the mean value of X
    #   Serves as auxiliary function
        return sum(X) / float(len(X))
    
    meanXVals = mean(X)
    meanYVals = mean(Y)
    xVals = pylab.array(X)
    yVals = pylab.array(Y)
    
    m = ( mean(xVals*yVals) - (meanXVals * meanYVals) ) / ( mean(xVals*xVals) - meanXVals**2 )
    b = meanYVals - m * meanXVals
            
    return m, b

def plotData( fileName='', X=[], Y=[], xMultK=1, 
             grphLabl='', grphTitl='', xLbl='', yLbl='',
             xLim=[0,0], yLim=[0,0], figNum=1 ):
    """
    Plots data from first two columns in text file, 
    or from lists or arrays in X and Y 
    If text file is specified:
        column 1 in the x axis
        column 2 in the y axis
    If X and Y are specified:
        X and Y can be either lists or numpy arrays
    """
    if fileName != '':
        xVals, yVals = getData(fileName)
    elif len(X) !=0 and len(Y) !=0:
        xVals = X
        yVals = Y

    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)    
    if xMultK != 1:
        # For example, convert mass to force (F = mg)
        xVals = xVals * xMultK 

    pylab.figure(figNum)
    pylab.title(grphTitl)
    pylab.xlabel(xLbl)
    pylab.ylabel(yLbl)
#    if xLimMin != 0 and xLimMax !=0:
    if xLim != [0,0]:
        pylab.xlim( xLim[0], xLim[1] )
    if yLim != [0,0]:
        pylab.ylim( yLim[0], yLim[1] )
    pylab.plot(xVals, yVals, 'bo', label = grphLabl)
    pylab.show()

if runPlotData == True:
    plotData('springData.txt', xMultK = 9.81, 
                grphLabl = 'Measured displacements', 
                grphTitl='Measured Displacement of Spring', 
                xLbl='Force (Newtons)', yLbl='Distance (meters)')
    
    #Another test file...
    #plotData('curedPatientData.txt', 
    #            grphTitl='Percentage cured relative to delay in admin. drug', 
    #            xLbl='Delay', yLbl='Percent cured',
    #            xLim=[-10,350] , figNum=2
    #            )

def plotAndFitData(fileName='', 
                    X=[], Y=[], 
                    xMultK=1, grphLabl='', grphTitl='', 
                    xLbl='', yLbl='', 
                    simpLinFit=False, linFit=True, sqFit=True, cubFit=False,
                    xLim=[0,0], yLim=[0,0], figNum=1
                    ):
    """
    Plots and fits data from first two columns in text file, or from X and Y 
    If text file is specified:
        column 1 in the x axis
        column 2 in the y axis
    If X and Y are specified:
        X and Y can be either lists or numpy arrays    
        column 1 in the x axis
        column 2 in the y axis
    """
    if fileName != '':
        xVals, yVals = getData(fileName)
    elif len(X) !=0 and len(Y) !=0:
        xVals = X
        yVals = Y

    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)    
    if xMultK != 1:
        # For example, convert mass to force (F = mg)
        xVals = xVals * xMultK 

    pylab.figure(figNum)
    pylab.title(grphTitl)
    pylab.xlabel(xLbl)
    pylab.ylabel(yLbl)
#    if xLimMin != 0 and xLimMax !=0:
    if xLim != [0,0]:
        pylab.xlim( xLim[0], xLim[1] )
    if yLim != [0,0]:
        pylab.ylim( yLim[0], yLim[1] )
    pylab.plot(xVals, yVals, 'bo', label = grphLabl)
    
    # Now, lets fit the data (if we are asked to do so)
    if simpLinFit == True:
        a,b = simpLinRegressn(xVals,yVals)
        estYVals = a*xVals + b
        k = 1/a
        pylab.plot(xVals, estYVals, label = 'Simple linear fit, k = '
               + str(round(k, 5)))        
         
    if linFit == True:
        a,b = pylab.polyfit(xVals, yVals, 1)
        # use line equation to graph predicted values
        estYVals = a*xVals + b
        k = 1/a
        pylab.plot(xVals, estYVals, label = 'Linear fit, k = '
               + str(round(k, 5)))        
    
    if sqFit == True:
        a,b,c = pylab.polyfit(xVals, yVals, 2)
        estYVals = a*(xVals**2) + b*xVals + c
        pylab.plot(xVals, estYVals, label = 'Square fit')
    
    if cubFit == True:
        a,b,c,d = pylab.polyfit(xVals, yVals, 3)
        estYVals = a*(xVals**3) + b*xVals**2 + c*xVals + d
        pylab.plot(xVals, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')
    pylab.show()

# Some simple test cases:
if runPlotAndFitData == True:
    plotAndFitData('springData.txt', xMultK = 9.81, 
                    grphLabl = 'Measured displacements', 
                    grphTitl='Measured Displacement of Spring', 
                    xLbl='Force (Newtons)', yLbl='Distance (meters)', 
                    linFit=True, sqFit=True, cubFit=True,
                    figNum=3
                    )
    #Another test file...
    #plotAndFitData('curedPatientData.txt', 
    #                grphLabl = 'Percent cured',
    #                grphTitl='Percentage cured relative to delay in admin. drug', 
    #                xLbl='Delay', yLbl='Percent cured',
    #                linFit=False, sqFit=True, cubFit=True,
    #                xLim=[-10,350] , 
    #                figNum= 4
    #                )
# A simple test case:
    #X,Y = [1,2,4 ],[2,1,3 ]
    #plotAndFitData(fileName='', X=X, Y=Y, grphLabl = 'Crazy coords', grphTitl='Some crazy coordinates', xLbl='x', yLbl='y', simpLinFit=True, linFit=True, sqFit=False, xLim=[0,10], yLim=[0,10])
