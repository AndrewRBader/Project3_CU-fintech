# Import required libraries
import os
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

#load our env file
load_dotenv()

#set w3 variable using getenv. 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# import contracts from contracts.py
from contracts import contract_AssetNFT


######################################################################################
st.title("Asset Registry")
accounts = w3.eth.accounts
address = w3.eth.accounts[0] 
st.markdown("---")

################################################################################
# Register Cash
################################################################################
st.markdown("## Register Cash Distribution")

if 'payment_list' not in st.session_state:
    st.session_state.payment_list = []

recipient_address = st.text_input("Enter recipient address:")
amount = st.number_input("Enter amount:")

if st.button("Register"):
    payment = {'recipient_address': recipient_address, 'amount': amount}
    st.session_state.payment_list.append(payment)

st.write(st.session_state.payment_list)

################################################################################
# Register New Asset, require name, type, price, details (+ document --> optional)
################################################################################

st.markdown("## Register New Asset")
nft_name = st.text_input("Enter the name of the asset")
nft_type = st.text_input("Enter the asset type")
price = st.text_input("Enter the value/price of your asset")
details = st.text_input("Enter any details you have")
nft_uri = "N/A"
if st.button("Register Asset"):
    tx_hash = contract_AssetNFT.functions.tokenizeAsset(
        nft_name,
        nft_type,
        details,
        int(price),
        nft_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")

################################################################################
# Declare Estate Administrator 
################################################################################
st.markdown("## Declare Estate Administrator")

# Create a select box containing a list of available accounts for the user to choose from
estate_admin = st.selectbox("Select Estate Administrator", options=accounts)
# "Declare Estate Administrator" button to call the smart contract function
if st.button("Declare Estate Administrator"):
    # Call the `declareEstateAdministrator` function with the selected estate administrator address as the argument
    tx_hash = contract_estate_admin.functions.declareEstateAdministrator(estate_admin).transact({
        'from': address, 
        'gas': 1000000})
    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    # catch if fails
    if contract_estate_admin.functions.estateAdministrators(estate_admin).call() == True:
        st.write(f"{estate_admin} has been declared as an estate administrator")
    else:
        st.write(f"Failed to declare {estate_admin} as an estate administrator")

