import streamlit as st
import pandas as pd

def dashboard():
    st.write("# Dashboard")

    # Load data into a DataFrame
    data = {
        "Beneficiary": ["Max", "Halam", "Trent", "Andrew"],
        "Amount": [1000, 2000, 1500, 2500]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame in a table
    st.write("## Beneficiary distribution")
    st.table(df)

