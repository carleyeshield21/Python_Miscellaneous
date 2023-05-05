def bmi_calc():
    weight = float(input('Type in weight in kilograms:\n'))
    height = float(input('Type in height in meters\n'))

    try:
        if height >= 3:
            raise ValueError()
        else:
            bmi = weight / (height ** 2)
            print(f'Your BMI is {bmi}')
    except ValueError:
        print('Height is out of range, please type in a lower height value')
        bmi_calc()

bmi_calc()