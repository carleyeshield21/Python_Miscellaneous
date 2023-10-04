import streamlit
from plotly import express
import pandas

fam_exp = pandas.read_csv('/home/carleyeshield/PycharmProjects/pythonProjects/Family Income and Expenditure.csv')
streamlit.title('Weather-weather four-cast')
place = streamlit.text_input('Place:',placeholder='Choose a place')
days = streamlit.slider('Forecast days',min_value=1,max_value=5,help='Tulungan nyo po ako')
option = streamlit.selectbox('Mamili kang hayup ka',('Temperature','Sky'))
streamlit.subheader(f'{option} for the next {days} day/s in {place}')

total_rice_exp = fam_exp['Total Rice Expenditure'][:20]
total_household_income = fam_exp['Total Food Expenditure'][:20]
print(total_rice_exp)
print(total_household_income)


figure = express.line(x=total_household_income,y=total_rice_exp,labels={'x':' Computer',
                                                                        'y':'5 yr olds'})

streamlit.plotly_chart(figure)