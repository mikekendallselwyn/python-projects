def fibonacci(position: int) -> int:
    """ Returns the number at the position given in the fibonacci sequence. """
    if position < 2:
        return position
    else:
        return fibonacci(position - 2) + fibonacci(position - 1)


assert fibonacci(5) == 5

print(fibonacci(1))
print(fibonacci(4))


def memoization_fibonacci(position: int, computed: dict = {}) -> int:
    """This function returns the number at the given position, but uses memoization for efficiency"""
    if position < 2:
        return position
    else:
        if not computed.get(position):
            computed[position] = memoization_fibonacci(position - 2, computed) + memoization_fibonacci(position - 1,
                                                                                                       computed)
    return computed.get(position)


assert memoization_fibonacci(5) == 5

print(memoization_fibonacci(1))
print(memoization_fibonacci(4))


def iterative_fibonacci(position: int) -> int:
    """This function iterates from 0 to the given number to calculate what element is in
        the fibonacci sequence at the given position"""

    if position == 0:
        return 0
    last_number: int = 0
    next_number: int = 1

    for _ in range(1, position):
        last_number, next_number = next_number, last_number + next_number

    return next_number


assert iterative_fibonacci(5) == 5
print(iterative_fibonacci(1))
print(iterative_fibonacci(4))
