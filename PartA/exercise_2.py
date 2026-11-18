def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n

    numbers = [0, 1]
    for i in range(n - 2):
        numbers.append(numbers[i] + numbers[i + 1])

    return numbers[len(numbers) - 1] + numbers[len(numbers) - 2]


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
