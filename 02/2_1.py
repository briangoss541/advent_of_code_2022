test_input = """A Y
B X
C Z"""

with open('input.txt') as in_file:
    input_string = in_file.read()

def rps(opp, player):

    if opp == player:
        return 'Draw'
    elif opp == 'r' and player != 'p':
        return 'Opponent'
    elif opp == 'p' and player != 's':
        return 'Opponent'
    elif opp == 's' and player != 'r':
        return 'Opponent'
    else:
        return 'Player'


total_score = 0
for game_round in input_string.split('\n'):

    if game_round == '':
        continue

    opponent_move, strategy_move = game_round.split(' ')

    opponent_map = {'A': 'r',
                    'B': 'p',
                    'C': 's'}

    strategy_map = {'X': 'r',
                    'Y': 'p',
                    'Z': 's'}

    shape_points = {'r': 1,
                    'p': 2,
                    's': 3}

    outcome_points = {'Opponent': 0,
                      'Draw': 3,
                      'Player': 6}

    outcome = rps(opponent_map[opponent_move], strategy_map[strategy_move])

    round_points = shape_points[strategy_map[strategy_move]] + outcome_points[outcome]
    total_score += round_points

print(total_score)
