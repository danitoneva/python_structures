"""This module is for testing insertion at the front and back of the deque."""
import pytest
from src.deque_data_structure import Deque

class TestDeque():
    """This class is for testing insertion at the front and back of the deque."""

    def test_insert_front(self):
        dq = Deque()
        dq.insert_front(5)
        dq.insert_front(10)
        expected = [10, 5]
        result = dq.to_list()
        assert expected == result

    def test_insert_rear(self):
        dq = Deque()
        dq.insert_rear(5)
        dq.insert_rear(10)
        expected = [5, 10]
        result = dq.to_list()
        assert expected == result

if __name__ == '__main__':
    pytest.main()
