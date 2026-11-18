def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i != 0:
            continue

        for j in range(2, n):
            if n % j != 0:
                continue

            if i * j == n:
                return False
    return True

def display_primes(limit: int) -> list:
    return [n for n in range(limit + 1) if is_prime(n)]

print(display_primes(25))

# my solution reduced the number of operations by using modulus to tell if a number is even divisible before trying its multiplication table