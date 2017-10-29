# python 2.7
# This code explores the likelihood of repeated results when rolling three fair sixe-sidded dice four times

rolls = {}

for x in range(3,19):
	rolls[x]=0

for i in range(1,7):
	for j in range(1,7):
		for k in range(1,7):
			result = i+j+k
			rolls[result]=rolls[result]+1

print "Probabilities of rolling result of three d6:"
for x in rolls:
	print "{}: {}/216".format(x,rolls[x])
print ""

sumOfRolls = 0

for x in rolls:
	sumOfRolls = sumOfRolls + rolls[x]


print "Sum of all the rolls is {}".format(sumOfRolls)
print ""


print "Now we calculate the different number of outcomes when three d6 are rolled four times."
print ""

#E keeps track of all the wasy we get repeated results
E = 0


#number of ways all for rolls are the same
A = 0
for i in rolls:
	result = rolls[i]*rolls[i]*rolls[i]*rolls[i]
	A = A + result
print "A: All four results are the same"
print "A: {}".format(A)
print ""

#number of ways three of the results are the same
#i is repeated and j is the singleton
B = 0
for i in rolls:
	for j in rolls:
		if(i!=j):
			# note that for any instance of i and j there are 4 ways it can happen
			result = rolls[i]*rolls[i]*rolls[i]*rolls[j]*4
			B = B + result
print "B: A result is repeated exaclty three times."
print "B: {}".format(B)
print ""

#number of ways for two results are the same
#i is the repeated and j/k are the singletons
#note that for any instance of i/j/k there are 12 ways they can be arranged
#but because how we are iterating j and k we will cut 12 in half to 6
C = 0
for i in rolls:
	for j in rolls:
		for k in rolls:
			if((i!=j)&(i!=k)&(j!=k)):
				result = rolls[i]*rolls[i]*rolls[j]*rolls[k]*6
				C = C + result
print "C: A result is repeated exaclty two times"
print "C: {}".format(C)
print ""

#number of ways two repeated results
#i and j are both repeatd result
D = 0
for i in rolls:
	for j in rolls:
		if(i!=j):
			result = rolls[i]*rolls[i]*rolls[j]*rolls[j]*3
			D = D + result
print "D Two results are repeated once each"
print "D: {}".format(D)
print ""

#number of was we do not get repeated results
Fnot = 0
for i in rolls:
	for j in rolls:
		for k in rolls:
			for l in rolls:
				if((i!=j)&(i!=k)&(i!=l)&(j!=k)&(j!=l)&(k!=l)):
					result = rolls[i]*rolls[j]*rolls[k]*rolls[l]
					Fnot = Fnot +result

F = A+B+C+D
print "F: one or more results are repeated any number of times"
print "F: {}".format(F)
print "F': {}".format(Fnot)
print ""

print "Sample size is {}".format((6**3)**4)
print "F + F' = {}".format(F+Fnot)
print ""

print "P(F) = {0:.5f}".format(float(F)/float((216**4)))
