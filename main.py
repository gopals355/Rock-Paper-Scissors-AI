import random

class RPS_AI:
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.results = []
    
    def make_move(self):
        if not self.results:
            # Random first move
            return random.choice(self.moves)
        
        # Get player's last move
        player_last_move = None
        if len(self.results) > 1:
            player_last_move = self.results[-2]
        
        if player_last_move and self.results.count(player_last_move) == 2:
            # Opponent repeated last move twice, play the counter move
            return self.moves[(self.moves.index(player_last_move) + 1) % len(self.moves)]
        else:
            # Otherwise, play randomly
            return random.choice(self.moves)
    
    def record_result(self, player_move, ai_move):
        # Only record the result if both moves are valid
        if player_move in self.moves and ai_move in self.moves:
            self.results.append(player_move)
            self.results.append(ai_move)

# Create an instance of the RPS_AI class
rps_ai = RPS_AI()

while True:
    # Ask the player to input their move
    player_move = input("Enter your move (rock, paper, or scissors): ")
    # Generate the AI's move
    ai_move = rps_ai.make_move()
    
    print(f"The AI played {ai_move}")
    
    # Check if the player's move is valid
    if player_move not in rps_ai.moves:
        print("Invalid move, try again.")
        continue
    
    # Determine the result of the game
    result = ""
    if player_move == ai_move:
        result = "tie"
    elif rps_ai.moves[(rps_ai.moves.index(player_move) + 1) % len(rps_ai.moves)] == ai_move:
        result
