"""
Splay Tree Data Structure Template
Self-adjusting BST with splaying operations
"""


class SplayNode:
    """Node class for Splay Tree"""
    
    def __init__(self, value):
        """Initialize splay tree node"""
        self.value = value
        self.left = None
        self.right = None


class SplayTree:
    """Template for Splay Tree"""
    
    def __init__(self):
        """Initialize empty splay tree"""
        self.root = None
    
    def splay(self, node):
        """Perform splay operation on node"""
        pass
    
    def zig(self, node):
        """Single rotation - Zig operation"""
        pass
    
    def zig_zig(self, node):
        """Double rotation - Zig-Zig operation"""
        pass
    
    def zig_zag(self, node):
        """Mixed rotation - Zig-Zag operation"""
        pass
    
    def rotate_left(self, node):
        """Left rotation"""
        pass
    
    def rotate_right(self, node):
        """Right rotation"""
        pass
    
    def insert(self, value):
        """Insert value and splay"""
        pass
    
    def search(self, value):
        """Search for value and splay"""
        pass
    
    def delete(self, value):
        """Delete value and splay"""
        pass
    
    def find_min(self):
        """Find minimum value"""
        pass
    
    def find_max(self):
        """Find maximum value"""
        pass
    
    def join(self, other_tree):
        """Join two splay trees"""
        pass
    
    def split(self, value):
        """Split tree at value"""
        pass
    
    def inorder_traversal(self):
        """In-order traversal"""
        pass
    
    def range_search(self, low, high):
        """Search range of values"""
        pass
