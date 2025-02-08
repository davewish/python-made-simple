import random


def word_guessing_game():
    # Step 1: Predefine a list of words
    words = ["python", "java", "ruby", "javascript"]

    # Step 2: Randomly select a word
    target_word = random.choice(words)

    print("Welcome to the Word Guessing Game!")
    print("Guess the word from the list:", words)

    # Step 3: Initialize attempt counter
    attempts = 0

    while True:
        # Step 4: Prompt user for a guess
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1  # Track the attempt

        # Step 5: Provide feedback
        if guess == target_word:
            print(f"Congratulations! You guessed the correct word in {attempts} attempts!")
            break
        else:
            print("Incorrect! Try again.")


# Run the game
word_guessing_game()
