""" Program To Explain Functions In Python

Lists & Dictionaries are mutable which means you can change their content without changib their identity.

Integers, Floats, Strings & Tuples are immutable """

def funct(val):
	val += 'bar'

def funct2(val):
	val += [3, 4, 5]

print "This is to illustrate how immutable objects such as a string works: \n"
x = 'foo'
print x
funct(x)
print x

print "\nNow to illustrate how mutable objects such as a list work: "
x = [1, 2, 3]
print x
funct2(x)
print x
