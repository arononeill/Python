# Merges two subarrays of arr[].
# First subarray is arr[LeftIndex..Midpoint]
# Second subarray is arr[Midpoint+1..RightIndex]
def merge(arr, LeftIndex, Midpoint, RightIndex):
    LeftArraySize = Midpoint - LeftIndex + 1
    RightArraySize = RightIndex- Midpoint
 
    # create temp arrays of sizes LeftArraySize and RightArraySize
    LeftArray = [0] * (LeftArraySize)
    RightArray = [0] * (RightArraySize)
 
    # Copy data to temp arrays LeftArray[] and RightArray[]
    for LeftArrayIndex in range(0 , LeftArraySize):
        LeftArray[LeftArrayIndex] = arr[LeftIndex + LeftArrayIndex]
 
    for RightArrayIndex in range(0 , RightArraySize):
        RightArray[RightArrayIndex] = arr[Midpoint + 1 + RightArrayIndex]
 
    # Merge the temp arrays back into arr[LeftIndex..RightIndex]
    LeftArrayIndex = 0     # Initial index of first subarray
    RightArrayIndex = 0     # Initial index of second subarray
    MergedArrIndex = LeftIndex     # Initial index of merged subarray
 
    while LeftArrayIndex < LeftArraySize and RightArrayIndex < RightArraySize : # Checks to clarify if all indexes have been visited or not
        if LeftArray[LeftArrayIndex] <= RightArray[RightArrayIndex]: # this checks which number is smaller between the LeftArray number and RightArray number
            arr[MergedArrIndex] = LeftArray[LeftArrayIndex] # The number checked in the LeftArray is then added to the array, controlled by the MergedArrIndex
            LeftArrayIndex += 1 # LeftArray's Index is the incremented by 1 to the check the next number

        else: # If the number in the RightArray is smaller then 
            arr[MergedArrIndex] = RightArray[RightArrayIndex] #  # The number checked in the RightArray is then added to the array, controlled by the MergedArrIndex
            RightArrayIndex += 1 # RightArray's Index is the incremented by 1 to the check the next number
        MergedArrIndex += 1 # After the number is added to the arr from either left or right array, the MergedArrIndex is incremented by 1 in order to move to the next place
 
    # Copy the remaining elements of LeftArray[], if there are any
    while LeftArrayIndex < LeftArraySize:
        arr[MergedArrIndex] = LeftArray[LeftArrayIndex]
        LeftArrayIndex += 1
        MergedArrIndex += 1
 
    # Copy the remaining elements of RightArray[], if there are any
    while RightArrayIndex < RightArraySize:
        arr[MergedArrIndex] = RightArray[RightArrayIndex]
        RightArrayIndex += 1
        MergedArrIndex += 1 
 
# LeftIndex is for left index and RightIndex is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,LeftIndex,RightIndex):
    if LeftIndex < RightIndex:
 
        # Adds the first number's index to the last number's index in the array and then halves it
        Midpoint = (LeftIndex+(RightIndex-1))/2
 
        # Sort first and second halves
        mergeSort(arr, LeftIndex, Midpoint) # This calls the first half of the array and splits it up in order to be sorted
        mergeSort(arr, Midpoint+1, RightIndex) # This calls the second half of the array and splits it up in order to be sorted

        merge(arr, LeftIndex, Midpoint, RightIndex)


# Driver code to test above
arr = [12, 11, 13, 50, 5, 25]
ArrLength = len(arr)
print ("Given array is")
for LeftArrayIndex in range(ArrLength):
    print ("%d" %arr[LeftArrayIndex]), 
 
mergeSort(arr,0,ArrLength-1)
print ("\n\nSorted array is")
for LeftArrayIndex in range(ArrLength):
    print ("%d" %arr[LeftArrayIndex]),