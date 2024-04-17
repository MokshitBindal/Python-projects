#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_path = "./Input/Letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"
final_path = "./Output/ReadyToSend"

with open(letter_path) as f:
    letter = f.read()
    # print(letter)

with open(names_path) as f:
    names = f.readlines()
    
letter_names = []
# for name in names:
#     name.strip()
#     letter_names.append(name)

# print(letter_names)
    
for name in names:
    final_letter = letter.replace("[name]", name.strip())
    letter_names.append(final_letter)

# print(letter_names[1])

for name in names:
    with open(f"{final_path}/letter_for_{name}", mode="w") as f:
        f.write(letter_names[names.index(name)])