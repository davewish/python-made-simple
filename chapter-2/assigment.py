import random

# Step 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2: Initialize a counter for attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Step 3: Start the guessing loop
while True:
    # Step 4: Get the user's guess
    guess = input("Enter your guess: ")
    guess = int(guess)  # Convert input to an integer
    attempts += 1  # Increment the attempt counter

    # Step 5: Provide feedback
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  # Exit the loop when the guess is correct