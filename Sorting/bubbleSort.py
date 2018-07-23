def bubbleSort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]: # This checks which element is lowest and swaps them according using a tempory variable
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [40,21,53,67,7,81,66,59,22]
print 'This program demonstrates a simple bubble sort algorithm\n'
print "This is the list previous to the bubble sort", list
bubbleSort(list)
print "\nThis is the list post bubble sort", list