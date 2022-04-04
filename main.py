def fibonacci(position: int) -> int:
    """ Returns the number at the position given in the fibonacci sequence. """
    if position < 2:
        return position
    else:
        return fibonacci(position - 2) + fibonacci(position - 1)


assert fibonacci(5) == 5

print(fibonacci(1))
print(fibonacci(4))
