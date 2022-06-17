import streamlit
import pandas

my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Lunch menu')
streamlit.text('🍞 Pão com Chouriço')
streamlit.text('🥣 Bacalhau à Brás')
streamlit.text('🐔 Xacuti')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_select = streamlit.multiselect('Pick some fruits:', list(my_fruits_list.index), ['Avocado', 'Strawberries'])
my_fruits_to_show = my_fruits_list.loc[fruits_select]
streamlit.dataframe(my_fruits_to_show)
