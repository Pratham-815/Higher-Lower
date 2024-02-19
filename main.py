import random
import os
from game_data import data
from art import logo, vs

def get_random_account():
    """Function to return a random data"""

    return random.choice(data)


def format_data(account):
    """Function to format account data into printable format"""

    name = account['name']
    description = account['description']
    country = account['country']
    print(f"{name}, a {description}, from {country}")


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right.Or False if they got it wrong."""

    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more follwers ? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls')

        print(logo)
        
        if is_correct:
            score += 1
            print(f"You are right...Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry...That's wrong...Final score: {score}")
        

game()