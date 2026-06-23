"""Linked-list node structures and operations"""


class Node:
    "Creates nodes for singly linked list."
    def __init__(self, data):
        """
        Initialize a singly linked list node.
        
        :parameter data: value to store in the node
        """
        self.data = data
        self.next = None

class DoublyNode:
    "Creates nodes for doubly linked list."
    def __init__(self, data, prev_node = None, next_node = None):
        """
        Initialize a doubly linked list node.
        
        :parameter data: value to store in the node
        :parameter prev: reference to previous node
        :parameter next: reference to next node
        """
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

class SinglyLinkedList:
    """This class is for singly linked list and basic operations."""
    def __init__(self):
        """
        Initialize an empty linked list.

        :parameter head: the first node on the list
        """
        self.head = None

    def detect_loop(self, head):
        """
        This loop is for detection of a loop using Floyd's Cycle-Finding Algorithm.

        :parameter head: the first node on the list
        :return: True/False
        """

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def reverse_list(self, head):
        """
        This function reverses a singly linked list.
        
        :parameter head: head node of the linked list
        :return: new head of the reversed list
        """
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def nth_to_last(self, head, position_from_end ):
        """
        Find nth to last node of a linked list.
        
        :parameter head: head node of the linked list
        :parameter position_from_end: position from the end
        :return: data of the nth-to-last node
        """
        fast = head
        slow = head
        i = 1

        while fast and i <= position_from_end:
            fast = fast.next
            i += 1

        while fast:
            fast = fast.next
            slow = slow.next

        return slow.data
