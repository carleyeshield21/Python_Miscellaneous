# with open('file1.txt') as f1:
#     f1_list = f1.readlines()
# print(f1_list)
# print(type(f1_list))
# for f1_item in f1_list:
#     f1_int = int(f1_item)
#     print(f1_int)
#     print(type(f1_int))
#
# with open('file2.txt') as f2:
#     f2_list = f2.readlines()
#
# # new_list = [new_item for item in list]
# same_nums = [int(x) for x in f1_list if x in f2_list]
# print(same_nums)

# samp_list = [1,2,3,4,5]
# new_list = [new_item for item in list]
# new_list = [samp for samp in samp_list]

# list = [1,2,3,4]
# new_list = [item + 3.1415 for item in list]
# print(new_list)
#
# name = 'Carl'
# new2 = [letter for letter in name]
# print(new2)

# range_list = [new_item for item in list]
# range_list = [num2 for num in range(1,5)]
# print(range_list)

# Python List Comprehension with condition
# newer_list = [new_item for item in list if test]
# list = [1,2,3,4,5]
# phonetic_equivalent = [num for num in list if num%2 == 1]
# print(phonetic_equivalent)

# numbers =[1,1,2,3,5,8,13,21,34,55]
# # phonetic_equivalent = [new_item for item in list]
# sq_nums = [num*num for num in numbers]
# print(sq_nums)
#
# evens = [num for num in numbers if num%2==0]
# print(evens)

# # LIST COMPREHENSION SYNTAX
# Python List Comprehension
# new_list = [new_item for item in list]
# Python List Comprehension with condition
# newer_list = [new_item for item in list if test]
# Dictionary Comprehension
# Keyword pattern
# new_dict = {new_key:new_value for item in list}
# Dictionary based on another dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# With if condition
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# import random
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# # syntax pattern
# # new_dict = {new_key:new_value for item in list}
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# print(type(student_scores))
#
# # passed_students = {new_key:new_value for (key,value) in dictionary.items()}
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# split_sentence = sentence.split()
# print(split_sentence)
# print(len(split_sentence))
# print(type(split_sentence))
# result = {word:len(word) for word in split_sentence}
# print(result)

# Dictionary with temperature conversion
# (temp_c * 9/5) + 32 = temp_f
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # new_dict = {new_key:new_value for(key,value) in dict.items()}
# sample = {day:fahrenheit_temp for (day, fahrenheit_temp) in weather_c.items() if fahrenheit_temp >= 20}
# print(sample)
# # weather_f = {new_key:new_value for(key,value) in weather_c.items()}
# weather_f = {day:(((celsius_temp*9/5))+32) for(day,celsius_temp) in weather_c.items()}
# print(weather_f)

# Iterating over Pandas Data Frame
# student_dict = {
#     'student': ['Angela','James','Lily'],
#     'score': [56,76,98]
# }
# looping through a dictionary
# for (key, value) in dict.items():
#     print(key)
#     print(value)

# for (key, value) in student_dict.items():
    # print(value)

# import pandas
# student_df = pandas.DataFrame(student_dict)
# print(student_df)
#
# for(index,row) in student_df.iterrows():
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     if row.student == 'Angela':
#         print(row.student, row.score)

# Creating a dictionary using iterrows() method
import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(type(nato))
# print(nato)
#
# nato_dict = nato.to_dict()
# print(nato_dict)

# for(index,row) in student_df.iterrows():
# for (index, row) in nato.iterrows():
#     # print(row.letter)
#     print(row.code)

# new_dict = {new_key:new_value for(key,value) in dict.items()}
# {new_key:new_value for(index, row) in df.iterrows()}
nato_iterrows = {row.letter:row.code for(index,row) in nato.iterrows()}
print(nato_iterrows)
# print(nato_iterrows.values())
# print(nato_iterrows.keys())
# print(type(nato_iterrows.keys()))
# print(type(nato_iterrows))
nato_iterrows_key_list = [value for value in nato_iterrows.keys()]
nato_iterrows_values_list = [value for value in nato_iterrows.values()]
# print(nato_iterrows_key_list)
# print(nato_iterrows_values_list)
dict_keys_to_list = list(nato_iterrows.keys())
dict_values_to_list = list(nato_iterrows.values())
# print(dict_keys_to_list)
# print(dict_values_to_list)
# print(type(dict_keys_to_list))
# print(type(dict_values_to_list))

word = input('Type any word\n\n')
letters_of_word = [letter.upper() for letter in word]
print(letters_of_word)
print(type(letters_of_word))

# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# This will output the correct dictionary but in the order of the letters in the word input
word_dict = {key:value for (key, value) in nato_iterrows.items() if key in letters_of_word}
print(word_dict)

# word_dict2 = {letter:new_value for letter in letters_of_word if letter in dict_values_to_list}

# for let in letters_of_word:
#     if let in dict_keys_to_list:
#         print(dict_keys_to_list.index(let))
#         print(dict_values_to_list[dict_keys_to_list.index(let)])

dick = {}
for n in letters_of_word:
    for key, value in nato_iterrows.items():
        if n == key:
            dick[key]=value
print(dick)
print(type(dick))

# word_dict = {letter:new_value for letter in letters_of_word}
# print(word_dict)
# # LIST COMPREHENSION SYNTAX
# Python List Comprehension
# new_list = [new_item for item in list]
# Python List Comprehension with condition
# newer_list = [new_item for item in list if test]
# Dictionary Comprehension
# Keyword pattern
# new_dict = {new_key:new_value for item in list}
# Dictionary based on another dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# With if condition
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# Using continue method in a while loop
lisht = [1,'a','b',3]
counter = 0
while True:
    try:
        index = int(input('Input an index\n'))
        print(lisht[index])
        break
    except IndexError:
        counter += 1
        print(f'{5-counter} tries remaining')
        if counter == 5:
            print('You have reached the maximum number of tries')
            exit()
        else:
            continue
