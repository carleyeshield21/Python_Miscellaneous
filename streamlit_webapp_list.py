# The method strip is very useful so that the items in a list will have a break line in the text file
import streamlit

streamlit.title('WibbApp')
streamlit.subheader('Web App List')
streamlit.write('Gumawa ka na ng listahan')

def add_item():
    added_item = streamlit.session_state['new_item']
    with open('file.txt', 'r') as file:
        # important to add the \n to create a breakline for a separate item
        file1 = file.readlines()
        file1.append(added_item + '\n')
        file = open('file.txt','w')
        file.writelines(file1)
        # streamlit.session_state.
# if 'something' not in st.session_state:
#     st.session_state.something = ''
#
# def submit():
#     st.session_state.something = st.session_state.widget
#     st.session_state.widget = ''
#
# st.text_input('Something', key='widget', on_change=submit)
#
# st.write(f'Last submission: {st.session_state.something}')


streamlit.text_input(label='Mag type ka dito ng entry mo',placeholder='Type entry here',on_change=add_item,key='new_item')
streamlit.button(label='Add entry')

streamlit.session_state

try:
    with open('file.txt', 'r') as new_file_list:
        for item in new_file_list:
            streamlit.checkbox(item.strip())
        # pass
except FileNotFoundError:
    print('A file text will be created')
    with open('file.txt','w'):
        pass


# new_item = input('Add a new item\n').strip() + '\n'
# with open('file.txt','r') as file_list:
#     new_file_list = file_list.readlines()
#     new_file_list.append(new_item)
#     file_list = open('file.txt','w')
#     file_list.writelines(new_file_list)