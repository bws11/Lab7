# Only one disk can be moved at a time.
# Only the top disk of a rod can be moved.
# A larger disk cannot be placed on top of a smaller disk.

# disks (2^n) - 1 moves
# I renamed the parameters because i like these more
def hanoi(n: int, source: str, helper: str, destination: str) -> list[tuple[str, str]]:
    """Return the moves needed to move n disks from source to destination."""
    
    if n < 0:
        raise ValueError("n must be zero or greater")

    # Use a set to immediately remove any duplicates
    if len({source, helper, destination}) != 3:
        raise ValueError("The rods must have different names")

    if n == 0:
        return []

    # move the smaller stack out of the way
    moves = hanoi(n - 1, source, destination, helper)

    # move largest disk to the destination
    moves.append((source, destination))

    # Finally move the smaller stack onto the largest disk
    moves.extend(hanoi(n - 1, helper, source, destination))

    return moves


print("Outcome: ", hanoi(3, "A", "B", "C"))