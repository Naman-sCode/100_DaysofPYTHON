import random
from Project_13 import data
import os


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')


def format_data(account):
    """ FORMATTING THE ACCOUNT DATA"""
    account_name = account['name']
    account_descr = account["description"]
    account_country = account['country']
    print(f"{account_name}, a {account_descr}, from {account_country}")


def check_answer(guess, a_follower, b_followers):
    """Take a user and followers count and return if they are right."""
    if a_follower > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
choice_b = random.choice(data)


while game_should_continue:
    choice_a = choice_b
    choice_b = random.choice(data)
    if choice_b == choice_a:
        choice_b = random.choice(data)

    print(f"Compare A: {format_data(choice_a)}")
    print(f"Against B: {format_data(choice_b)}")

    guess = input("Who has more followers: A or B: ").lower()

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear_screen()

    if is_correct:
        score += 1
        print(f"You're right!. Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
