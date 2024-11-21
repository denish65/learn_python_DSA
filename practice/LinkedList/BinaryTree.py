# A Python class that represents
# an individual node in a Binary Tree
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d


# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode        





 


