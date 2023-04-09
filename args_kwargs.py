# # *args example
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# add(1,2,3)
# print(add(1,2,3))

# # **kwargs example
# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         print(f'key={key}, value={value}')
#
# #     OR
#     print(kwargs['add'])
#     print(kwargs['multiply'])
# calculate(add=3, multiply=5)

# def calc(n, **wagas):
#     n += wagas['add']
#     n *= wagas['multiply']
#     print(n)
# calc(9, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']
my_Car = Car(make='Tesla',model='T')
print(my_Car.make)
print(my_Car.model)
# the code below will produce an error because there is no attribute mileage
# print(my_Car.mileage)

# To avoid returning an error we must use the function get so if there is no attribute, it will only return 'None'.
# We should also note that the attribute should be declared in the self initialization
class Car1:
    def __init__(self, **kw1):
        self.make = kw1.get('make')
        self.model = kw1.get('model')
        self.mileage = kw1.get('mileage')
my_Car1 = Car1(make='Tesla',model='T')
print(my_Car1.mileage)