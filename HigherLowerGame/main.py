import random
import os
from art import logo, vs
from game_data import data


def get_random_account():
    """Returns a random account"""
    return random.choice(data)

# Format account data into printable format.
def printFormat(account):
    """Takes account and returns the printable format"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"
    
def check_answer(guess, follower_a, follower_b):
    """Compare followers against user's guess and return True if they're right else False"""
    if follower_a > follower_b:
        return guess == "a"
    if follower_a < follower_b:
        return guess == "b"
    

print(logo)
score = 0
game_should_continue = True
account_b = get_random_account()

while game_should_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
        account_b = get_random_account()
    
    print(f"Compare A: {printFormat(account_a)}")
    print(vs)
    print(f"Against B: {printFormat(account_b)}")
    
    # Ask user for a guess.
    guess = input("Who has mor followers? Type 'A' or 'B' ").lower()
    
    # Check if user is correct.
    ## Get follower count.
    account_a_count = account_a["follower_count"]
    account_b_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, account_a_count, account_b_count)
    
    os.system("clear")
    print(logo)
    
    # Feedback.
    if is_correct:
        score += 1
        print(f"You got it right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
