import streamlit as st
import pandas as pd
import time

def get_user_name():
    return 'John'

st.header("Echo Function: ")
with st.echo():
    # ----------------------------------------
    # Want people to see this part of code...
        # Everything inside this block will be both printed to the screen and executed.

    def get_perctuation():
        return '!!!'

    greeting = "Hi three, "
    user_name = get_user_name()
    puntuation = get_perctuation()

    st.write(greeting,user_name,puntuation)

    # ...up to here
    # ----------------------------------------

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Done!')

st.error('This is an error')

st.warning('This is a warning')

st.info('This is a purely informational message')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

my_placeholder = st.empty()

# Now replace the placeholder with some text:
my_placeholder.text("Hello world!")

st.help(pd.DataFrame)

x = get_user_name()
st.help(x)