# height = float(input('height: '))
# weight =int(input('weight: '))
#
# if height > 3:
#     raise ValueError('Height out of normal range')
#
# bmi = weight/height**2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print('Fruit Pie')
# make_pie(3)

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit Pie')
    else:
        print(fruit + ' pie')
make_pie(3)