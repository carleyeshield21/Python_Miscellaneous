def strength(password):
    pass_list = list(password)
    upper_case = []
    if_int = []
    conditions = []

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


    if not any(conditions) == True:
        return print('Strong Password')
    else:
        return print('Weak Password')

# strength('i7H53IkLk')
# strength('wGbnaUgxdTj')
# strength('G9L1')
# strength('qkvUVw0MrrXaOBBa')
# strength('agofp')
# strength('c7')
strength('paMHjg8h7senPEBmK')