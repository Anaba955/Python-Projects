PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)
