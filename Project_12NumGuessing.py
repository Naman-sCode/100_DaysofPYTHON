import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guess_system(guess, chosen_number):
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}")
    elif guess < chosen_number:
        print("Too Low.")
    elif guess > chosen_number:
        print("Too high")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level = "easy":
        def game():
            print(logo)
            # Choosing a random number between 1 and 100.
            print("Welcome to the Number Guessing Game!")
            print("I'm thinking of a number between 1 and 100.")
            answer = randint(1, 100)
            # print(f"Pssst, the correct answer is {answer}")

            turns = set_difficulty()
            # Repeat the guessing functionality if they get it wrong.
            guess = 0
            while guess != answer:
                print(f"You have {turns} attempts remaining to guess the number.")

                # Let the user guess a number.
                guess = int(input("Make a guess: "))

                # Track the number of turns and reduce by 1 if they get it wrong.
                turns = check_answer(guess, answer, turns)
                if turns == 0:
                    print("You've run out of guesses, you lose.")
                    return
                elif guess != answer:
                    print("Guess again.")

        game()


# print("Welcome to the Number Guessing Game!.")
# print("I'm thinking of a number between 1 and 100")
# difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard':  ").lower()
# chosen_number = random.randint(1, 100)



