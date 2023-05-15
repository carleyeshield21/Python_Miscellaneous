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

# # Lists created from each column of the given csv file converted to dataframe using the method iterrows
# # creating a list from a given data will create a list without discarding repeating items, all will be included in the list
# item_list = [data["item"] for (index,data) in file.iterrows()]
# calories_list = [data["calories"] for (index, data) in file.iterrows()]
# fat_list = [data["fat"] for (index, data) in file.iterrows()]
# carb_list = [data["carb"] for (index, data) in file.iterrows()]
# fiber_list = [data["fiber"] for (index, data) in file.iterrows()]
# protein_list = [data["protein"] for (index, data) in file.iterrows()]
# type_list = [data["type"] for (index, data) in file.iterrows()]
# print(item_list)
# print(len(item_list))
# print(calories_list)
# print(len(calories_list))
# print(fat_list)
# print(len(fat_list))
# print(carb_list)
# print(len(carb_list))
# print(fiber_list)
# print(len(fiber_list))
# print(protein_list)
# print(len(protein_list))
# print(type_list)
# print(len(type_list))

# # when we create a dictionary from a list with repeating items, it will only output a dictionary with unique items and will dicard doubles
# item_dict = {data["item"] for (index,data) in file.iterrows()}
# calories_dict = {data["calories"] for (index, data) in file.iterrows()}
# fat_dict = {data["fat"] for (index, data) in file.iterrows()}
# carb_dict = {data["carb"] for (index, data) in file.iterrows()}
# fiber_dict = {data["fiber"] for (index, data) in file.iterrows()}
# protein_dict = {data["protein"] for (index, data) in file.iterrows()}
# type_dict = {data["type"] for (index, data) in file.iterrows()}
# print(item_dict)
# print(len(item_dict))
# print(carb_dict)
# print(len(carb_dict))
# print(fat_dict)
# print(len(fiber_dict))
# print(carb_dict)
# print(len(carb_dict))
# print(fiber_dict)
# print(len(fiber_dict))
# print(protein_dict)
# print(len(protein_dict))
# print(type_dict)
# print(len(type_dict))

# # birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# # creating a dictionary with a tuple
# item_dict ={(row_data["calories"],row_data["fat"]):row_data["item"] for (index, row_data) in file.iterrows()}
# print(item_dict)
# print(len(item_dict))
#
# # using the for loop below will output the first item as the key and value
# for key, value in item_dict:
#     print(key)
#     print(value)
#     print('=====')
#
# # the for loop below using .items will take the tuple as the key and the item as the value
# for key, value in item_dict.items():
#     print(key)
#     print(value)
#     print('=====')

# # creating a dictionary from the dataframe file with double tuples
# tuple_dict = {(row["item"],row["protein"]):(row["item"],row["carb"]) for (index, row) in file.iterrows()}
