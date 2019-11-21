import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My First app')

st.header('First DataFrame: ')
st.write("Here's out first attemp at using data to create to table:")
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

df

st.write("Here's out first attemp at using data to create to maps:")
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns = ['lat','lon']
)

st.map(map_data)

st.header("Checkbox: ")

if st.checkbox('Show dataframe?'):
    st.write("Here's out first attemp at using data to create to chart line:")
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c']
    )

    st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You Selected: ', option

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'...and now we\'re done!'

st.markdown(' Streamlit is **_really_ cool**.')

st.header('Code example: ')

code = ''' <html>
    <body>
        <title>Hello World</title>
        <meta charset="UTF-8">
   </body>
   <head>
        <h1>Hello Example!</h1>
        <br>
        <p>Hello world</p>
    </head>
</html>'''
st.code(code,language='html')

with st.echo():
    st.write('This code will be printed')