def selectionSort(list):
   for fillslot in range(length-1,0,-1):
       GreatestPosition = 0
       for location in range(1,fillslot+1):
           if list[location]>list[GreatestPosition]:
               GreatestPosition = location

       temp = list[fillslot]
       list[fillslot] = list[GreatestPosition]
       list[GreatestPosition] = temp

list = [54,26,93,17,77,31,44,55,20]
length = len(list)    
selectionSort(list)
print(list) 