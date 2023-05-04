import streamlit as st
import pandas as pd

# Create the layout of the app with three columns
col1, col2, col3 = st.columns(3)

# Add content to the first column
with col1:
    st.write("This is the first column")

# Add content to the third column
with col3:
    st.write("This is the third column")

# Add content to the second column
with col2:
    st.write("This is the second column")
    
    # Add four input widgets to the second column
    input1 = st.text_input("Enter value 1")
    input2 = st.text_input("Enter value 2")
    input3 = st.text_input("Enter value 3")
    input4 = st.text_input("Enter value 4")
