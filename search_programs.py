def binary_search_contains(number_to_find: int, numbers: list) -> bool:
    lower_bound: int = 0
    higher_bound: int = len(numbers) - 1

    while lower_bound <= higher_bound:
        middle_bound: int = (lower_bound + higher_bound) // 2
        middle_number: int = numbers[middle_bound]

        if middle_number < number_to_find:
            lower_bound = middle_bound + 1
        elif middle_number > number_to_find:
            higher_bound = middle_bound - 1
        else:
            return True

    return False


assert binary_search_contains(60, [1, 10, 54, 60, 80, 100, 120, 200, 367]) == True
assert binary_search_contains(136, [1, 32, 54, 72, 84, 96, 102, 120, 128]) == False



