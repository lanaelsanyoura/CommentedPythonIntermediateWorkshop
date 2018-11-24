class BSTree():
    """
    A Binary search tree such with a root TreeNode such that the value
    of the TreeNode is greater than or equal to all the values in its
    left subtree, and less than or equal to the values in the right subtree
                 ____(8)____
                |           |
             __(4)      __(10)__
            |          |        |
           (1)        (9)     (11)

    ==== Attributes ====

    root: TreeNode, default is None
    size: number of nodes in our tree

    """
    def __init__(self, root = None):
        # self.root = root
        # self.size = 1 if self.root else 0
        pass

    def addNode(self, node):
        """
        Add a node to our tree while keeping the BST ordering
        @param node:
        @return:
        """
        # If self is a leaf'
        # self.root =self.add_helper(self.root, node)
        pass

    def add_helper(self, currNode, nodeToAdd):
        """
        Add the nodeToAdd to this currNode's children
        @param currNode: Could be None, node we're on
        @param nodeToAdd: Node to ad
        @return: the modified currNode after adding nodeToAdd
        """
        # self.size += 1
        # if currNode is None:
        #     return nodeToAdd
        # else:
        #     if currNode.value <= nodeToAdd.value:
        #         currNode.right = self.add_helper(currNode.right, nodeToAdd)
        #     else:
        #         currNode.left = self.add_helper(currNode.left, nodeToAdd)
        #     return currNode
        pass


    def __str__(self):
        """
        Read left subtree, read root, read right subtree
        Prints the values in ascending order
        :return:
        """
        #return self.str_helper(self.root)
        pass

    def str_helper(self, currNode):
        """
        Print the values in the tree through in-order
        :param currNode: The node we are currently on
        :return: The string representing this node
        """
        # if currNode is not None:
        #     return "{} {} {} ".format(self.str_helper(currNode.left),
        #                               currNode.value,
        #                               self.str_helper(currNode.right))
        # else:
        #     return ""
        pass

    def __contains__(self, value):
        """
        Check if value is in this Tree
        @param value: int value of node we're looking for
        @return: True if value in self, else False
        """
        # return self.contains_helper(value, self.root)
        pass

    def contains_helper(self, value, currNode):
        """
        Helper function that checks if value is in a currNode or its subtrees
        @param value: int
        @param currNode: TreeNode
        @return: True if value in currNode, else False
        """
        # Check to see if this BST contains the given value
        # if currNode is None:
        #     return False
        # else:
        #     inLeft = False
        #     inRight = False
        #     if value < currNode.value:
        #         # Search in the left tree
        #         inLeft = self.contains_helper(value, currNode.left)
        #     if currNode.value < value:
        #         inRight = self.contains_helper(value, currNode.right)
        #     return value == currNode.value or inLeft or inRight
       pass

    def get_max_value(self):
        """
        Return the max value in our tree
        @return: int
        """
        #return self.get_max_helper(self.root)
        pass

    def get_max_helper(self, currNode):
        """
        Return the max value in currNode
        @param currNode: TreeNode
        @return: int
        """
        # if currNode.isLeaf():
        #     return currNode.value
        # else:
        #     return max(self.get_max_helper(currNode.right), currNode.value)
        pass


class TreeNode:
    """
    A Node in a BST
    @param Node left: greater value
    @param Node right: lesser value

    # NOTES: A leaf has None as children
    """
    def __init__(self, value, left=None, right=None):
        # self.value = value
        # self.left = left
        # self.right = right
        pass

    def isLeaf(self):
        """
        Return True if this node has no children (both children are None)
        @return:
        """
        return not (self.left and self.right)