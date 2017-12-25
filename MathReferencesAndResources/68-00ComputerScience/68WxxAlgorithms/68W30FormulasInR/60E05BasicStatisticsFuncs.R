##############################################################################
#
#	60E05BasicStatisticsFuncs.R    
#	R script
#	Date created: Jan 4, 2015
#	Copied mainly from KIexpoRx course
###############################################################################

a <- c(1,2,3,4,5,7,8,10,11)
b <- a+2 

duration = faithful$eruptions
waiting = faithful$waiting

mean(a)  #arithmetic mean
mean(duration)
median(b)  #median
median(duration)
var(a)
var(duration)
sd(a)  #standard deviation
sd(duration)

# Coefficient of variation
CV <- function(mean, sd){
	(sd/mean)*100
}

max(a)
min(a)

range(duration)

quantile(duration)
quantile(duration, c(.32, .57, .98))

# Set working directory in order to save files
setwd( "C:/Projects/ReferencesAndResources/MathReferencesAndResources/60-XXProbbltyAndStochstc/tmp")
print(  paste( "Files will be read from, and saved to: ",getwd() )  )

png(file="BoxPlotExamples.png", width=450, height=450)
old.par <- par( mfrow=c(1, 2), pty="s" )

duration = faithful$eruptions
waiting = faithful$waiting
boxplot(duration, main="Old Faithful Duration")
boxplot(waiting, main="Old Faithful Waiting")

par(old.par)
dev.off()

png(file="HistogramExample.png", width=450, height=450)
old.par <- par( mfrow=c(2, 2), pty="s" )

duration = faithful$eruptions
waiting = faithful$waiting
hist(duration, main="Old Faithful Duration")
hist(waiting, main="Old Faithful Waiting")
boxplot(  sort( rnorm(10000) ), main="Normal distribution" )
hist(sort(rnorm(10000)), main="Normal distribution")

par(old.par)
dev.off()

IQR(duration)

cov(duration, waiting)
cor(duration, waiting)



# Random values
rnorm(10000)
x <- rnorm(10000) 
mean(x)  
sd(x)

