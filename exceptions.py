# FileNotFoundError. This code will result in FileNotFoundError because the a_file.txt does not exist
# with open('a_file.txt') as file:
#     file.read()

# KeyError: An error that results from calling a key in a dictionary that does not exist
# a_dictionary = {'key':'value'}
# value = a_dictionary['non']

# TypeError: An error that results from combining two different data types, an integer can not be combined with a string
# text = 'abc'
# print(5+text)

# Try, Except, Else, Finally(teef)

# Using try and except: This code will return the except statement
# try:
#     file = open('x_file.txt')
# except:
#     print('May error pre')

# Using try and except when file does not exist, then create it
# try:
#     file = open('x_file.txt')
# except:
#     file = open('x_files.txt', 'w')

# The codes below will first write the file because it does not exist yet, once the file has been created and we run the program again, it will then output the message in the  second exception because it will detect that the file already exists
try:
    file = open('x_file.txt')
    a_dictionary = {'key':'value'}
    # print(a_dictionary['spf20'])
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open('x_file.txt','w')
    file.write('Something in the way')
except KeyError as iror:
    print(f'The key {iror} does not exist')
# the else will only execute if there are no detected exceptions, until we change the key value in the dictionary to what actually exists in the dictionary, the else statement will not be executed
else:
    content = file.read()
    print(content)
# the method finally will run no matter if there is an exception or not:
finally:
    file.close()
    print("bahala na kung may error")