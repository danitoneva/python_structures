"""Linked-list node structures and operations"""


class Node:
    "Creates nodes for singly linked list."
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    "Creates nodes for doubly linked list."
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class SinglyLinkedList:
    """This class is for singly linked list and basic operations."""
    def __init__(self):
        self.head = None

    def detect_loop(self, head):
        "This loop is for detection of a loop using Floyd's Cycle-Finding Algorithm"

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def reverse_list(self, head):
        """This function reverses the list."""
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def nth_to_last(self, head, n):
        """Find nth to last node of a linked list."""
        fast = head
        slow = head
        i = 1

        while fast and i <= n:
            fast = fast.next
            i += 1

        while fast:
            fast = fast.next
            slow = slow.next

        return slow.data
