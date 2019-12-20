import sys
import random
sys.path.append('../queue_and_stack')



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a tree/root
        # value < self.value go left, make a new tree/node if empty, otherwise keep going
         # value > self.value go right, make a new tree/node if empty, otherwise keep going
        if value == self.value:
            return None
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            elif self.left is not None:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            elif self.right is not None:
                self.right.insert(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target = self.value return
        # else go left/right based on smaller or bigger
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right, else return self.value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Recursively
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        return

        # iteratively
        # stack = Stack()
        # stack.push(self)

        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)



