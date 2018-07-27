# Merges two subarrays of arr[].
# First subarray is arr[LeftIndex..Midpoint]
# Second subarray is arr[Midpoint+1..RightIndex]
def merge(arr, LeftIndex, Midpoint, RightIndex):
    n1 = Midpoint - LeftIndex + 1
    n2 = RightIndex- Midpoint
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[LeftIndex + i]
 
    for j in range(0 , n2):
        R[j] = arr[Midpoint + 1 + j]
 
    # Merge the temp arrays back into arr[LeftIndex..RightIndex]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = LeftIndex     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# LeftIndex is for left index and RightIndex is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,LeftIndex,RightIndex):
    if LeftIndex < RightIndex:
 
        # Adds the first number's index to the last number's index in the array and then halves it
        Midpoint = (LeftIndex+(RightIndex-1))/2
 
        # Sort first and second halves
        mergeSort(arr, LeftIndex, Midpoint)
        mergeSort(arr, Midpoint+1, RightIndex)
        merge(arr, LeftIndex, Midpoint, RightIndex)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
ArrLength = len(arr)
print ("Given array is")
for i in range(ArrLength):
    print ("%d" %arr[i]), 
 
mergeSort(arr,0,ArrLength-1)
print ("\n\nSorted array is")
for i in range(ArrLength):
    print ("%d" %arr[i]),