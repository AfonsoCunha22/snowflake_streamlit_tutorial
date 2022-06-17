import streamlit
import pandas

my_fruits = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Lunch menu')
streamlit.text('🍞 Pão com Chouriço')
streamlit.text('🥣 Bacalhau à Brás')
streamlit.text('🐔 Xacuti')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
