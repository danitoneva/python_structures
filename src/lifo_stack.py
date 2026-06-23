"""LIFO stack with basic operations: push, pop, peek, is_empty and size."""


class LifoStack:
    """
    This class creates a LIFO stack and basic operation like 
    push, pop, peek, is_empty and size.
    """
    def __init__(self):
        """
        This functions creates a list for the stack.
        
        :parameter items: an empty list 
        """
        self.items = []

    def push(self, item):
        """
        Add elements to the end of the stack.
        
        :parameter item: element inserted in the list
        """
        self.items.append(item)

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        :return: the size of the list
        """
        return len(self.items) == 0

    def pop(self):
        """
        Removes elements from the front of the stack.
        
        :return: the element that is deleted
        """
        if self.is_empty():
            raise ValueError("The stack is empty.")
        return self.items.pop()

    def size(self):
        """
        This functions returns the size of the stack.
        
        :return size: int
        """
        return len(self.items)

    def peek(self):
        """
        Return the first element.
        
        :return: first element
        """
        return self.items[0]
