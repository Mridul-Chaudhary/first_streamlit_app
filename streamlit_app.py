import streamlit
streamlit.title("Mom's diner")
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 poha')
streamlit.text('🥗 upma')
streamlit.text('🐔 omelette')
streamlit.text('🥑🍞 avocado toast')
#streamlit.text()
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
