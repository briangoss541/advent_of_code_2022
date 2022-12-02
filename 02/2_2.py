test_input = """A Y
B X
C Z"""

with open('input.txt') as in_file:
    input_string = in_file.read()


def rps_response(opp, req_outcome):
    if req_outcome == 'Draw':
        return opp
    elif opp == 'r':
        if req_outcome == 'Opponent':
            return 's'
        elif req_outcome == 'Player':
            return 'p'
    elif opp == 'p':
        if req_outcome == 'Opponent':
            return 'r'
        elif req_outcome == 'Player':
            return 's'
    elif opp == 's':
        if req_outcome == 'Opponent':
            return 'p'
        elif req_outcome == 'Player':
            return 'r'


total_score = 0
for game_round in input_string.split('\n'):

    if game_round == '':
        continue

    opponent_move, strategy_move = game_round.split(' ')

    opponent_map = {'A': 'r',
                    'B': 'p',
                    'C': 's'}

    outcome_map = {'X': 'Opponent',
                   'Y': 'Draw',
                   'Z': 'Player'}

    shape_points = {'r': 1,
                    'p': 2,
                    's': 3}

    outcome_points = {'Opponent': 0,
                      'Draw': 3,
                      'Player': 6}

    outcome = rps_response(opponent_map[opponent_move], outcome_map[strategy_move])

    round_points = shape_points[outcome] + outcome_points[outcome_map[strategy_move]]
    total_score += round_points

print(total_score)
