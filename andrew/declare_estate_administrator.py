# importing libraries
import streamlit as st # using for front end framework

# importing file dependencies
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

# Pinata from module
import requests

# prepping imports

#load our env file
load_dotenv()

#set w3 variable 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#make a load_contract that will bring in the json abi file
@st.cache(allow_output_mutation=True)
def load_contract():
    path = Path('contract_abi.json')
    with open(path) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract
# connect the contract variable to the load_contract function
contract = load_contract()

# NFT registration
st.title("Register New NFT")
accounts = w3.eth.accounts
address = st.selectbox("Select NFT Owner", options=accounts)
nft_uri = st.text_input("The URI to the asset")

if st.button("Register Asset"):
    tx_hash = contract.functions.tokenizeAsset("name", "assetType", "description", 4, nft_uri).transact({
        "from": address,
        "gas": 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

################################################################################
# Declare Estate Administrator 
################################################################################
st.markdown("## Declare Estate Administrator")

# Create a select box containing a list of available accounts for the user to choose from
estate_admin = st.selectbox("Select Estate Administrator", options=accounts)
# "Declare Estate Administrator" button to call the smart contract function
if st.button("Declare Estate Administrator"):
    # Call the `declareEstateAdministrator` function with the selected estate administrator address as the argument
    tx_hash = contract.functions.declareEstateAdministrator(estate_admin).transact({'from': address, 'gas': 1000000})
    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    # catch if fails
    if contract.functions.estateAdministrators(estate_admin).call() == True:
        st.write(f"{estate_admin} has been declared as an estate administrator")
    else:
        st.write(f"Failed to declare {estate_admin} as an estate administrator")
