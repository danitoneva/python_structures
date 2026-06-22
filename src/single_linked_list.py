


class Node:
    "Creates linked list."
    def __init__(self, node):
        self.data = node
        self.next = None

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
