import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header('Day 5: Streamlit: st.write')

st.write('This is a simple example of st.write')



st.write("Numbers:")
st.write(1234)


df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': [10,20,30,40]
})

st.write("Dataframe:")
st.write(df)

# Connection
st.write("Below is a Dataframe", df, "Above is a df" )

#use alt


df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a','b','c']
)

c= alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c']
).interactive()
st.write(c)


st.success('This is a success message')
st.info('This is an info message')
st.warning('This is a warning message')


