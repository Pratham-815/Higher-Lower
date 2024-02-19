import random
import os
from game_data import data
from art import logo, vs

def get_random_account():
    """Function to return a random data"""

    return random.choice(data)
