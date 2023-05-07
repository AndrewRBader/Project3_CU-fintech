import streamlit as st

def asset_distribution_form():
    # Form inputs
    name = st.text_input("Your full name:")
    date_of_birth = st.date_input("Date of birth:")
    place_of_birth = st.text_input("Place of birth:")
    marital_status = st.selectbox("Marital status:", ["Married", "Single", "Divorced"])
    spouse_name = st.text_input("Spouse's full name (if applicable):")
    children_names = st.text_input("Names of children (if applicable):")
    executor_name = st.text_input("Executor's full name:")
    beneficiary_names = st.text_input("Names of beneficiaries:")

    # Asset inputs
    bank_accounts = st.number_input("Total amount in bank accounts:")
    real_estate = st.number_input("Total value of real estate owned:")
    investments = st.number_input("Total value of investments:")
    personal_property = st.number_input("Total value of personal property (e.g. vehicles, furniture):")
    other_assets = st.number_input("Total value of any other assets:")

    # Return input values as a dictionary
    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "marital_status": marital_status,
        "spouse_name": spouse_name,
        "children_names": children_names,
        "executor_name": executor_name,
        "beneficiary_names": beneficiary_names,
        "bank_accounts": bank_accounts,
        "real_estate": real_estate,
        "investments": investments,
        "personal_property": personal_property,
        "other_assets": other_assets
    }
