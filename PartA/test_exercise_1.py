import pytest
from exercise_1 import factorial_recursive, factorial_iterative

def test_factorial():
    assert factorial_iterative(0) == 1
    assert factorial_recursive(0) == 1

    assert factorial_iterative(1) == 1
    assert factorial_recursive(1) == 1

    assert factorial_iterative(3) == 6
    assert factorial_recursive(3) == 6

    assert factorial_iterative(5) == 120
    assert factorial_recursive(5) == 120

    assert factorial_iterative(7) == 5040
    assert factorial_recursive(7) == 5040

pytest.main()