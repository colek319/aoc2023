from collections import namedtuple


def solvea(problem_input):
    Number = namedtuple('Number', ['value', 'location'])
    symbol_locations = {}  # map of strings representing the symbols
    number_locations = {}  # map of tuples representing the sequence of numbers
    for i, line in enumerate(problem_input):
        number_stack = []
        for j, c in enumerate(line):
            if c.isnumeric():
                number_stack.append((i, j))
            elif len(number_stack) != 0:
                num_sum = 0
                for (numi, numj) in number_stack:
                    num = int(problem_input[numi][numj])
                    num_sum = num_sum * 10 + num
                number_stack = []
                print(num_sum)
    return "not implemented"


def solveb(problem_input):
    print("not implemented")
