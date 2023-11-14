import pandas as pd

# TODO 1. Create a dictionary in this format:
alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
user_input_using_alphabet = [alphabet_dict.get(c) for c in list(user_input.upper())]
print(user_input_using_alphabet)
