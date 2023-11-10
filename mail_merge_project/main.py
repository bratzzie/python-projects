def write_new_letters():
    with open("./Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()

    with open("./Input/Letters/starting_letter.txt") as letter_template_file:
        letter_template = letter_template_file.read()

    for name in names:
        name = name.strip("\n")
        completed_letter = letter_template.replace("[name]", name)
        new_file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")  # alternatively use with open
        new_file.write(completed_letter)
        new_file.close()


write_new_letters()
