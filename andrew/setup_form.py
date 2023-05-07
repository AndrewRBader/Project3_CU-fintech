import streamlit as st

def setup_form():
    st.write("# Setup Form")

    # Define input fields for the form
    total_assets = st.number_input("Total assets value")
    num_beneficiaries = st.number_input("Number of beneficiaries", min_value=1, step=1)
    executor_name = st.text_input("Executor's name")
    executor_email = st.text_input("Executor's email")

    # Define a dictionary to hold the form data
    form_data = {
        "total_assets": total_assets,
        "num_beneficiaries": num_beneficiaries,
        "executor_name": executor_name,
        "executor_email": executor_email
    }

    # Add a submit button to the form
    if st.button("Submit"):
        st.write(form_data)
