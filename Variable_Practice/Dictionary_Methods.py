import operator

# Decalring a Dictionary Variable
dictExample = {
	"student0" : "Bob",
	"student1" : "Lewis",
	"student2" : "Paddy",
	"student3" : "Steve",
	"student4" : "Pete"
}

print "\n\nDictionary method get() Returns the value of the searched key\n"
find = dictExample.get("student0")
print find


print "\n\nDictionary method items() returns view of dictionary's (key, value) pair\n"
view = dictExample.items()
print "\n", view


print "\n\nDictionary method keys() Returns View Object of All Keys\n"
keys = dictExample.keys()
print "\n", keys

print "\n\nDictionary method popitem() Returns the dictionary contents\nminus the top key and value as they have been popped off the stack\n"
dictExample.popitem()
print dictExample

print "\n\nDictionary method pop() removes and returns element having given key, student4\n\n"
dictExample.pop("student4")
print dictExample

print "\n\nDictionary method max() returns largest key\n"
print "max is ", max(dictExample)

print "\nDictionary method min() returns smallest key\n"
print "min is ", min(dictExample)

print "\nDictionary method sorted() returns sorted keys in ascending order\n"
print (sorted(dictExample))

print "\nDictionary method sorted() returns sorted keys in descending order\n"
print (sorted(dictExample, reverse=True))