def factorial_iterative(n: int) -> int:
    total = 1

    for i in range(n):
        total *= i + 1
    return total

def factorial_recursive(n: int) -> int:
    if n > 1:
        return n * factorial_recursive(n - 1)
    return 1