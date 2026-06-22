"""FIFO Queue data structure with basic operations: enqueue, dequeue, is_empty and size."""


class FifoQueue:
    """This class creates a FIFO Queue and basic operation like enqueue, dequeue, is_empty and size."""
    def __init__(self):
        """This functions creates a list for the queue."""
        self.items = []

    def enqueue(self, item):
        """Add elements to the end of the queue."""
        self.items.append(item)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def dequeue(self):
        """Removes elements from the front of the queue."""
        if self.is_empty():
            raise ValueError("The queue is empty.")
        return self.items.pop(0)

    def size(self):
        "This functions returns the size of the queue."
        return len(self.items)
