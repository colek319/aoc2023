# make list of strings for 1-9
one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
numbers = set([one, two, three, four, five, six, seven, eight, nine])


def solvea(problem_input):
    sums = []
    for line in problem_input:
        first_last = []
        for c in line:
            if c.isnumeric() and len(first_last) < 2:
                first_last.append(c)
            elif c.isnumeric():
                first_last.pop()
                first_last.append(c)
        if len(first_last) < 2:
            first_last.append(first_last[0])
        together = ''.join(first_last)
        sums.append(int(together))
    return sum(sums)


def solveb(problem_input):
    sums = []
    for line in problem_input:
        first_last = []
        buffer = []
        for c in line:
            match = None
            if c.isnumeric():
                # if its numeric, we have an immediate match
                match = c
                buffer = []
            else:
                # not numeric, so we need to append to buffer and see if we have a match
                buffer.append(c)
                candidate = ''.join(buffer)
                digit = get_most_recent_number(candidate)
                if digit:
                    match = digit
                    # now update buffer
                    if digit == '1':
                        buffer = ['e']
                    elif digit == '2':
                        buffer = ['o']
                    elif digit == '3':
                        buffer = ['e']
                    elif digit == '5':
                        buffer = ['e']
                    elif digit == '7':
                        buffer = ['n']
                    elif digit == '8':
                        buffer = ['t']
                    elif digit == '9':
                        buffer = ['e']
                    else:
                        buffer = []

            if not match:
                # skip if we don't have a match
                continue

            # the second does what we did for part a
            if match.isnumeric() and len(first_last) < 2:
                first_last.append(match)
            elif match.isnumeric():
                first_last.pop()
                first_last.append(match)
        if len(first_last) < 2:
            first_last.append(first_last[0])
        together = ''.join(first_last)
        sums.append(int(together))
    return sum(sums)


def get_most_recent_number(word: str):
    words_to_check = []
    if len(word) > 2:
        # add 3 letter words
        words_to_check.append(one)
        words_to_check.append(two)
        words_to_check.append(six)
    if len(word) > 3:
        # add 4 letter words
        words_to_check.append(four)
        words_to_check.append(five)
        words_to_check.append(nine)
    if len(word) > 4:
        # add 5 letter words
        words_to_check.append(three)
        words_to_check.append(seven)
        words_to_check.append(eight)

    match = None
    for w in words_to_check:
        word_idx = len(word) - len(w)
        if word[word_idx:] == w:
            match = w

    if match == one:
        return '1'
    elif match == two:
        return '2'
    elif match == three:
        return '3'
    elif match == four:
        return '4'
    elif match == five:
        return '5'
    elif match == six:
        return '6'
    elif match == seven:
        return '7'
    elif match == eight:
        return '8'
    elif match == nine:
        return '9'
    else:
        return None