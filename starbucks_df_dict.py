import pandas
# We must import the pandas module to read the csv file by using pandas.read_csv, this file will automatically become a dataframe, then we can convert it to a dictionary by using the method .to_dict. We then pass in the orient argument then set it to records to have it read line per line in each row
file = pandas.read_csv('python_files/starbucks.csv')
file_to_dict = file.to_dict(orient='records')
# file_to_dict = file.to_dict()

# for temi in file_to_dict:
#     print(f'item: {temi["item"]}')
#     print(f'calories: {temi["calories"]}')
#     print(temi)
#     print('==============')
#     print(type(temi))

# We can create a new dictionary from a dataframe
# new_dict = {row["item"]:row["type"] for(index, row) in file.iterrows()}
# print(new_dict)
# print(len(new_dict))
# print(type(new_dict))

# for key, value in new_dict.items():
#     print(f'{key} : {value}')

# for items in new_dict.items():
#     print(items)
#     print(len(items))

# for each_item in new_dict.items():
#     print(each_item[0])
#     print(each_item[1])

# This code will iterate on each column
# for each in file.items():
#     print(each)

# This will create a dictionary of each item with its fat content
# fat_dict = {row["item"]:row["fat"] for(index, row) in file.iterrows()}
# print(fat_dict)
