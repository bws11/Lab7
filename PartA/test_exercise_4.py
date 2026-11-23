import pytest
from exercise_4 import hanoi

def test_hanoi():
    assert hanoi(2, "A", "B", "C") == [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
    ]
    assert hanoi(3, "A", "B", "C") == [
        ('A', 'C'),
        ('A', 'B'),
        ('C', 'B'),
        ('A', 'C'),
        ('B', 'A'),
        ('B', 'C'),
        ('A', 'C')
    ]


pytest.main()