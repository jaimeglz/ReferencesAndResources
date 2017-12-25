# P62J05RegressionCurveFitting
# 
# 
###############################################################################

# From Chi yau c07-s08
# png(file="numerical-data8x.png", width=450, height=450)
duration = faithful$eruptions    # eruption durations
waiting = faithful$waiting       # waiting interval
plot(duration, waiting,          # plot the variables
		xlab="Eruption duration",      # x-axis label
		ylab="Time waited")    
abline(lm(waiting ~ duration))
# dev.off()

