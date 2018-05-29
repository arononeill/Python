# Declaration of a new list
thislist = ["apple", "banana", "cherry"]
print "This is the list created\n"
print(thislist)

print "\nThis illustrates how to change a value in a list\n"
thislist[1] = "blackcurrant"
print(thislist)

print "\nThis shows how to use the append() method to append an item\n"
thislist.append("damson")
print(thislist)

# Append() And Insert() do the same thing just append puts the new element to the top of the list whereas list asks for the index for where to place the value
print "\nThis shows how to use the insert() method to append an item\n"
thislist.insert(1, "damson")
print(thislist)

print "\nThis shows how to use the remove() method to remove an item\n"
thislist.remove("apple")
print(thislist)

# The method pop() removes the top element or the element searched for according to the index, pop (index) whilst remove() removes according to the value
print "\nThe method pop() removes the value of the index searched, in this case, 0, blackcurrent\n"
thislist.pop()
print thislist

print "\nThe reverse() method returns the number of items in a list\n"
thislist.reverse()
print(thislist)

print "\nThe len() method returns the number of items in a list\n"
thislist = list(("apple", "banana", "cherry"))
print(len(thislist))