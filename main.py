import random

class RPS_AI:
    def __init__(self):
        self.total_moves = {"rock": 0, "paper": 0, "scissors": 0}
        self.winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        self.last_few_moves = []
    
    def record_result(self, player_move, ai_move):
        self.total_moves[player_move] += 1
        self.total_moves[ai_move] += 1
        self.last_few_moves.append(player_move)
        if len(self.last_few_moves) > 3:
            self.last_few_moves.pop(0)
    
    def predict_move(self):
        if not self.last_few_moves:
            return random.choice(list(self.total_moves.keys()))
        move_counts = self.total_moves.copy()
        for i in range(len(self.last_few_moves)-1):
            move_counts[self.last_few_moves[i]] -= 1
            if self.last_few_moves[i] == self.last_few_moves[-1]:
                move_counts[self.last_few_moves[i+1]] -= 1
        predicted_move = max(move_counts, key=move_counts.get)
        counter_move = self.winning_moves[predicted_move]
        return counter_move
    
    def make_move(self):
        ai_move = self.predict_move()
        player_move = input("Enter your move (rock/paper/scissors): ")
        while player_move not in ["rock", "paper", "scissors"]:
            print("Invalid move, please enter rock, paper, or scissors.")
            player_move = input("Enter your move (rock/paper/scissors): ")
        self.record_result(player_move, ai_move)
        if ai_move == player_move:
            print("Tie!")
        elif ai_move == self.winning_moves[player_move]:
            print("You win!")
        else:
            print("I win!")
