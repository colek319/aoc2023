from functools import reduce

RED_STR = 'red'
GREEN_STR = 'green'
BLUE_STR = 'blue'

RED_COUNT = 12
GREEN_COUNT = 13
BLUE_COUNT = 14

COLOR_COUNTS = {
    RED_STR: RED_COUNT,
    GREEN_STR: GREEN_COUNT,
    BLUE_STR: BLUE_COUNT
}


def solvea(problem_input):
    possible_games_ids = []
    for line in problem_input:
        game_raw, results_raw = line.split(':')
        game_number = parse_game(game_raw)
        results = parse_results(results_raw)
        found_bad_case = False
        for game_round in results:
            for color, count in game_round.items():
                if count > COLOR_COUNTS.get(color, 0):
                    found_bad_case = True
                    break
            if found_bad_case:
                break
        if not found_bad_case:
            possible_games_ids.append(game_number)
    return sum(possible_games_ids)


def solveb(problem_input):
    power_of_rounds = []
    for line in problem_input:
        game_raw, results_raw = line.split(':')
        results = parse_results(results_raw)
        minimum_cube_set = {}
        for game_round in results:
            for color, count in game_round.items():
                minimum_cube_set[color] = max(minimum_cube_set.get(color, 0), count)
        # get product of all values in minimum_cube_set
        power = reduce(lambda x, y: x * y, minimum_cube_set.values())
        power_of_rounds.append(power)
    return sum(power_of_rounds)


def get_input(filename):
    # Process the file
    lines = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return lines


def parse_game(game_raw):
    _, round_number = game_raw.split()
    return int(round_number)


def parse_results(results_raw):
    rounds_raw = results_raw.split(';')
    rounds = []
    for r in rounds_raw:
        colors = {}
        for color_raw in r.split(','):
            color_count_str, color_id = color_raw.strip().split(' ')
            colors[color_id] = int(color_count_str)
        rounds.append(colors)
    return rounds
