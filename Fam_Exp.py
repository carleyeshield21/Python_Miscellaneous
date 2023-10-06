import streamlit
from plotly import express
import pandas

streamlit.header('Family Income and Expenditure Plotting',divider='rainbow')

fam_exp = pandas.read_csv('/home/carleyeshield/PycharmProjects/pythonProjects/Family Income and Expenditure.csv')
rice_exp = fam_exp['Total Rice Expenditure'][:1000]
income = fam_exp['Total Household Income'][:1000]
rice_exp1 = fam_exp['Total Rice Expenditure']
region = fam_exp['Region']
set_region = set(fam_exp['Region'])

region_selection = streamlit.selectbox('Choose region', (set_region))
print(f'Region selected: {region_selection}')
column = streamlit.selectbox('Select category', (fam_exp.columns))
print(f'Column selected: {column}')

# least = list(fam_exp[column])

per_region_list = [index for index, rehiyon in enumerate(region) if rehiyon == region_selection]
print(per_region_list)
column_list = fam_exp[column]


region_column_list = [column_list[item] for item in per_region_list]
print(region_column_list)
print(len(region_column_list))
haysto = express.histogram(region_column_list)
streamlit.plotly_chart(haysto)

# fig = express.scatter(fam_exp,x = rice_exp,y = income)
# fig.update_layout(xaxis_title='Total Rice Expenditure',yaxis_title='Total Household Income')
# fig1 = express.scatter(fam_exp,x = rice_exp1,y = region,color='Region')
# fig.update_layout(xaxis_title='Total Rice Expenditure',yaxis_title='Region')
# streamlit.plotly_chart(fig)
# streamlit.plotly_chart(fig1)
#
# # Pie Plot
# pie_plot = express.pie(values=fam_exp['Total Rice Expenditure'],names=fam_exp['Region'])
# streamlit.plotly_chart(pie_plot)


# lees = ['Car','jeep','tri','Car','Car']
# for index, item in enumerate(lees):
#     print(index, item)
# newlees = [index for index, item in enumerate(lees) if item == 'Car']
# print(newlees)
