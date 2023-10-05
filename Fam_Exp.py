import streamlit
from plotly import express
import pandas

fam_exp = pandas.read_csv('/home/carleyeshield/PycharmProjects/pythonProjects/Family Income and Expenditure.csv')
rice_exp = fam_exp['Total Rice Expenditure'][:1000]
income = fam_exp['Total Household Income'][:1000]
rice_exp1 = fam_exp['Total Rice Expenditure']
region = fam_exp['Region']
# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
# fig = px.scatter(df,x = "total_bill",y = "tip",color = "sex")
streamlit.header('Family Income and Expenditure Plotting',divider='rainbow')

option = streamlit.selectbox('Mamili kang hayup ka',('Temperature','Sky'))
# select_box = streamlit.selectbox('Choose region',(region))
fig = express.scatter(fam_exp,x = rice_exp,y = income)
fig.update_layout(xaxis_title='Total Rice Expenditure',yaxis_title='Total Household Income')
fig1 = express.scatter(fam_exp,x = rice_exp1,y = region,color='Region')
fig.update_layout(xaxis_title='Total Rice Expenditure',yaxis_title='Region')
streamlit.plotly_chart(fig)
streamlit.plotly_chart(fig1)