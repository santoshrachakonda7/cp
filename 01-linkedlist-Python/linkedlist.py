"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        new_element = Element(new_element)
        t = self.head
        if(self.head):
            while(t.next):
                t = t.next
            t.next = new_element
        else:
            self.head = new_element
        
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        t = self.head
        count = 1
        if(position < 1):
            return None
        while(t and count <= position):
            if(count == (position)):
                return t.value
            count += 1
            t = t.next
        return None

    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if(position == 1):
            node = Element(new_element)
            node.next = self.head
            self.head = node
        a = 1
        h = self.head
        while(a < position-1 and h != None):
            h = h.next
            a += 1
        if(h != None):
            node = Element(new_element)
            node.next = h.next
            h.next = node
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        t = self.head
        pre_node = None
        while(t.next and t.value != value):
            pre_node = t
            t = t.next
        if(t.value == value):
            if(pre_node):
                pre_node.next = t.next
            self.head = t.next
