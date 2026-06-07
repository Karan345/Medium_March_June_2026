"""
Binary Search Tree (BST) Data Structure Template
"""


class TreeNode:
    """Node class for Binary Search Tree"""
    
    def __init__(self, value):
        """Initialize a tree node"""
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Template for Binary Search Tree"""
    
    def __init__(self):
        """Initialize empty BST"""
        self.root = None
    
    def insert(self, value):
        """Insert a value into BST"""
        pass
    
    def search(self, value):
        """Search for a value in BST"""
        pass
    
    def delete(self, value):
        """Delete a value from BST"""
        pass
    
    def inorder_traversal(self):
        """In-order traversal (Left-Root-Right)"""
        pass
    
    def preorder_traversal(self):
        """Pre-order traversal (Root-Left-Right)"""
        pass
    
    def postorder_traversal(self):
        """Post-order traversal (Left-Right-Root)"""
        pass
    
    def level_order_traversal(self):
        """Level-order (Breadth-first) traversal"""
        pass
    
    def find_min(self):
        """Find minimum value"""
        pass
    
    def find_max(self):
        """Find maximum value"""
        pass
    
    def height(self):
        """Get height of tree"""
        pass
    
    def is_balanced(self):
        """Check if tree is balanced"""
        pass
    
    def is_bst(self):
        """Verify if tree is a valid BST"""
        pass
    
    def find_kth_smallest(self, k):
        """Find kth smallest element"""
        pass
    
    def find_kth_largest(self, k):
        """Find kth largest element"""
        pass
    
    def lowest_common_ancestor(self, node1, node2):
        """Find LCA of two nodes"""
        pass
    
    def is_ancestor(self, ancestor, node):
        """Check if node is ancestor"""
        pass


class AVL_Node:
    """Node for AVL Tree (included here for reference)"""
    
    def __init__(self, value):
        """Initialize AVL node"""
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
