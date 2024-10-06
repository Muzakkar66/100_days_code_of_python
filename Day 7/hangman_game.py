import random
import hangman_word
word_list = ["aardvark", "baboon", "camel"]

while True:
    lives = 6
    chosen_word = random.choice(hangman_word.word_list)
    print("New word chosen!")

    correct_letters = []
    game_over = False

    while not game_over:
        # Generate display based on guessed letters so far
        display = ""
        for letter in chosen_word:
            if letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Current word:", display)

        # Check if player has won
        if "_" not in display:
            print("You Win!")
            break

        guess = input("Guess a letter: ").lower()
        if guess in correct_letters:
            print(f"You have already guessed ${guess}")
        # Check if the guessed letter is in the word
        if guess in chosen_word:
            correct_letters.append(guess)
        else:
            lives -= 1
            print(f"Incorrect! Lives remaining: {lives}")
            if lives == 0:
                game_over = True
                print("You lose!")
                break

    # Prompt to restart the game
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
