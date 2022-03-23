import pytest

from activity.main import *

def test_exception():
    # Arrange
    num_1 = "hi"
    num_2 = "hello"

    # Act
    with pytest .raises(TypeError):
        multiply_two_nums(num_1, num_2)
