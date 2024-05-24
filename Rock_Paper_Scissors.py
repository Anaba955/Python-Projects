import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
game_state = [rock, paper, scissors]

if user_choice > 2 or user_choice < 0:
    print("Its an invalid number, you lose")
else:
    print(game_state[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer choose:")
    print(game_state[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You won!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You won!")
    elif computer_choice > user_choice:
        print("You lose")
    else:
        print("Its a draw")
