listahan = []
while True:
    user_action = input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                        "exit and view your list\n'r' to remove item from the list\n")
    match user_action:
        case 'a':
            item = input('Type an entry\n')
            listahan.append(item.capitalize())
        case 'x':
            print(listahan)
            exit()
        case 's':
            for entry in listahan:
                print(f'{listahan.index(entry)+1}. {entry}')
            print('==============')

        case 'r':
            num_item = int(input('Type the number of the item you want to remove\n'))
            listahan.remove(listahan[num_item-1])
            print(listahan)

        case 'e':
            try:
                for entry in listahan:
                    print(f'{listahan.index(entry)+1}. {entry}')
                to_edit = int(input('Type the number of the item you want to change\n'))
                if to_edit <= len(listahan):
                        edited_item = input('Type the new item\n')
                        listahan[to_edit - 1] = edited_item.capitalize()
                else:
                    print('The item you chose does not exist\nPlease try again.\n')
                    user_action = input("Type 'a' to add item to list\n's' to view your list\n' 'x' to exit and show your list\n'e' to "
                                        "edit your list\n")
            except IndexError:
                print('The item you chose does not exist\nPlease try again.\n')
                user_action = input("Type 'a' to add item to list\n's' to view your list\n' 'x' to exit and show your list\n'e' to "
                                    "edit your list\n")
