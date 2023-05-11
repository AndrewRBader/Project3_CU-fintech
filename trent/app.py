# Import required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

#load our env file
load_dotenv()

#set w3 variable using getenv. 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#import streamlit libraries 
import streamlit as st
from setup_form import setup_form
from dashboard import dashboard

#make a load_contract that will bring in the json abi file
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./contract_abi.json')) as f:
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
st.title("Register New Asset")
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


# Pinata from module
import requests

# make a dictionary called "file_headers" that has your pinata keys
file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

# return hash of the ipfs
def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    # print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash


'''
# Define the execution tab
def execution():
    st.write("This is the execution tab")

# Define the main function
def main():
    st.set_page_config(page_title="Will Asset Token App")
    st.title("Will Asset Token App")

    # Create a tab menu
    tabs = ["Form to set up", "Dashboard", "Execution"]
    current_tab = st.sidebar.radio("Select a tab", tabs)

    # Display the appropriate tab
    if current_tab == "Form to set up":
        setup_form()
    elif current_tab == "Dashboard":
        dashboard()
    else:
        execution()

# Call the main function to run the app
if __name__ == "__main__":
    main()
'''