from collections import namedtuple

Card = namedtuple('Card', ['winning', 'selected'])


def winning_numbers(card):
    wset = set(card.winning)
    sset = set(card.selected)
    return wset.intersection(sset)


def read_card(card_raw):
    winning_raw, selected_raw = card_raw.split('|')
    winning = set(map(lambda x: int(x), winning_raw.strip().split()))
    selected = set(map(lambda x: int(x), selected_raw.strip().split()))
    card = Card(winning, selected)
    return card


def solvea(problem_input):
    cards = []
    for line in problem_input:
        card_raw = line.split(':')[1].strip()
        card = read_card(card_raw)
        cards.append(card)
    points = [int(2**(len(winning_numbers(card)) - 1)) for card in cards]
    return sum(points)


def solveb(problem_input):
    win_counts = []
    for i, line in enumerate(problem_input):
        card_num, card_raw = line.split(':')[0].strip(), line.split(':')[1].strip()
        card = read_card(card_raw)
        winner_set = winning_numbers(card)
        win_counts.append(len(winner_set))

    card_counts = [1] * len(problem_input)
    for card_idx in range(len(win_counts) - 1, -1, -1):
        # start at the end, iterate backwards since we only ever repeat indexes ahead
        wins = win_counts[card_idx]
        end_card_idx = min(len(card_counts), card_idx + wins)
        for i in range(card_idx + 1, end_card_idx + 1):
            card_counts[card_idx] += card_counts[i]

    return sum(card_counts)
