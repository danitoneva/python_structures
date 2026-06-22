"""This module is for testing the basic operations of the FIFO queue."""
import pytest
from src.lifo_stack import LifoStack


class TestLifoStack():
    """This class tests the operations like push, pop, peek, is_empty and size."""

    def test_push(self):
        dq = LifoStack()
        dq.push(1)
        dq.push(2)
        dq.push(3)
        expected = [1, 2, 3]
        result = dq.items
        assert expected == result

    def test_is_empty(self):
        dq = LifoStack()

        with pytest.raises(ValueError):
            dq.pop()

    def test_pop(self):
        dq = LifoStack()
        dq.push(1)
        dq.push(2)
        dq.push(3)
        dq.pop()
        expected = [1, 2]
        result = dq.items
        assert expected == result

    def test_size(self):
        dq = LifoStack()
        dq.push(1)
        dq.push(2)
        dq.push(3)
        expected = 3
        result = dq.size()
        assert expected == result

    def test_peek(self):
        dq = LifoStack()
        dq.push(1)
        dq.push(2)
        dq.push(3)
        expected = 1
        result = dq.peek()
        assert expected == result

if __name__ == '__main__':
    pytest.main()
