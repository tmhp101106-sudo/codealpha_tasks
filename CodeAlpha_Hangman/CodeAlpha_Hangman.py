import random

# List of words for the game
word_list = ["python", "hangman", "computer", "program", "challenge", "garden", "science"]

# Select a random word
word = random.choice(word_list)
guessed = ["_"] * len(word)
attempts = 7
used_letters = []

print("Welcome to Hangman!")
print("Guess the word:")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in used_letters:
        print("⚠ You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("✔ Good guess!")
        for index, letter in enumerate(word):
            if letter == guess:
                guessed[index] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(sorted(used_letters)))

# End of game results
if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)