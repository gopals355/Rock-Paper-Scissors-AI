import random

class RPSAI:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.winning_moves = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        self.results = []

    def record_result(self, player_move, ai_move):
        if player_move == ai_move:
            self.results.append("tie")
        elif ai_move == self.winning_moves[player_move]:
            self.results.append("loss")
        else:
            self.results.append("win")

    def make_move(self):
        if not self.results:
            # If no results have been recorded yet, choose a random move
            return random.choice(self.moves)

        last_result = self.results[-1]
        if last_result == "win":
            # If the last result was a win, choose the move that beats the player's last move
            player_last_move = self.moves[self.moves.index(self.results[-2])]
            return self.winning_moves[player_last_move]
        elif last_result == "loss":
            # If the last result was a loss, choose a random move
            return random.choice(self.moves)
        else:
            # If the last result was a tie, choose the move that beats the player's last move
            player_last_move = self.moves[self.moves.index(self.results[-2])]
            return self.winning_moves[player_last_move]

# Example usage:
ai = RPSAI()
while True:
    player_move = input("Enter your move (rock/paper/scissors): ")
    ai_move = ai.make_move()
    print(f"AI move: {ai_move}")
    ai.record_result(player_move, ai_move)
    print(f"Results so far: {ai.results}\n")
