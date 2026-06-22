"""This module is for testing insertion at the front and back of the deque."""
import pytest
from src.single_linked_list import Node, SingleLinkedList

class TestSingleLinkedList():
    """This class is for testing single linked list and common operations."""

    def test_detect_loop(self):
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(4)

        head.next.next.next = head.next

        expected = True
        result = SingleLinkedList.detect_loop(self, head)
        assert expected == result

    def test_no_loop_detected(self):
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(4)
        head.next.next.next = Node(5)

        expected = False
        result = SingleLinkedList.detect_loop(self, head)
        assert expected == result

if __name__ == '__main__':
    pytest.main()
