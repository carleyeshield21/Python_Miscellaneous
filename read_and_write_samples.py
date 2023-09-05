# Sample of creating and writing in a file
text_file = open('file.txt','w')
text_file.writelines('snail')

# a.txt = I am a.
# b.txt = I am b.
# c.txt = I am c.
list = ['a','b','c']
for letter in list:
    with open(f'{letter}.txt') as file:
        print(file.read())

# Looping through a list of text then creating a text file for each and writing ''Hello" in each file
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for text_file in filenames:
    with open(text_file,'w') as file:
        print('success')
        file.writelines('Hello')

# Adding an item to a list and saving it to the file
# John Smith
# Sen Lakmi
# Sono Octonot
with open('members.txt','r') as members:
    members_list = members.readlines()
    new_member = input('Type the name of the new member\n')
    members_list.append(f'\n{new_member.title()}')
    new_list = open('members.txt','w')
    new_list.writelines(members_list)

# The true meaning of obscurity lies underneath the most delicate structures of viscosity. The idea of changing that balance is obscure by itself.
with open('essay.txt') as file:
    list = file.read().split()
    list2 = [word2.capitalize() for word2 in list]
    print(' '.join(list2))

# The true meaning of obscurity lies underneath the most delicate structures of viscosity. The idea of changing that balance is obscure by itself.
# with open('essay.txt') as file:
#     list = file.read().split()
#     list2 = [word2.capitalize() for word2 in list]
#     str = ' '.join(list2)
#     print(len(str))
#     print(' '.join(list2))
#     print(type(str))

# text_file = open('file.txt','w')
# text_file.writelines('snail')
# with open('file.txt','r') as file:
#     # print(file.read())
#     file2 = file.readlines()
#     print(file2)

# text_file = open('file.txt','w')
# with open('file.txt','r'):
#     with open('file.txt','w'):
#         text_file.writelines('snail')

# with open('essay.txt','r') as file:
#     essay = file.read()
#     print(essay)

# text_file = open('file.txt','w')
# text_file.writelines('snail')
# with open('file.txt')as thefile:
#     print(thefile.read())
# with open('file.txt','r') as file2:
#     f = file2.read()
#     print(f)

try:
    with open('file.txt','r') as file:
        print(file.read())
except FileNotFoundError:
    print('no file')
    with open('file.txt','w') as file:
        file.writelines('snail')
        with open('file.txt','r') as thefile:
            f = thefile.read()
            print(f)