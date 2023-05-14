# Import required libraries
import os
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from setup_form import setup_form
from dashboard import dashboard

#load our env file
load_dotenv()

#set w3 variable using getenv. 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Import necessary definitions from pinata.py
from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json, pin_nft

# import contracts from contracts.py
from contracts import contract_CashToken, contract_AssetNFT


######################################################################################
st.title("Asset Registry")
st.write("Choose your account")
accounts = w3.eth.accounts
address = w3.eth.accounts[0] 
st.markdown("---")

################################################################################
# Register New Asset, require name, type, price, details (+ document --> optional)
################################################################################

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
    if upload_choice == "yes":
        st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
        st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{nft_ipfs_hash})")

st.markdown("---")

################################################################################
# Register Cash
################################################################################

st.markdown("## Register Cash") 
total_cash_amount = st.text_input("Enter the amount of total cash")
if st.button("Register Cash"):
    tx_hash = contract_CashToken.functions._mint(total_cash_amount).transact()
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
