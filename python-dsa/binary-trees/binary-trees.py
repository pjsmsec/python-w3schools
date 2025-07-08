# Binary Tree

# A trype of tree data structure where each node can have a maximum of two child 
# nodes.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.left.data", root.right.left.data)

# Types fo binary trees
# Balanced - has at most 1 in difference between it's left and right subtree heights,
#   for each node
# Complete - has all levels full of nodes, except the last level
# Full - where each node has either 0 or 2 child nodes
# Perfect - has all leaf nodes on the same level, meaning all levels are full of 
#   nodes, and all internal nodes have two child nodes

# Binary Tree Traversal

# Categories:
# Breadth First Search (BFS) is when the nodes on the same level are visited before
#   going to the next level in the tree.
#   This means that the tree is explores in a more sideways direction.
# Depth First Search (DFS) is when the traversal moves down the tree all the way to 
#   the leaf nodes, exploring the tree branch in a downwards direction

# There are three types of DFS traversals:
# pre-order
# in-order
# post-order

# Pre-order traversal of binary trees
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
preOrderTraversal(root)

print()

# In-order traversal of binary trees
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right) 

print()

# Post-order traversal of binary trees
def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ") 
