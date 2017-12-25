# 62F03tPower
# Source: University of California, Berkeley. 
# Originally from Phil Spector, Dept. of Statistics, Statistics 133
# http://statistics.berkeley.edu/computing/r-t-tests
###############################################################################
# Power of the t-test

t.power = function(nsamp=c(10,10),nsim=1000,means=c(0,0),sds=c(1,1)){
	lower = qt(.025,df=sum(nsamp) - 2)
	upper = qt(.975,df=sum(nsamp) - 2)
	ts = replicate(nsim,
			t.test(rnorm(nsamp[1],mean=means[1],sd=sds[1]),
					rnorm(nsamp[2],mean=means[2],sd=sds[2]))$statistic)
	
	sum(ts < lower | ts > upper) / nsim
}
