"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. check if there is no root
        if self is None:
            # if there isn't, create the node and park it there
            self = BSTNode(value)
        # 2. otherwise, there is a root
        else:
            # compare teh value to the root's value to determine which direction we go in
            # if the value < roots value
            if value < self.value:
                # go left
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            # if the value > roots value
            else:
                # go right
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree

    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.contains(6)
