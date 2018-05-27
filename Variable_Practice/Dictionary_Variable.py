# Declaration of a dictionary varaibale
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}

print " Dispalys the contents of the originally declared dictionary variable\n\n"
print(thisdict)

print "\n\nIt can also be decrilared as :"

print "thisdict = dict(apple='green', banana='yellow', cherry='red')\n\n"


print "Changes the colour of the key value apple to red and displays the newly chnaged contents of the thisdict variable\n\n"
thisdict["apple"] = "red"
print(thisdict)

print "\n\n--- Adds an item of key damson with value purple and displays the change ---\n\n"
thisdict["damson"] = "purple"
print(thisdict)

print " \n\n---Removes the ditionary item banana and its value and displays the change ---\n\n"
del(thisdict["banana"])
print(thisdict)

print " \n\n--- Prints the length (number of items) in the dictionary varibale ---\n"
print(len(thisdict))

print " \n\n--- Prints the value of the key below ---\n"
print(thisdict['cherry'])