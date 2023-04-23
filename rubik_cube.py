import random    # the chance of the game
random_number = random.randint(18, 26)   # max and min moves to solve
sides_of_colors = 6 + 6 * 3   # the total moves needed in worst case
time_to_1st = sides_of_colors - random_number 
total_moves = sides_of_colors - time_to_1st  # total moves for this cube 
print(f"Total moves of player: {total_moves}")   
    
