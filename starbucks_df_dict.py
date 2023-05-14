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

# Lists created from each column of the given csv file converted to dataframe using the method iterrows
calories_list = [data["calories"] for (index, data) in file.iterrows()]
item_list = [data["item"] for (index,data) in file.iterrows()]
fat_list = [data["fat"] for (index, data) in file.iterrows()]
carb_list = [data["carb"] for (index, data) in file.iterrows()]
fiber_list = [data["fiber"] for (index, data) in file.iterrows()]
protein_list = [data["protein"] for (index, data) in file.iterrows()]
type_list = [data["type"] for (index, data) in file.iterrows()]
print(item_list)
print(calories_list)
print(fat_list)
print(carb_list)
print(fiber_list)
print(protein_list)
print(type_list)

# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
