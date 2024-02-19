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
    
