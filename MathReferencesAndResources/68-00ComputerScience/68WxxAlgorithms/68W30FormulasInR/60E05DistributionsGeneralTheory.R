# 60E05DistributionsGeneralTheory
# 
# Taken main from Chi Yau and KIExploRx
###############################################################################

duration = faithful$eruptions
waiting = faithful$waiting

# Binomial, Poisson, Continuous, Exponential, Normal, Chi-Squared, Student, F distributions 
# http://www.r-tutor.com/elementary-statistics/probability-distributions/binomial-distribution
# ...
# See rtutor-pt2-c09 in Chi Yau tutorial

# Variance and sd for binomial distribution
var_Binom <- function(p){
	p*(1-p)
}

sd_Binom <- function(p){
	sqrt( p*(1-p) )
}

# Frequency distribution1
range(duration)
breaks = seq(1.5, 5.5, by=0.5) 
duration.cut = cut(duration, breaks, right=FALSE)
duration.freq = table(duration.cut)
cbind(duration.freq)

# Histogram With colors
colors = c("red", "yellow", "green", "violet", "orange", "blue", "pink", "cyan") 
hist(duration, right=FALSE, 
		col=colors, 
		main="Old Faithful Eruptions",
		xlab="Duration minutes")


# Histogram (with cut)
duration = faithful$eruptions
breaks = seq(1.5, 5.5, by=0.5) 
h = hist(duration, breaks=breaks, 
		right=FALSE, plot=TRUE)
duration.freq = h$counts

# Cumulative frequency distribution
duration.cumfreq = cumsum(duration.freq)
cbind(duration.cumfreq)
# Cumulative feq graph
cumfreq0 = c(0, cumsum(duration.freq))
plot(breaks, cumfreq0,
		main="Old Faithful Eruptions",
		xlab="Duration minutes",
		ylab="Cumulative eruptions")
lines(breaks, cumfreq0)

# Central moment
# http://www.r-tutor.com/elementary-statistics/numerical-measures/moment 

library(e1071)
moment(duration, order=0, center=TRUE)
moment(waiting, order=0, center=TRUE)
moment(rnorm(10000), order=0, center=TRUE)

moment(duration, order=1, center=TRUE)
moment(waiting, order=1, center=TRUE)
moment(rnorm(10000), order=1, center=TRUE)

# The second central moment μ2 is called the variance, and is usually denoted σ2
#	where σ represents the standard deviation.
moment(duration, order=2, center=TRUE)
moment(waiting, order=2, center=TRUE)
moment(rnorm(1000000), order=2, center=TRUE)

# The third and fourth central moments are used to define skewness and kurtosis
moment(duration, order=3, center=TRUE)
moment(waiting, order=3, center=TRUE)
moment(rnorm(10000), order=3, center=TRUE)

moment(duration, order=4, center=TRUE)
moment(waiting, order=4, center=TRUE)
moment(rnorm(10000), order=4, center=TRUE)

# Skewness
# http://www.r-tutor.com/elementary-statistics/numerical-measures/skewness
skewness(duration) 
skewness(waiting)
skewness(rnorm(10000))

# KUrtosis
# http://www.r-tutor.com/elementary-statistics/numerical-measures/kurtosis
kurtosis(duration) 
kurtosis(waiting)
kurtosis(rnorm(10000))

# Z table
zheader <- seq(0,0.09,0.01)
zrows <- seq(0, 0.9, 0.1)
for (j in 0:9)
{
	print( paste("col=",j) )
	for (i in 0:9)
	{ 
		z[i+1] <- round( pnorm(i/10,0,1) , digits=4 )
		print(z[i])
	}
	zrows <- data.frame(zrows,z)
}
zrows.colnames <- zheader


