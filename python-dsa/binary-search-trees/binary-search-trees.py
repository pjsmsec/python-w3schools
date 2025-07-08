# Binary search trees

# Traversal
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)

print()

# Search for a value

# Steps
# 1 - Start at the root node.
# 2 - If this is the value we are looking for, return.
# 3 - If the value we are looking for is higher, continue searching in the right 
#     subtree.
# 4 - If the value we are looking for is lower, continue searching in the left 
#     subtree.
# 5 - If the subtree we want to search does not exist, depending on the programming 
#     language, return None, or NULL, or something similar, to indicate that the 
#     value is not inside the BST.

# Example:
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Search for a value
result = search(root, 13)
if result:
  print(f"Found the node with value: {result.data}")
else:
  print("Value not found in the BST.")

print()

# Insert a node
# Steps:
# 1 - Start at the root node.
# 2 -Compare each node:
#         Is the value lower? Go left.
#         Is the value higher? Go right.
# 3 - Continue to compare nodes with the new value until there is no right or left 
#   to compare with. That is where the new node is inserted.

# Example:
def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
  return node

# Inserting new value into the BST
insert(root, 10)

print()

# Find the lowest value

# Steps:
# 1 - Start at the root node of the subtree.
# 2 - Go left as far as possible.
# 3 - The node you end up in is the node with the lowest value in that BST subtree.

# Example:
def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

# Find Lowest
print("\nLowest value:",minValueNode(root).data) 

print()

# Delete a node

# Steps:
# 1 - If the node is a leaf node, remove it by removing the link to it.
# 2 - If the node only has one child node, connect the parent node of the node you 
#   want to remove to that child node.
 # 3 - If the node has both right and left child nodes: Find the node's in-order 
 #  successor, change values with that node, then delete it.

# Example:
def delete(node, data):
  if not node:
    return None

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    # Node with only one child or no child
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None
      return temp

    # Node with two children, get the in-order successor
    node.data = minValueNode(node.right).data
    node.right = delete(node.right, node.data)

  return node

# Delete node 15
delete(root,15)
