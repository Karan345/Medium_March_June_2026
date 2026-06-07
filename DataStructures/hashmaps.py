"""
HashMap Data Structure Template
Using Hash Table with Key-Value pairs
"""


class HashMap:
    """Template for HashMap implementation"""
    
    def __init__(self, capacity=16, load_factor=0.75):
        """Initialize hashmap with capacity and load factor"""
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def hash(self, key):
        """Hash function for computing bucket index"""
        pass
    
    def put(self, key, value):
        """Insert or update key-value pair"""
        pass
    
    def get(self, key):
        """Get value for given key"""
        pass
    
    def remove(self, key):
        """Remove key-value pair"""
        pass
    
    def contains_key(self, key):
        """Check if key exists"""
        pass
    
    def contains_value(self, value):
        """Check if value exists"""
        pass
    
    def is_empty(self):
        """Check if hashmap is empty"""
        pass
    
    def clear(self):
        """Clear all entries"""
        pass
    
    def size_of(self):
        """Get number of entries"""
        pass
    
    def key_set(self):
        """Get all keys"""
        pass
    
    def values(self):
        """Get all values"""
        pass
    
    def entry_set(self):
        """Get all key-value pairs"""
        pass
    
    def resize(self):
        """Resize hashmap when load factor exceeded"""
        pass
    
    def display(self):
        """Display all entries"""
        pass


class LinkedHashMap(HashMap):
    """Template for LinkedHashMap (maintains insertion order)"""
    
    def __init__(self, capacity=16):
        """Initialize linked hashmap"""
        super().__init__(capacity)
        self.order = []
    
    def put(self, key, value):
        """Insert or update with order tracking"""
        pass
    
    def display_ordered(self):
        """Display entries in insertion order"""
        pass


class ConcurrentHashMap:
    """Template for Thread-Safe ConcurrentHashMap"""
    
    def __init__(self, capacity=16):
        """Initialize concurrent hashmap"""
        pass
    
    def put(self, key, value):
        """Thread-safe insert or update"""
        pass
    
    def get(self, key):
        """Thread-safe get"""
        pass
    
    def remove(self, key):
        """Thread-safe remove"""
        pass
