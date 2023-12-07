from collections import namedtuple
from functools import reduce


def solvea(problem_input):
    width = len(problem_input[0])
    height = len(problem_input)
    Number = namedtuple('Number', ['value', 'location'])
    symbol_locations = {}  # map of strings representing the symbols
    numbers = []  # map of tuples representing the sequence of numbers

    for i, line in enumerate(problem_input):
        number_stack = []
        for j, c in enumerate(line):
            if c.isnumeric():
                number_stack.append((i, j))
            elif c != '.':  # we have a symbol
                symbol_locations[(i, j)] = c

            if len(number_stack) != 0 and not c.isnumeric():
                num_sum = 0
                for (numi, numj) in number_stack:
                    num = int(problem_input[numi][numj])
                    num_sum = num_sum * 10 + num
                numbers.append(Number(num_sum, tuple(number_stack)))
                number_stack = []

        if len(number_stack) != 0:
            num_sum = 0
            for (numi, numj) in number_stack:
                num = int(problem_input[numi][numj])
                num_sum = num_sum * 10 + num
            numbers.append(Number(num_sum, tuple(number_stack)))

    part_numbers = []
    for number in numbers:
        for (i, j) in number.location:
            part_number = None
            adjacent_locations = get_surrounding_indices(i, j, height, width)
            for loc in adjacent_locations:
                if loc not in symbol_locations:
                    continue
                part_number = number.value
            if part_number:
                part_numbers.append(part_number)
                break

    return sum(part_numbers)


def get_surrounding_indices(i, j, height, width):
    # Define all possible directions around a cell in a 2D grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    surrounding_indices = []

    for direction in directions:
        di, dj = i + direction[0], j + direction[1]
        # Check if the new indices are within the bounds of the grid
        if 0 <= di < height and 0 <= dj < width:
            surrounding_indices.append((di, dj))

    return surrounding_indices


def solveb(problem_input):
    width = len(problem_input[0])
    height = len(problem_input)
    Number = namedtuple('Number', ['value', 'location'])
    gear_locations = {}  # map of strings representing the symbols
    numbers = []  # map of tuples representing the sequence of numbers

    for i, line in enumerate(problem_input):
        number_stack = []
        for j, c in enumerate(line):
            if c.isnumeric():
                number_stack.append((i, j))
            elif c == '*':  # we have a symbol
                gear_locations[(i, j)] = set()

            if len(number_stack) != 0 and not c.isnumeric():
                num_sum = 0
                for (numi, numj) in number_stack:
                    num = int(problem_input[numi][numj])
                    num_sum = num_sum * 10 + num
                numbers.append(Number(num_sum, tuple(number_stack)))
                number_stack = []

        if len(number_stack) != 0:
            num_sum = 0
            for (numi, numj) in number_stack:
                num = int(problem_input[numi][numj])
                num_sum = num_sum * 10 + num
            numbers.append(Number(num_sum, tuple(number_stack)))

    for number in numbers:
        for (i, j) in number.location:
            part_number = None
            adjacent_locations = get_surrounding_indices(i, j, height, width)
            for loc in adjacent_locations:
                if loc not in gear_locations:
                    continue
                # we found a
                part_number = number.value
                gear_locations[loc].add(part_number)
            if part_number:
                break

    gear_ratios = []
    for part_numbers in gear_locations.values():
        if len(part_numbers) == 2:
            ratio = reduce(lambda x, y: x * y, part_numbers)
            gear_ratios.append(ratio)

    return sum(gear_ratios)
