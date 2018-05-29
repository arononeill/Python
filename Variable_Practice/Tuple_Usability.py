# Create a Tuple Variable
thistuple = ("apple", "banana", "cherry")

print " Displaying it \n"
print(thistuple)

print "\n Print an item from a certain position in the tuple\n"
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print "\nThe len() method returns the number of items in a tuple\n\nThe number of items in this tuple are: "
print(len(thistuple))

print "\nUsing the tuple() method to make a tuple\n\nIt's contents are :"
thistuple2 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple2)

print "\n Attempt at changing variable located at position 1, but you cannot change values in a tuple as they are immutable\n"
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # test changeability
print(thistuple)