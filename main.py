import sys
import importlib


def main(day, filename, part):
    problem_input = get_input(filename)
    solution = importlib.import_module(f'{day}.solution')
    if part == 'a':
        print(solution.solvea(problem_input))
    elif part == 'b':
        print(solution.solveb(problem_input))


def get_input(filename):
    # Process the file
    lines = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return lines


if __name__ == "__main__":
    if len(sys.argv) > 3:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("No file provided.")
