"""
Hash Table Data Structure Template
Hash Functions, Collision Handling, and Operations
"""


class HashTable:
    """Template for Hash Table with separate chaining"""
    
    def __init__(self, size=100):
        """Initialize hash table with given size"""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        """Hash function to compute index"""
        pass
    
    def insert(self, key, value):
        """Insert key-value pair"""
        pass
    
    def search(self, key):
        """Search for a key"""
        pass
    
    def delete(self, key):
        """Delete a key-value pair"""
        pass
    
    def display(self):
        """Display all key-value pairs"""
        pass
    
    def get(self, key):
        """Get value for given key"""
        pass


class OpenAddressingHashTable:
    """Template for Hash Table with Open Addressing (Linear Probing)"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function(self, key):
        """Hash function"""
        pass
    
    def linear_probe(self, index):
        """Linear probing for collision resolution"""
        pass
    
    def insert(self, key, value):
        """Insert key-value pair"""
        pass
    
    def search(self, key):
        """Search for a key"""
        pass
    
    def delete(self, key):
        """Delete a key-value pair"""
        pass
    
    def display(self):
        """Display all key-value pairs"""
        pass


class QuadraticProbingHashTable:
    """Template for Hash Table with Quadratic Probing"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function(self, key):
        """Hash function"""
        pass
    
    def insert(self, key, value):
        """Insert key-value pair"""
        pass
    
    def search(self, key):
        """Search for a key"""
        pass
    
    def delete(self, key):
        """Delete a key-value pair"""
        pass


class DoubleHashingHashTable:
    """Template for Hash Table with Double Hashing"""
    
    def __init__(self, size=100):
        """Initialize hash table"""
        self.size = size
        self.table = [None] * size
        self.occupied = [False] * size
    
    def hash_function1(self, key):
        """Primary hash function"""
        pass
    
    def hash_function2(self, key):
        """Secondary hash function"""
        pass
    
    def insert(self, key, value):
        """Insert key-value pair"""
        pass
    
    def search(self, key):
        """Search for a key"""
        pass
    
    def delete(self, key):
        """Delete a key-value pair"""
        pass
