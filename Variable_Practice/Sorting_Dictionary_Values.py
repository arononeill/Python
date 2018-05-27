import operator
dict = {
	1: 2,
	3: 4,
	4: 3,
	2: 1,
	0: 0
}

print('Original dictionary : ',d)

# Sorts the dictionary values in ascending order according to key size
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_dict)

# Sorts the dictionary values in descending order according to key size
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_dict)