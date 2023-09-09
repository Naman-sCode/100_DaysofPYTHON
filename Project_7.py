import random
# Hangman Logic
# word_list = ["advark", "baboon", "camel"]


chosen_word = random.choice(word_list)
display = []
lives = len(chosen_word)
for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")


    print(stages[lives])
