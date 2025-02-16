import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
     
st.subheader('Detail of items')
st.write("Type of icecream:", type(icecream))
st.write("Icecream:", icecream)
st.write("Type of coffee:", type(coffee))
st.write("Coffee:", coffee)
st.write("Type of cola:", type(cola))
st.write("Cola:", cola)