import random

class RPS_AI:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.move_counts = {move: 0 for move in self.moves}
        self.player_moves = []

    def update_move_counts(self, move):
        self.move_counts[move] += 1
        self.player_moves.append(move)

    def make_move(self):
        if sum(self.move_counts.values()) == 0:
            return random.choice(self.moves)

        winning_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

        # consider the player's most recent moves in addition to overall move counts
        last_few_moves = self.player_moves[-3:]
        last_few_move_counts = {move: last_few_moves.count(move) for move in self.moves}
        most_common_move = max(last_few_move_counts, key=last_few_move_counts.get)

        if last_few_move_counts[most_common_move] >= 2:
            ai_move = winning_moves[most_common_move]
        else:
            most_common_move = max(self.move_counts, key=self.move_counts.get)
            ai_move = winning_moves[most_common_move]

        return ai_move

    def record_result(self, player_move, ai_move):
        self.update_move_counts(player_move)

        if player_move == ai_move:
            print("Tie!")
        elif ai_move == winning_moves[player_move]:
            print("AI wins!")
        else:
            print("Player wins!")


# test the AI
rps_ai = RPS_AI()
while True:
    player_move = input("Enter your move (rock/paper/scissors): ")
    if player_move not in rps_ai.moves:
        print("Invalid move. Try again.")
        continue

    ai_move = rps_ai.make_move()
    print(f"AI played {ai_move}")

    rps_ai.record_result(player_move, ai_move)
