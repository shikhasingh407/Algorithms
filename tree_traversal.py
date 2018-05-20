# Implementing In-order, post order and pre order traversal of a tree

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if root == None:
        return
    preorder(root.left)
    print(root.val)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.val)

def preorder(root):
    if root == None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("pre order traversal:")
preorder(root)

print("post order traversal:")
postorder(root)

print("In order traversal:")
inorder(root)

