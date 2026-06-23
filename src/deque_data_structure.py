""""
This module implements a double-ended queue(deque) data structure 
that supports adding and removing elements from both - the front and the rear.
"""
class Node:
    """
    This class is for doubly linked list.
    """
    def __init__(self, data):
        """
        Function for creating doubly linked list.
        
        :parameter data: value stored in the node
        :parameter prev: reference to previous node
        :parameter next: reference to next node
        """
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    """
    This class is for implementation of deque using doubly linked list.
    """
    def __init__(self):
        """
        Initializes an empty deque.

        :parameter front: the first element of the dequeue
        :parameter rear: the last element of the dequeue
        :parameter size: the size of the deque 
        """
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """
        Checking to see if the deque is empty.
        
        :return: True/False
        """
        return self.front is None

    def get_size(self):
        """
        Checking the size.
        
        :return size: int
        """
        return self.size

    def insert_front(self, data):
        """
        This function inserts an element at the beginning of the deque.
        
        :parameter data: value to insert
        """
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def insert_rear(self, data):
        """
        This function inserts an element at the end of the queue.
        
        :parameter data: value to insert
        """
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def remove_front(self):
        """
        This function removes an element from the front of the queue.
        
        :parameter data: value to delete
        """
        if self.is_empty():
            raise ValueError("UnderFlow")
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1

    def remove_rear(self):
        """
        This function remove an element from the end of the queue.
        
        :parameter data: value to delete
        """
        if self.is_empty():
            raise ValueError("UnderFlow")
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1

    def to_list(self):
        """
        Returns the deque as a list.
        
        :return: a list with all elements
        """
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result
