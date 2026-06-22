"""This module is for testing the basic operations of the FIFO queue."""
import pytest
from src.fifo_queue import FifoQueue


class TestFifoQueue():
    """This class tests the operations like enqueue, dequeue, is_empty and size."""

    def test_enqueue(self):
        dq = FifoQueue()
        dq.enqueue(1)
        dq.enqueue(2)
        dq.enqueue(3)
        expected = [1, 2, 3]
        result = dq.items
        assert expected == result

    def test_is_empty(self):
        dq = FifoQueue()

        with pytest.raises(ValueError):
            dq.dequeue()

    def test_dequeue(self):
        dq = FifoQueue()
        dq.enqueue(1)
        dq.enqueue(2)
        dq.enqueue(3)
        dq.dequeue()
        expected = [2, 3]
        result = dq.items
        assert expected == result

    def test_size(self):
        dq = FifoQueue()
        dq.enqueue(1)
        dq.enqueue(2)
        dq.enqueue(3)
        expected = 3
        result = dq.size()
        assert expected == result

if __name__ == '__main__':
    pytest.main()
