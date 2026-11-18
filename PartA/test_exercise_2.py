import pytest, time
from exercise_2 import fibonacci_iterative, fibonacci_recursive

def fib_test():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_iterative(0) == 0

    assert fibonacci_recursive(1) == 1
    assert fibonacci_iterative(1) == 1

    assert fibonacci_recursive(5) == 5
    assert fibonacci_iterative(5) == 5

    assert fibonacci_recursive(7) == 13
    assert fibonacci_iterative(7) == 13

    assert fibonacci_recursive(10) == 55
    assert fibonacci_iterative(10) == 55

    assert fibonacci_recursive(15) == 610
    assert fibonacci_iterative(15) == 610


pytest.main()

start = time.perf_counter()
fibonacci_iterative(40)
end = time.perf_counter()
print("Execution time (iterative):", end - start, "seconds")

start = time.perf_counter()
fibonacci_recursive(40)
end = time.perf_counter()
print("Execution time (recursive):", end - start, "seconds")


# (i = interative, r = recursive)
# Records of speed

# + n = 10
# i = 0.000008
# r = 0.0001

# + n = 20
# i = 0.000006
# r = 0.001

# + n = 30
# i = 0.000007
# r = 0.12

# + n = 35
# i = 0.000009
# r = 1.72

# + n = 40
# i = 0.00001
# r = 11