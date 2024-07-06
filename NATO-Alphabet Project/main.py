import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        letter_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, letters in alphabet please.")
        generate_phonetic()
    else:
        print(letter_list)


generate_phonetic()
