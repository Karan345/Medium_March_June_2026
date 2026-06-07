"""
AVL Tree Data Structure Template
Self-balancing Binary Search Tree
"""


class AVLNode:
    """Node class for AVL Tree"""
    
    def __init__(self, value):
        """Initialize AVL tree node"""
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """Template for AVL Tree"""
    
    def __init__(self):
        """Initialize empty AVL tree"""
        self.root = None
    
    def get_height(self, node):
        """Get height of node"""
        pass
    
    def get_balance_factor(self, node):
        """Get balance factor of node"""
        pass
    
    def rotate_left(self, node):
        """Left rotation for rebalancing"""
        pass
    
    def rotate_right(self, node):
        """Right rotation for rebalancing"""
        pass
    
    def rotate_left_right(self, node):
        """Left-Right rotation"""
        pass
    
    def rotate_right_left(self, node):
        """Right-Left rotation"""
        pass
    
    def insert(self, value):
        """Insert value with self-balancing"""
        pass
    
    def delete(self, value):
        """Delete value with self-balancing"""
        pass
    
    def search(self, value):
        """Search for value"""
        pass
    
    def inorder_traversal(self):
        """In-order traversal"""
        pass
    
    def preorder_traversal(self):
        """Pre-order traversal"""
        pass
    
    def postorder_traversal(self):
        """Post-order traversal"""
        pass
    
    def is_balanced(self):
        """Check if tree is balanced"""
        pass
    
    def height(self):
        """Get tree height"""
        pass
    
    def find_min(self):
        """Find minimum value"""
        pass
    
    def find_max(self):
        """Find maximum value"""
        pass
