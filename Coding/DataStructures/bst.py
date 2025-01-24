# Tree Implementation
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, node):
        if self.root == None:
            self.root = node
            return
        self._insert(self.root, node)
    
    def _insert(self, node, new):
        if new.val < node.val:
            # Go to the left subtree
            if node.left == None:
                node.left = new
            else:
                self._insert(node.left, new)
        elif new.val > node.val:
            # Go to the right subtree
            if node.right == None:
                node.right = new
            else:
                self._insert(node.right, new)
        
    # Specifically in-order traversal
    def DepthFirstSearch(self, node):
        if node == None:
            return

        self.DepthFirstSearch(node.left)
        print(f"({node.val})", end=" ")
        self.DepthFirstSearch(node.right)


    def BreadthFirstSearch(self):
        if self.root == None:
            return
        
        q = deque([self.root])
        while q:
            curr = q.popleft() # get the front node
            print(f"({curr.val})", end=" ")

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)


tree = Tree()
tree.add(Node(1))
tree.add(Node(2))
tree.add(Node(-1))
tree.add(Node(0))
tree.DepthFirstSearch(tree.root)
print()
tree.BreadthFirstSearch()
