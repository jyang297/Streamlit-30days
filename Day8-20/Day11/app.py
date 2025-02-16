import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
st.write("Type of options:", type(options))


select_number = st.multiselect(
    'Select a number',
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [3, 4, 5]
)

st.write('You selected:', select_number)
sum = sum(select_number)

st.write('Sum of selected numbers:', sum)