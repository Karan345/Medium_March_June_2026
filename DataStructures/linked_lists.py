"""
Linked List Data Structure Templates
Singly, Doubly, and Circular Linked Lists
"""


class Node:
    """Node class for linked list"""
    
    def __init__(self, data):
        """Initialize a node"""
        self.data = data
        self.next = None


class DoublyNode:
    """Node class for doubly linked list"""
    
    def __init__(self, data):
        """Initialize a node"""
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """Template for Singly Linked List"""
    
    def __init__(self):
        """Initialize empty singly linked list"""
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert element at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert element at the end"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        """Insert element at specific position (0-indexed)"""
        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if not current:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        """Delete element from beginning"""
        if not self.head:
            print("List is empty")
            return None
        
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data
    
    def delete_at_end(self):
        """Delete element from end"""
        if not self.head:
            print("List is empty")
            return None
        
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position (0-indexed)"""
        if position < 0 or not self.head:
            print("Invalid position or empty list")
            return None
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        count = 0
        
        while current.next and count < position - 1:
            current = current.next
            count += 1
        
        if not current.next:
            print("Position out of range")
            return None
        
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data
    
    def search(self, value):
        """Search for an element"""
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def traverse(self):
        """Traverse and display all elements"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) if elements else "List is empty")
        return elements
    
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __len__(self):
        """Get length of linked list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        """String representation of linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"


class DoublyLinkedList:
    """Template for Doubly Linked List"""
    
    def __init__(self):
        """Initialize empty doubly linked list"""
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        """Insert element at the beginning"""
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert element at the end"""
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def insert_at_position(self, data, position):
        """Insert element at specific position (0-indexed)"""
        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = DoublyNode(data)
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if not current:
            print("Position out of range")
            return
        
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node
        
        current.next = new_node
    
    def delete_at_beginning(self):
        """Delete element from beginning"""
        if not self.head:
            print("List is empty")
            return None
        
        deleted_data = self.head.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        return deleted_data
    
    def delete_at_end(self):
        """Delete element from end"""
        if not self.head:
            print("List is empty")
            return None
        
        deleted_data = self.tail.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position (0-indexed)"""
        if position < 0 or not self.head:
            print("Invalid position or empty list")
            return None
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        count = 0
        
        while current and count < position:
            current = current.next
            count += 1
        
        if not current:
            print("Position out of range")
            return None
        
        deleted_data = current.data
        
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        
        if current.prev:
            current.prev.next = current.next
        
        return deleted_data
    
    def search(self, value):
        """Search for an element"""
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def traverse_forward(self):
        """Traverse forward and display elements"""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" <-> ".join(elements) if elements else "List is empty")
        return elements
    
    def traverse_backward(self):
        """Traverse backward and display elements"""
        elements = []
        current = self.tail
        
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        print(" <-> ".join(elements) if elements else "List is empty")
        return elements
    
    def reverse(self):
        """Reverse the linked list"""
        if not self.head:
            return
        
        current = self.head
        self.head = self.tail
        self.tail = current
        
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
    
    def __len__(self):
        """Get length of doubly linked list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        """String representation of doubly linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements) if elements else "Empty"


class CircularLinkedList:
    """Template for Circular Linked List"""
    
    def __init__(self):
        """Initialize empty circular linked list"""
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert element at the beginning"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        
        new_node.next = self.head
        current.next = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert element at the end"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        
        current.next = new_node
        new_node.next = self.head
    
    def insert_at_position(self, data, position):
        """Insert element at specific position (0-indexed)"""
        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if not self.head:
            print("Position out of range")
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1
        
        if count != position - 1:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        """Delete element from beginning"""
        if not self.head:
            print("List is empty")
            return None
        
        if self.head.next == self.head:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next != self.head:
            current = current.next
        
        deleted_data = self.head.data
        current.next = self.head.next
        self.head = self.head.next
        return deleted_data
    
    def delete_at_end(self):
        """Delete element from end"""
        if not self.head:
            print("List is empty")
            return None
        
        if self.head.next == self.head:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        deleted_data = current.next.data
        current.next = self.head
        return deleted_data
    
    def delete_at_position(self, position):
        """Delete element at specific position (0-indexed)"""
        if position < 0 or not self.head:
            print("Invalid position or empty list")
            return None
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        count = 0
        
        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1
        
        if count != position - 1 or current.next == self.head:
            print("Position out of range")
            return None
        
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data
    
    def search(self, value):
        """Search for an element"""
        if not self.head:
            return -1
        
        current = self.head
        position = 0
        
        while True:
            if current.data == value:
                return position
            current = current.next
            position += 1
            if current == self.head:
                break
        
        return -1
    
    def traverse(self):
        """Traverse and display all elements"""
        if not self.head:
            print("List is empty")
            return []
        
        elements = []
        current = self.head
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements))
        return elements
    
    def display(self):
        """Display the circular linked list"""
        if not self.head:
            print("Circular List is empty")
            return
        
        print("Circular List: ", end="")
        current = self.head
        
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        
        print("(back to " + str(self.head.data) + ")")
    
    def __len__(self):
        """Get length of circular linked list"""
        if not self.head:
            return 0
        
        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count += 1
        return count
    
    def __str__(self):
        """String representation of circular linked list"""
        if not self.head:
            return "Empty"
        
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        return " -> ".join(elements) + " -> (circular)"
