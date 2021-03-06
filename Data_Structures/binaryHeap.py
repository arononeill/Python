# A Python program to demonstrate common binary heap operations
 
# Import the heap functions from python library
from heapq import heappush, heappop, heapify 
 
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time
 
# A class definition for MinHeap
class MinHeap:
     
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
 
    def parent(self, i):
        return (i-1)/2
     
    # Inserts a new key 'Newkey'
    def insertKey(self, Newkey):
        heappush(self.heap, Newkey) # This calls the imported heap function heappush which in turns pushes the passed element 'NewKey' into the heap          
 
    # Decrease value of key at index 'DeleteIndex' to new_val
    # It is assumed that new_val is smaller than heap[DeleteIndex]
    def decreaseKey(self, DeleteIndex, new_val):
        self.heap[DeleteIndex]  = new_val 
        while(DeleteIndex != 0 and self.heap[self.parent(DeleteIndex)] > self.heap[DeleteIndex]):
            # Swap heap[DeleteIndex] with heap[parent(DeleteIndex)]
            self.heap[DeleteIndex] , self.heap[self.parent(DeleteIndex)] = (
            self.heap[self.parent(DeleteIndex)], self.heap[DeleteIndex])
             
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
 
    # This functon deletes key at index DeleteIndex. It first reduces value to minus infinite and then calls extractMin()
    def deleteKey(self, DeleteIndex):
        self.decreaseKey(DeleteIndex, float("-inf"))
        self.extractMin()
 
    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]
 
# Driver program to test above functions
heapObj = MinHeap()
heapObj.insertKey(3) 
heapObj.insertKey(2)
heapObj.deleteKey(1) # Deletes the value at index 1
heapObj.insertKey(15) 
heapObj.insertKey(5)
heapObj.insertKey(4) 
heapObj.insertKey(45)

print heapObj.extractMin() # Returns the minimum value of the heap and removes it
print heapObj.getMin() # Retrieves the minimum value from the heap
heapObj.decreaseKey(2, 1) # Changes the value at index 2 to a value of 1
print heapObj.getMin() # Retrieves the minimum value from the heap