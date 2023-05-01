import string
import random

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)
symbols = ['~', ':','+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
# In the num_list, we must convert the new item 'num' into a string so we can use it later in the join method, we can not use join for any numerical value, only strings
num_list = [str(num) for num in range(0,10)]

alpha_lower_choice = [random.choice(alpha_lower) for low in range(5)]
alpha_upper_choice = [random.choice(alpha_upper) for upper in range(5)]
symbols_choice = [random.choice(symbols) for sym in range(random.randint(5,8))]
numbers_choice = [random.choice(num_list) for num in range(5)]

string_gen = alpha_lower_choice+alpha_upper_choice+symbols_choice+numbers_choice
random.shuffle(string_gen)
password = ''.join(string_gen)
print(password)