import random
words = ["apple", "banana", "cherry", "grape", "kiwi", "mango", "orange", "pineapple", "strawberry", "watermelon"]
hangman_stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
      -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
      -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
      -------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
      -------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
      -------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
      -------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
      -------
    """
]

lives = 6
chosen_word = random.choice(words).lower() 
display = []
for _ in range(len(chosen_word)): 
    display += '_' 
guessed_letters = []
game_over = False
print("Welcome to Hangman!")
print(hangman_stages[6 - lives]) 
print(" ".join(display)) 
while not game_over:
    guessed_letter = input("Guess a letter: ").lower() 
    if guessed_letter in guessed_letters:
        print(f"You've already guessed '{guessed_letter}'. Try a different letter.")
        print(hangman_stages[6 - lives])
        print(" ".join(display))
        continue 
    guessed_letters.append(guessed_letter) 
    found_in_word = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = letter
            found_in_word = True
    if not found_in_word:
        lives -= 1
        print(f"'{guessed_letter}' is not in the word. You lose a life!")
        if lives == 0:
            game_over = True
            print(hangman_stages[6 - lives])
            print(f"The word was: {chosen_word}")
            print("You lose!")
        else:
            print(f"Lives remaining: {lives}")
    else:
        print(f"Good guess! '{guessed_letter}' is in the word.")
    print(hangman_stages[6 - lives])
    print(" ".join(display)) 
    if '_' not in display:
        game_over = True
        print("Congratulations! You win!")

