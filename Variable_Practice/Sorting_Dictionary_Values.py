import operator
dict = {
	1: 2,
	3: 4,
	4: 3,
	2: 1,
	0: 0
}

print 'Original dictionary : ',dict

# Sorts the dictionary values in ascending order according to key size & Displays both keys and values
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print("\n")
print('Dictionary in ascending order by value : ',sorted_dict)

print "\n\n --- Sorts the dictionary values in ascending order according to key size ---\n"
print(sorted(dict))

print "\n\n --- Sorts the dictionary values in descending order according to key size & Displays both keys and values ---\n\n"
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_dict)