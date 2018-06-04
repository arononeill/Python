class Node:
    # Tree node: left and right child + data which can be any object

    # This creates a new class named Node with 3 attributes, left node, right node and node's data
    def __init__(self, data):

        # Node constructor
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        """ Insert new node with data
        @param data node data object to insert """

        if self.data:

            if data < self.data: # Checks whether the node to insert is less than the root node

                if self.left is None: # When the left child is none 
                    self.left = Node(data) # We attach the value to insert into it

                else: # If there is a left sub node then this else statement is called
                    self.left.insert(data) # The insert() method is called again, now with the subtree's value, along with the same value for data

            elif data > self.data:

                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def lookup(self, data, parent=None):

        """ Lookup node containing data
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None """

        if data < self.data: # Checks whether the value given to lookup is less than the root's data

            if self.left is None:
                return None, None # Value not found, none returned

            return self.left.lookup(data, self) # root's left child's lookup() method is called using the same data whilst making the parent value equal to the current node

        elif data > self.data: # If the value searched is greater than the node's value

            if self.right is None:
                return None, None # Value not found, none returned

            return self.right.lookup(data, self) # root's right child's lookup() method is called using the same data whilst making the parent value equal to the current node

        else: # When the node's data is equal to the value searched 
            return self, parent # We return that value as well as it's parent's node value

    def delete(self, data):

        """ Delete node containing data
        @param data node's content to delete """

        # get node containing data
        node, parent = self.lookup(data)

        if node is not None:
            children_count = node.children_count() # Gets the number of children and returns it, assigning it to children_count

        if children_count == 0: 
            # if node has no children, just remove it
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None

        elif children_count == 1:
            # if node has 1 child
            # replace node with its child

            if node.left: 
                n = node.left # If the node has a left child, it is assigned to n
            else:
                n = node.right # If the node has a right child, it is assigned to n

            if parent: 
                if parent.left is node: # If the left child of the parent is the value of the searched for node
                    parent.left = n # The left child of the parent is assigned the value of n, which is the value of the child, of the parent's child
                                    # This swpas the parent's child and child's child

                else: # If the right child of the parent is the value of the searched for node
                    parent.right = n # The right child of the parent is assigned the value of n, which is the value of the child, of the parent's child
                                     # This swpas the parent's child and child's child
                del node

            else: # This handles the case where the node is the root of the tree
                self.left = n.left
                self.right = n.right
                self.data = n.data

        else:
            # if node has 2 children
            # find its successor
            parent = node # Node searched to be deleted is assigned to parent
            successor = node.right # Successor is given the value of the right child of the node to be deleted 

            while successor.left: # While successor has a left child
                parent = successor # parent is given the value of the successor which after the next line means it is successor's parent node
                successor = successor.left # By doing this successor is given the value of the most bottom left node

            # replace node data (the value to be deleted) by its successor data
            node.data = successor.data

            # fix successor's parent's child
            if parent.left == successor: # If the successor was the value of the parent's left child node
                parent.left = successor.right # assigns parent's left child node, the value of successor's right (parent's right) in other words, swpas the two children nodes
            else:
                parent.right = successor.right

    def print_tree(self):
    
        # Print tree content in order

        if self.left:
            self.left.print_tree()

        print self.data,

        if self.right:

            self.right.print_tree()

    def compare_trees(self, node):

        """ Compare 2 trees
        @param node tree's root node to compare to
        @returns True if the tree passed is identical to this tree """

        if node is None:
            return False

        if self.data != node.data:
            return False
        res = True

        if self.left is None:

            if node.left:
                return False

        else:
            res = self.left.compare_trees(node.left)

        if res is False:
            return False

        if self.right is None:

            if node.right:
                return False

        else:
            res = self.right.compare_trees(node.right)

        return res

    def tree_data(self):

        # Generator to get the tree nodes data
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:

            if node:
                stack.append(node)
                node = node.left

            else: # we are returning so we pop the node and we yield it

                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        
        """ Returns the number of children
        @returns number of children: 0, 1, 2 """

        cnt = 0
        if self.left:
            cnt += 1

        if self.right:
            cnt += 1

        return cnt

root = Node(8) # This creates a tree with a single node, 8
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
root.print_tree()
root.delete(3)
print "\n"
node, parent = root.lookup(20)
root.print_tree()

root2 = Node(8)
root2.insert(3)
root2.insert(11)
Compare_check = root.compare_trees(root2)
print Compare_check

root3 = Node(8)
root3.insert(3)
root3.insert(11)
Compare_check = root2.compare_trees(root3)
print Compare_check



