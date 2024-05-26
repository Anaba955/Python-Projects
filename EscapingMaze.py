# You can play this game on 'https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json'

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# To avoid infinite loop
while front_is_clear() == True:
    move()
turn_left()

while at_goal()!=True:
    if right_is_clear() == True:
        turn_right()
        move()
    elif wall_in_front() != True:
        move()
    else:
        turn_left()
