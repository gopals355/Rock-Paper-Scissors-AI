import random

class RPS_AI:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.results = []
        self.win_loss_dict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        self.lose_win_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    def make_move(self):
        if len(self.results) == 0:
            ai_move = random.choice(self.moves)
        else:
            player_last_move = self.results[-1]
            ai_move = self.win_loss_dict[player_last_move]
        return ai_move

    def record_result(self, player_move, ai_move):
        self.results.append(player_move)
        if ai_move == player_move:
            print("Tie!")
        elif ai_move == self.win_loss_dict[player_move]:
            print("You win!")
        else:
            print("You lose!")

rps_ai = RPS_AI()

while True:
    player_move = input("Enter your move (rock/paper/scissors): ")
    if player_move.lower() not in rps_ai.moves:
        print("Invalid move. Please enter either rock, paper, or scissors.")
        continue
    ai_move = rps_ai.make_move()
    print("AI move: ", ai_move)
    rps_ai.record_result(player_move.lower(), ai_move.lower())
