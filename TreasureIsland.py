# You can find more such figures on ASCII Art
# HAVE FUN!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You find yourself at the edge of a dense jungle, where the path splits into two directions. Do you want to go 'left' into the dark, twisted trees or 'right' towards the sunny, open trail? ").lower()
if direction == 'left':
    choice = input("You carefully navigate through the jungle and come across a wide, fast-flowing river. Do you want to 'swim' across or 'wait' for a better opportunity? ").lower()
    if choice == 'wait':
        door = input("As you wait, you discover a hidden path that leads to three ancient doors, each a different color. Which color do you choose: 'red', 'blue', or 'yellow'? ").lower()
        if door == 'yellow':
            print("You push open the yellow door and find a room filled with gold and jewels. Congratulations, you found the treasure!")
        elif door == 'red':
            print("As you open the red door, flames burst out and engulf you. Burned by fire. Game over!")
        elif door == 'blue':
            print("The blue door creaks open to reveal a pack of hungry beasts that leap out and attack you. Eaten by beasts. Game over!")
        else:
            print("You hesitate too long, and the doors slam shut, trapping you forever. Game over!")
    else:
        print("You dive into the river, but the current is too strong. You're swept away and attacked by a school of hungry trouts. Game over!")
else:
    print("You stroll down the sunny path, but it suddenly collapses under your feet. You fall into a hidden pit. Game over!")
