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
        if not self.head:
            self.head = new_element
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp = self.head
        count = 1
        while(temp):
            if count == position:
                return temp
            temp = temp.next
            count += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        temp = self.get_position(position - 1)
        new_element.next = temp.next
        temp.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        prev_node, current_node = self.head, self.head.next
        if prev_node.value == value:
            self.head = prev_node.next
            prev_node = None
            return        
        while current_node is not None:
            if current_node == value:
                prev_node.next = current_node.next
            prev_node, current_node = current_node, current_node.next

def main():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    e4 = Element(4)
    ll.insert(e4, 3)
    ll.delete(1)
    print("1",ll.get_position(1).value)
    print("2",ll.get_position(2).value)
    print("3",ll.get_position(3).value)

if __name__ == "__main__":
    main()