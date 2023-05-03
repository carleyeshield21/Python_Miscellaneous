import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')

# MY SOLUTION
# nato_iterrows is exactly the same as word_dict, both of these are dictionary
nato_iterrows = {row.letter:row.code for(index,row) in nato.iterrows()}
word_dict = {key:value for (key, value) in nato_iterrows.items()}
print(nato_iterrows)
print(word_dict)
print(nato_iterrows == word_dict)

def my_solution():
    word = input('Type any word\n')
    letters_of_word = [letter.upper() for letter in word]
    try:
        # list_output = [word_dict[n] for  n in letters_of_word]
        list_output = [nato_iterrows[n] for n in letters_of_word]
    except KeyError:
        print('Letters only, no numbers, no punctuation marks, no special characters')
        my_solution()
    else:
        print(list_output)
my_solution()

# dick = {}
# word = input('Type any word\n')
# letters_of_word = word.upper()
# for n in letters_of_word:
#     print(n)
#     for key, value in nato_iterrows.items():
#         if n == key:
#             dick[key]=value
# print(dick)

# dick = {}
# word = input('Type any word\n')
# letters_of_word = word.upper()
# for n in letters_of_word:
#     print(n)
#     for key, value in nato_iterrows.items():
#         if n == key:
#             dick[key]=value
# print(dick)
# MY SOLUTION

# # SOLUTION from Angela Lee
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(type(output_list))
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(output_list)
#
# generate_phonetic()
# # SOLUTION from Angela Lee
