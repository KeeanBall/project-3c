print("Enter the integer for the player to guess.")
num = int(input())
guessed_right = False
print("Enter your guess.")
guess = int(input())
num_guesses = 0
while not guessed_right:
    if guess > num:
        print("Too high - try again:")
        guess = int(input())
    elif guess < num:
        print("Too low - try again:")
        guess = int(input())
    else:
        guessed_right = True
    num_guesses += 1
print(f"You guessed it in {num_guesses} tries.")
