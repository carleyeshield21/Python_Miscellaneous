from tkinter import *
password_strength = Tk()
password_strength.title('Password Strength Test')
password_strength.config(padx=50,pady=50)
password_strength.config(background='lightblue')
password_strength.geometry("1300x550+500+300")
strength_canvas = Canvas(password_strength,width=800,height=400)
strength_canvas.grid(row=1,column=1,rowspan=2)
text = strength_canvas.create_text(150,40,text="**Password Remarks",font=('Calibri 18'), fill="black")


def strength():
    import string
    specials = set(string.punctuation)
    new_special = list(specials)
    new_special_chars = ''.join(new_special).strip()
    upper_case = []
    if_int = []
    conditions = []
    special_character = []
    password = password_entry.get()

    # this code is putting the typed password into the label
    new_entry = password_label.config(text=password_entry.get())


    # if length of password is 8 or greater
    if len(password) >= 8:
        conditions.append(True)
    else:
        conditions.append(False)


    # if password contains upper case letter
    for char in password:
        # print(char.isupper())
        if char.isupper():
            upper_case.append(char)
    if len(upper_case) > 0:
        conditions.append(True)
    else:
        conditions.append(False)


    # if password contains a special character
    for char in password:
        # print(char)
        if char in new_special_chars:
            special_character.append(char)
    if len(special_character) > 0:
        conditions.append(True)
    else:
        conditions.append(False)

    # if password contains a number
    for char in password:
        try:
            # print(int(char))
            if_int.append(int(char))
        except ValueError:
            pass

    if len(if_int) > 0:
        conditions.append(True)
    else:
        conditions.append(False)

    print(f'conditions = {conditions}')

    # Testing all conditions if True to test password strength
    if all(conditions) == True:
        return strength_canvas.itemconfig(text,text='Strong Password')
    else:
        return strength_canvas.itemconfig(text,text='Weak Password\n\nPlease check if all the conditions of your '
                                                    'password are met\n\n1. At least 8 characters\n2. Has at least one '
                                                    'upper case letter\n3. Has at least one '
                                                    'number\n4. Has at least one special character',anchor="nw",
                                          fill='darkcyan')


password_label = Label(width=30,font='Roboto 13')
password_label.grid(row=0,column=1)

password_entry = Entry(password_strength,width=30,font='Roboto 15')
password_entry.insert(1,'**Type your password here**')
password_entry.grid(row=1,column=0)

test_passwd = Button(text='Strength Test',font='Roboto 13',command=strength)
test_passwd.grid(row=0,column=0)

password_strength.mainloop()