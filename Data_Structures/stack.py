class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


s = Stack() # Creates a new Stack called s
print(s.isEmpty()) # Checks whether stack s is empty or not, returns true
s.push(40) # Pushes element 40 onto stack
s.push('Tiocfaidh ar la') # Pushses element 'Tiocfaidh ar la' onto the stack 
print(s.peek()) # Returns the element at the top of the stack
s.push('NewElement') # Pushes element 'NewElement' onto the stack
print(s.size()) # Returns the size of the stack
print(s.isEmpty()) # Checks whether stack s is empty or not, returns true
s.push(99) # Pushes element 99 onto the stack
print(s.pop()) # Removes the top element from the stack
print(s.pop()) # Removes the top element from the stack
print(s.size()) # Returns the size of stack s