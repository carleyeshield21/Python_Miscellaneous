# first way to create a to do list
num_of_todos1 = int(input('How many to dos for today?\n'))
to_dos = []
for num in range(1, num_of_todos1 + 1):
    item = input(f'Enter to do item number {num}\n')
    to_dos.append(item)
print(to_dos)

# second way to creating a to do list using list comprehension
num_of_todos2 = int(input('How many to dos for today?\n'))
new_list = [input(f'Enter to do item number {num}\n') for num in range(1, num_of_todos2 + 1)]
print(new_list)