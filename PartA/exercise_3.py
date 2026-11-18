def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, n):
        for j in range(2, n):
            if i * j == n:
                return False

    return True