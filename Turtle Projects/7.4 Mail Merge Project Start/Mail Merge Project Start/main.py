
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    name = names_file.readlines()
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for i in name:
        strippedletter = i.strip()
        new_letter=letter.replace(PLACEHOLDER,strippedletter)
        with open(f"./Output/ReadyToSend/letter_for{strippedletter}.txt",mode="w") as files:
            files.write(new_letter)
        
       
        