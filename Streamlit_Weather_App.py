# import streamlit
# from plotly import express
#
# streamlit.title('Weather-weather four-cast')
# place = streamlit.text_input('Place:',placeholder='Choose a place')
# days = streamlit.slider('Forecast days',min_value=1,max_value=5,help='Tulungan nyo po ako')
# option = streamlit.selectbox('Mamili kang hayup ka',('Temperature','Sky'))
# streamlit.subheader(f'{option} for the next {days} day/s in {place}')
#
# figure = express.line()

import streamlit
import pandas
import math
import matplotlib
import flask

fam_exp = pandas.read_csv('Family Income and Expenditure.csv')
# print(fam_exp)
# column_names = list(fam_exp.columns)
# print(column_names)
rice_exp = fam_exp['Total Rice Expenditure'].values

for index, row in fam_exp.iterrows():
    print(row['Region'])

# print(len(column_names))
# for col in column_names:
#     print(col)

# main_src = fam_exp['Main Source of Income']
# inc_src = [inc for inc in main_src]
# print(inc_src)
# print(len(inc_src))

# 41544

# sample = pandas.read_csv('sample.csv')
# # print(sample)
# # print(type(sample))
# print(sample.columns)
# print(type(sample.columns.values))
# list1 = list(sample.columns)
# print(list1)
# print(type(list1))
#
# print(sample['column1'].values)
# print(sample['column2'].values)
# print(sample['column3'].values)