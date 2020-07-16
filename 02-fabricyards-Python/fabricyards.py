# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	# your code goes here
	if(inches>36 and inches <=72):
    		return 2
	if(inches<=36 and inches>0):
    		return 1
	if (inches>72 and inches <=108):
    		return 3
	return 0

def fun_fabricexcess(inches):
	# your code goes here
	if(inches<=36 and inches>0):
    		return 36-inches
	if(inches>36 and inches <=72):
			return 72-inches;
	if (inches>72 and inches <=108):
    		return 108-inches
	return 0

