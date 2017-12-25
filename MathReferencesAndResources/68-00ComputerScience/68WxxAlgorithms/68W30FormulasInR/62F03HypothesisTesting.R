# 62F03HypothesisTesting
# 
# Author: Jaime
###############################################################################

# z-score
 
zScor <- function(x, popMean, popSDev) {
	(x-popMean)/popSDev
}

# install.packages(c("R.basic"), contriburl="http://www.braju.com/R/repos/")
library(R.basic)
# ?zscore()
sampl <- read.csv("C:/Projects/ReferencesAndResources/MathReferencesAndResources/68-00ComputerScience/68WxxAlgorithms/68W30FormulasInR/Samples.csv")
# sampl <- read.table("clipboard", header=T, sep="\t")
zscore(sampl[,2])

# ztest
x = scan("C:/Users/Jaime/Dropbox/Refer/Matemat/ApuntesRefsyRecursos/68a94DxxMatemAplicadas/68-00CienciasComputacion/68WxxAlgoritmos/68W30_00A22FormulasEnR/ChiYauRTutorialSRC/lightbulbs.txt")
xbar = mean(x)         # sample mean
mu0 = 10000            # hypothesized value
sigma = 120            # population standard deviation
n = length(x)          # sample size
z = (xbar-mu0)/(sigma/sqrt(n))
pval = pnorm(z)
pval

# Alternative: use z.test from TeachingDemos 
library(TeachingDemos)
test = z.test(x, mu=mu0, stdev=sigma, 
		alternative="less")
test$p.value

# From KIExploRx: one tailed test   
# rare in health sciences, more common in industrial process control
x01=seq(50,140,length=200)
y1=dnorm(x01,80, 10)
plot(x01,y1,type='l',lwd=2,col='red')
y2=dnorm(x01,110, 10)
lines(x01,y2,type='l',lwd=2,col='blue')
abline(v=qnorm(0.95,80,10)) 

# From KIExploRx: Two-tailed Z test
xrange <- seq(60, 120, 1) 
plot(xrange, dnorm(xrange, 90, 10), type="l", xlim=c(60, 120), main="two-tailed test") 
# pnorm(70, 90, 10)  
abline(v=70) 
cord.x <- c(60,seq(60,70,1),70) 
cord.y <- c(0,dnorm(seq(60, 70, 1), 90, 10),0) 
polygon(cord.x,cord.y,col='skyblue') 
cord.x1 <- c(110,seq(110,120,1),120) 
cord.y1 <- c(0,dnorm(seq(110, 120, 1), 90, 10),0) 
polygon(cord.x1,cord.y1,col='skyblue') 
text(65, 0.005, round(pnorm(70, 90, 10), 3)) 
text(115, 0.005, round(pnorm(70, 90, 10), 3)) 
text(75, 0.02,  " p = 0.070 "  ) 

#two tailed test
#common in the health sciences, because in most cases, both
#an increase or a decrease in a variable would affect health
x01=seq(50,140,length=200)
y1=dnorm(x01,80, 10)
plot(x01,y1,type='l',lwd=2,col='red')
y2=dnorm(x01,110, 10)
lines(x01,y2,type='l',lwd=2,col='blue')
abline(v=qnorm(0.025,80,10))
abline(v=qnorm(0.975,80,10))

#colour the rejection area, also referred to as alpha.
#If the p-value is equal to or lower than alpha - reject the null hypothesis
x=seq(50,140,length=200)
y1=dnorm(x,80, 10)
plot(x,y1,type='l',lwd=2,col='red')
y2=dnorm(x,110, 10)
lines(x,y2,type='l',lwd=2,col='blue')
cord.x1 <- c((round(qnorm(0.975, 80, 10))),seq((round(qnorm(0.975, 80, 10))), 120,1),120) 
cord.y1 <- c(0,dnorm(seq((round(qnorm(0.975, 80, 10))), 120, 1), 80, 10),0) 
polygon(cord.x1,cord.y1,col='red')
cord.x2 <- c(50,seq(50,round(qnorm(0.025, 80, 10),1)),round(qnorm(0.025, 80, 10))) 
cord.y2 <- c(0,dnorm(seq(50,round(qnorm(0.025, 80, 10),1)), 80, 10),0) 
polygon(cord.x2,cord.y2,col='red')

#Imagine that the alternative hypothesis were true. 
#Beta is the risk that you will keep (=not reject) the false null hypothesis
x=seq(50,140,length=200)
y1=dnorm(x,80, 10)
plot(x,y1,type='l',lwd=2,col='red')
y2=dnorm(x,110, 10)
lines(x,y2,type='l',lwd=2,col='blue')
cord.x2<- c(0,seq((round(1-qnorm(0.025,110,10))),100,1),100)
cord.y2 <- c(0,dnorm(seq((round(1-qnorm(0.025, 110, 10))), 100, 1), 110, 10),0) 
polygon(cord.x2,cord.y2,col='red')
abline(v=round(qnorm(0.975, 80, 10, lower.tail=T)))
abline(v=round(qnorm(0.025, 80, 10, lower.tail=T)))
text(95,0.005, "ß ",xpd=5)

#Statistical power, 1-beta, is the probability to reject a false null hypothesis
x<- seq(50,140,length=200)
y1<- dnorm(x,80, 10)
plot(x,y1,type='l',lwd=2,col='red')
y2<- dnorm(x,110, 10)
lines(x,y2,type='l',lwd=2,col='blue')
cord.x2<- c(0,seq((round(1-qnorm(0.025,110,10))),100,1),100)
cord.y2 <- c(0,dnorm(seq((round(1-qnorm(0.025, 110, 10))), 100, 1), 110, 10),0) 
polygon(cord.x2,cord.y2,col='red')
abline(v=round(qnorm(0.975, 80, 10, lower.tail=T)))
abline(v=round(qnorm(0.025, 80, 10, lower.tail=T)))
cord.x1 <- c(100,seq(round(qnorm(0.975, 80, 10, lower.tail=T)), 140,1),140) 
cord.y1 <- c(0,dnorm(seq(round(qnorm(0.975, 80, 10, lower.tail=T)),140, 1), 110, 10),0) 
polygon(cord.x1,cord.y1,col='6')
text(95,0.005, "ß ",xpd=5)
text(115,0.005, "1-ß ",xpd=5)
