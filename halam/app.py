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


# Import libraries needed for Pinata functions
import requests
from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

# make a dictionary called "file_headers" that has your pinata keys
file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

# This is for those who'd like to upload files such as deeds. 
def pin_nft(nft_name, nft_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(nft_file.getvalue())

    # Build a token metadata file for the artwork
    token_json = {
        "name": nft_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash

st.title("Asset Registry")
st.write("Choose your account")
accounts = w3.eth.accounts
address = w3.eth.accounts[0] 
st.markdown("---")

################################################################################
# Register New Asset 
################################################################################
# require name, type, price, details (+ document which will be optional)

st.markdown("## Register New Asset")
nft_name = st.text_input("Enter the name of the asset")
nft_type = st.text_input("Enter the asset type")
price = st.text_input("Enter the value/price of your asset")
details = st.text_input("Enter any details you have")
upload_choice = st.selectbox("Upload doc (optional)", options = ("yes", "no"))
if upload_choice == "yes":
    nft_doc = st.file_uploader("Upload Your Document", type=["jpg", "jpeg", "png", "pdf"])
    nft_ipfs_hash = pin_nft(nft_name, nft_doc)
    nft_uri = f"ipfs://{nft_ipfs_hash}"
else: 
    nft_uri = "N/A"
if st.button("Register Asset"):
    tx_hash = contract.functions.tokenizeAsset(
        nft_name,
        nft_type,
        details,
        int(price),
        nft_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    # st.write(contract.functions.estateAssets(1).call()) THIS DOESNT WORK YET
    if upload_choice == "yes":
        st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
        st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{nft_ipfs_hash})")

st.markdown("---")

################################################################################
# Register Cash
################################################################################
'''
st.markdown("## Register Cash") 
total_cash_amount = st.text_input("Enter the amount of total cash")
if st.button("Register Cash"):
    tx_hash = contract.functions._mint(total_cash_amount).transact()
'''

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