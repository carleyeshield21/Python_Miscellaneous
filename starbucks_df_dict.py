import pandas

file = pandas.read_csv('python_files/starbucks.csv')
file_to_dict = file.to_dict(orient='records')
# file_to_dict = file.to_dict()

for temi in file_to_dict:
    print(f'item: {temi["item"]}')
    print(f'calories: {temi["calories"]}')
    print('==============')
    # print(type(temi))

# for every_item in file_to_dict:
#     print(f'{every_item["item"]}:{every_item["calories"]}')

# nato_iterrows = {row.letter:row.code for(index,row) in nato.iterrows()}
# {new_key:new_value for(index, row) in df.iterrows()}