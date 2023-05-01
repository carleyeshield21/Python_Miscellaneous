import pandas
# iterrows method iterates through each row of a dataframe. this will only work in dataframes, so we must convert first any csv file

PHL_df = pandas.read_csv('PHL_adm1.csv')

# This code will create a dictionary iterating on each row from the dataframe PHL_df that has iterrows method applied to it first
PHL_iterrow = {row.NAME_1:row.TYPE_1 for(index,row) in PHL_df.iterrows()}
print(PHL_iterrow)

# new_dict = {new_key:new_value for (key, value) in dict.items()}
new_dict = {key+'key':value+'value' for (key, value) in PHL_iterrow.items()}
print(new_dict)