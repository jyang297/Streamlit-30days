import streamlit as st

st.write('Button Test')
if st.button(label='Say hello', key=1, help='This is a button to say hello', icon='👋'):
    st.write('Why hello there')
else:
    st.write('Goodbye')