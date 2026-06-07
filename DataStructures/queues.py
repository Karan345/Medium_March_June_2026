"""
Queue and Deque Data Structure Templates
FIFO (First In First Out) for Queue, FILO for Deque
"""


class QueueArray:
    """Template for Queue using Array"""
    
    def __init__(self, capacity=100):
        """Initialize queue with given capacity"""
        self.capacity = capacity
        self.queue = []
        self.front = 0
        self.rear = -1
    
    def enqueue(self, value):
        """Add element to rear of queue"""
        pass
    
    def dequeue(self):
        """Remove element from front of queue"""
        pass
    
    def peek(self):
        """View front element without removing"""
        pass
    
    def is_empty(self):
        """Check if queue is empty"""
        pass
    
    def is_full(self):
        """Check if queue is full"""
        pass
    
    def size(self):
        """Get current size of queue"""
        pass
    
    def display(self):
        """Display all elements in queue"""
        pass


class CircularQueue:
    """Template for Circular Queue using Array"""
    
    def __init__(self, capacity=100):
        """Initialize circular queue"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, value):
        """Add element to rear"""
        pass
    
    def dequeue(self):
        """Remove element from front"""
        pass
    
    def peek(self):
        """View front element"""
        pass
    
    def is_empty(self):
        """Check if queue is empty"""
        pass
    
    def is_full(self):
        """Check if queue is full"""
        pass
    
    def display(self):
        """Display all elements"""
        pass


class QueueLinkedList:
    """Template for Queue using Linked List"""
    
    def __init__(self):
        """Initialize empty queue"""
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        """Add element to rear"""
        pass
    
    def dequeue(self):
        """Remove element from front"""
        pass
    
    def peek(self):
        """View front element"""
        pass
    
    def is_empty(self):
        """Check if queue is empty"""
        pass
    
    def display(self):
        """Display all elements"""
        pass


class DequeArray:
    """Template for Deque (Double Ended Queue) using Array"""
    
    def __init__(self, capacity=100):
        """Initialize deque"""
        self.capacity = capacity
        self.deque = []
        self.front = 0
        self.rear = -1
    
    def insert_front(self, value):
        """Insert element at front"""
        pass
    
    def insert_rear(self, value):
        """Insert element at rear"""
        pass
    
    def delete_front(self):
        """Delete element from front"""
        pass
    
    def delete_rear(self):
        """Delete element from rear"""
        pass
    
    def get_front(self):
        """Get element at front"""
        pass
    
    def get_rear(self):
        """Get element at rear"""
        pass
    
    def is_empty(self):
        """Check if deque is empty"""
        pass
    
    def display(self):
        """Display all elements"""
        pass


class DequeLinkedList:
    """Template for Deque using Linked List"""
    
    def __init__(self):
        """Initialize empty deque"""
        self.front = None
        self.rear = None
    
    def insert_front(self, value):
        """Insert element at front"""
        pass
    
    def insert_rear(self, value):
        """Insert element at rear"""
        pass
    
    def delete_front(self):
        """Delete element from front"""
        pass
    
    def delete_rear(self):
        """Delete element from rear"""
        pass
    
    def is_empty(self):
        """Check if deque is empty"""
        pass
    
    def display(self):
        """Display all elements"""
        pass
