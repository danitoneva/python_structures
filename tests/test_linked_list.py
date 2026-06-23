"""This module is for testing insertion at the front and back of the deque."""
import pytest
from src.linked_list import Node, SinglyLinkedList
from src.linked_list import DoublyNode

class TestSingleLinkedList():
    """This class is for testing single linked list and common operations."""

    def test_detect_loop(self):
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(4)
        head.next.next.next = head.next

        expected = True
        result = SinglyLinkedList.detect_loop(self, head)
        assert expected == result

    def test_no_loop_detected(self):
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(4)
        head.next.next.next = Node(5)

        expected = False
        result = SinglyLinkedList.detect_loop(self, head)
        assert expected == result

    def test_reverse_list(self):
        head = Node(10)
        head.next = Node(20)
        head.next.next = Node(30)

        result = []
        current = SinglyLinkedList.reverse_list(self, head)
        while current:
            result.append(current.data)
            current = current.next

        expected = [30, 20, 10]
        assert expected == result

    def test_nth_to_last(self):
        head = Node(3)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(5)
        head.next.next.next.next = Node(4)

        n = 2
        expected = 5
        result = SinglyLinkedList.nth_to_last(self, head, n)
        assert expected == result

class TestDoublyLinkedList():
    def test_doubly_linked_list(self):
        d1 = DoublyNode(10)
        d2 = DoublyNode(20, prev=d1)
        d1.next = d2

        assert d1.next == d2
        assert d2.prev is d1

if __name__ == '__main__':
    pytest.main()
