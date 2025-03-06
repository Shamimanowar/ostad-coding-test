
from typing import List, Tuple

class Node():
    def __init__(self, value: int, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


# Task-1
def integer_to_linked_list(n: int) -> Node:
    # Convert the integer to a string to process digits and sign
    n_str = str(n)
    head = None
    current = None

    for char in n_str:
        # Create a new Node for each character
        new_node = Node(char)
        if not head:  # If it's the first node, make it the head
            head = new_node
        else:
            current.next = new_node
            new_node.prev = current
        current = new_node

    return head

# Task-1
def linked_list_to_integer(head: Node) -> int:
    # Traverse the linked list to reconstruct the integer
    current = head
    num_str = ""
    while current:
        num_str += str(current.value)
        current = current.next

    return int(num_str)



# Task-2
def delete_from_linked_list(array, head):
    # Convert the array to a set for O(1) lookups
    values_to_remove = set(array)
    
    # Create a dummy node to handle edge cases
    dummy = Node(0)
    dummy.next = head
    current = dummy
    
    # Traverse the linked list
    while current.next:
        if current.next.val in values_to_remove:
            # Skip the node to remove it
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next



test_cases_integer_to_linked_list = [
    {"serial": 1, "input": 12345, "expected_output": "1 <-> 2 <-> 3 <-> 4 <-> 5"},
    {"serial": 2, "input": 7, "expected_output": "7"},
    {"serial": 3, "input": -789, "expected_output": "- <-> 7 <-> 8 <-> 9"},
    {"serial": 4, "input": 0, "expected_output": "0"},
    {"serial": 5, "input": 9876543210, "expected_output": "9 <-> 8 <-> 7 <-> 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> 0"}
]

if __name__ == '__main__':
    pass