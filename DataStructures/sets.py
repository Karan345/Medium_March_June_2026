"""
Set Data Structure Template
Unordered collection of unique elements
"""


class HashSet:
    """Template for HashSet implementation"""
    
    def __init__(self, capacity=16):
        """Initialize hashset"""
        self.capacity = capacity
        self.set = [[] for _ in range(capacity)]
        self.size = 0
    
    def hash(self, element):
        """Hash function for computing bucket index"""
        pass
    
    def add(self, element):
        """Add element to set"""
        pass
    
    def remove(self, element):
        """Remove element from set"""
        pass
    
    def contains(self, element):
        """Check if element exists in set"""
        pass
    
    def is_empty(self):
        """Check if set is empty"""
        pass
    
    def size_of(self):
        """Get number of elements"""
        pass
    
    def clear(self):
        """Clear all elements"""
        pass
    
    def to_list(self):
        """Convert set to list"""
        pass
    
    def display(self):
        """Display all elements"""
        pass


class TreeSet:
    """Template for TreeSet (Sorted Set using BST)"""
    
    def __init__(self):
        """Initialize tree set"""
        self.root = None
        self.size = 0
    
    def add(self, element):
        """Add element to sorted set"""
        pass
    
    def remove(self, element):
        """Remove element from set"""
        pass
    
    def contains(self, element):
        """Check if element exists"""
        pass
    
    def first(self):
        """Get smallest element"""
        pass
    
    def last(self):
        """Get largest element"""
        pass
    
    def display_sorted(self):
        """Display elements in sorted order"""
        pass


class SetOperations:
    """Template for Set operations"""
    
    @staticmethod
    def union(set1, set2):
        """Return union of two sets"""
        pass
    
    @staticmethod
    def intersection(set1, set2):
        """Return intersection of two sets"""
        pass
    
    @staticmethod
    def difference(set1, set2):
        """Return difference of two sets"""
        pass
    
    @staticmethod
    def symmetric_difference(set1, set2):
        """Return symmetric difference"""
        pass
    
    @staticmethod
    def is_subset(set1, set2):
        """Check if set1 is subset of set2"""
        pass
    
    @staticmethod
    def is_superset(set1, set2):
        """Check if set1 is superset of set2"""
        pass
