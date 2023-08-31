from user_action_oop import GetUserInput
create = GetUserInput(input("Type 'a' to add item to list\n's' to view your list\n'e' to edit your list\n'x' to "
                                    "exit and view your list\n'r' to remove item from the list\n").strip().lower())
create.show_input()
# ==================================================
class GetUserInput:
    def __init__(self,user_input):
        self.userInput = user_input

    def show_input(self):
        print(self.userInput)