"""Linked-list node structures and operations"""


class Node:
    "Creates linked list."
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
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
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
