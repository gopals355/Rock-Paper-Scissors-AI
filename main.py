import random

class RPS_AI:
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.win_table = {
            'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
            'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
            'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
        }
        self.results = []

    def record_result(self, player_move, ai_move):
        self.results.append(player_move)
        self.results.append(ai_move)

    def make_move(self):
        if len(self.results) < 2:
            return random.choice(self.moves)
        player_last_move = self.moves[self.moves.index(self.results[-2])]
        for move, result in self.win_table[player_last_move].items():
            if result == 'win':
                return move
        return random.choice(self.moves)
