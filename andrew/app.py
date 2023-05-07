import streamlit as st
from asset_distribution_form import asset_distribution_form

def main():
    st.title("Asset Distribution Form")

    # Call the component function and store the input values
    input_values = asset_distribution_form()

    # Display the input values as a JSON string
    st.json(input_values)

if __name__ == "__main__":
    main()
