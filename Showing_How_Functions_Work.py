#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
	"This changes a passed list into this function"
	mylist.append(1); # Here we are maintainig the refernece, mylist, of the passed oject 
	print "Values inside the function: ", mylist
	return

def changeme2( mylist ):
	"This changes a passed list into this function"
	mylist = [1,2,3,4]; # The reference, mylist, is being overwritten inside the function
	print "Values inside the function: ", mylist	
	return
 
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total	

# Now you can call changeme function
mylist = [10,20,30];
print "This is to illustrate maintaining the reference inside the function\n"
changeme( mylist );
print "Values outside the function: ", mylist

mylist = [10,20,30];
print "\nThis is to illustrate overwritting the reference inside the function\n"
changeme2( mylist );
print "Values outside the function: ", mylist

print "\nThis is to demonstrate local vs gloabl variables\n"
total = 0; # This is global variable.
# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 

print "\nHere is an example of how to correctly use Pass by Value: \n"
# Now you can call sum function
total = sum( 10, 20 ); # The correct way of returning a variable using pass by value
print "Outside the function global total : ", total 