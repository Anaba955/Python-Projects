import os
from art import logo

print(logo)

track = {}
more = 'yes'
max = 0
winner = ""
while more == 'yes':
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    track[name] = bid
    if bid > max:
        max = bid
        winner = name
    more = input("Are there any other bidders? 'yes' or 'no' ").lower()
    if more == 'yes':
        os.system('clear')
print(f"The winner is {winner} with a bid of ${max}")
    
