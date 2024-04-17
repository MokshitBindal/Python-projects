import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)


def nato():
    name = input("Enter your name:").upper()
    try:
        word_list = [data_dict[word] for word in name]
    except KeyError:
        print("Sorry, only letters in alphabets please!\n")
        nato()
    else:
        print(word_list)

nato()
