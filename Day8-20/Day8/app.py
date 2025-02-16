import streamlit as st

import streamlit as st
import datetime as datetime
from datetime import time, datetime

st.header('Day 8: Streamlit: st.slider')

st.subheader('Slider')

st.subheader("Range slider")

values = st.slider(
    "SElect a range of values",
    0.0, 100.0, (25.0, 75.0)
)
st.write("Values:", values)

st.subheader("AGE")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

start_time = st.slider("When do you start?", time(8, 45), time(12, 30), format="HH/DD/YY - hh:mm")

st.write("Start time:", start_time)


# Select_slider

st.subheader("Select Slider")
st.select_slider('Select a range of values', options=[1,2,3,4,5,6,7,8,9,10])


# Multiselect_slider
st.multiselect('Select a range of values', options=[1,2,3,4,5,6,7,8,9,10])



# Color
st.subheader("Color Picker")
color= st.select_slider("Select a color", 
                        options=[
                            'red', 'orange', 'yellow',
                            'green', 'blue', 'indigo', 'violet']
                        , value=['red', 'green'])
st.write('Selected color:', color)



