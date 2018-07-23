# Stack implementation from using a LinkedList Class
from LinkedList import LinkedList.Node

class Stack (object)
	def __init__(self, top=None):
			seelf.ll = LinkedList(top)

	def push(self, new_element):
			"Push (add) a new element onto the top of the stack"
			return self.ll.insert_first(new_element)

	def pop(self)
		"Remove the element at the top"