import random

def roll_dice():
    """Roll two dice and return their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0

def play_game():
    player_score = 0
    computer_score = 0
    target_score = 5
    
    print("Welcome to the Even or Odd game!")
    print(f"First to {target_score} points wins!")
    
    while player_score < target_score and computer_score < target_score:
        player_guess = input("Guess even or odd (e/o): ").strip().lower()
        if player_guess not in ['e', 'o']:
            print("Invalid guess. Please enter 'e' for even or 'o' for odd.")
            continue
        
        dice_sum = roll_dice()
        print(f"Dice rolled a sum of {dice_sum}")
        
        if (is_even(dice_sum) and player_guess == 'e') or (not is_even(dice_sum) and player_guess == 'o'):
            player_score += 1
            print("You scored a point!")
        else:
            computer_score += 1
            print("Computer scored a point!")
            
        print(f"Score: You {player_score} - {computer_score} Computer")
    
    if player_score >= target_score:
        print("Congratulations! You won!")
    else:
        print("Computer won this time. Better luck next time!")

if __name__ == '__main__':
    play_game()

