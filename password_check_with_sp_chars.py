def strength():
    import string
    password = input('Type in your password to test its strength\n')
    pass_list = list(password)
    specials = set(string.punctuation)
    new_special = list(specials)
    new_special_chars = ''.join(new_special).strip()
    upper_case = []
    if_int = []
    conditions = []
    special_character = []

    for char in password:
        if char in new_special_chars:
            special_character.append(char)


    if len(pass_list) >= 8:
        conditions.append(False)
    else:
        conditions.append(True)


    for char in pass_list:
        upper_case.append(char.isupper())
        try:
            int(char)
            if_int.append(True)
        except ValueError:
            if_int.append(False)


    if not any(if_int) == False:
        conditions.append(False)
    else:
        conditions.append(True)

    if not any(upper_case) == False:
        conditions.append(False)
    else:
        conditions.append(True)


    if not any(conditions) == True and len(special_character) > 0:
        return print('Strong Password')
    else:
        return print('Weak Password')

strength()
# strength('i7H53IkL(')
# strength('wGbnaUgxdTj')
# strength('G9L1')
# strength('qkvUVw0MrrXaOBBa')
# strength('agofp')
# strength('c7')
# strength('paMHjg8h7senPEBmK')
