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

# Pinata for interacting with IPFS network

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




################################################################################
# declaring estate administrator 
################################################################################
st.markdown("## Declare Estate Administrator")



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

