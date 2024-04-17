import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#TODO 1. Create a dictionary in this format:
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()
word_list = [data_dict[word] for word in name]
# for word in name:
#     word_list.append(data_dict[word])

print(word_list)

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}


# {"A": "Alfa", "B": "Bravo"}