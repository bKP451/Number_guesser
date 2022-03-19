import random
from number_guesser_art import logo
print(logo)
print("WELCOME TO THE NUMBER GUESSING GAME !!! ")
user_level = input("""I am thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': 
""").lower()
target_number = random.choice(range(100))
# print(target_number)

if user_level == 'easy':
    lives = 10
elif user_level == 'hard':
    lives = 5
else:
    print("Sorry !! You entered wrong level")
    exit()

game_finished = False
while not game_finished:
    if lives == 0:
        print(f"Sorry you could not guess the number ! The number was {target_number}")
        game_finished = True
    guess = int(input("Enter a guess "))
    if guess == target_number:
        print("Hurray !! You guessed it right")
        game_finished = True
    elif guess > target_number:
        lives -= 1
        print(f"""Too high. \nGuess Again. You have {lives} attempts to guess the number.""")
    else:
        lives -= 1
        print(f"""Too  low. \nGuess Again. You have {lives} attempts to guess the number.""")

