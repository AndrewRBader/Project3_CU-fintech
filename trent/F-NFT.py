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
    with open(Path('./AssetNFT_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract
# connect the contract variable to the load_contract function
contract = load_contract()

def mint_nft(name, assetType, description, price, tokenURI):
    owner = w3.eth.accounts[0]
    tx_hash = contract.functions.tokenizeAsset(
        name,
        assetType, 
        description, 
        price, 
        tokenURI
    ).transact({'from': owner})
    receipt=w3.eth.waitForTransactionReceipt(tx_hash)
    asset_info = contract.functions.getAssetInfo(1).call()
    asset_owner = contract.functions.getOwner(1).call()
    st.write(dict(receipt))
    st.write('Asset Info')
    st.write(asset_info)
    st.write('Owner')
    st.write(asset_owner)

def distribute_fractionalized_tokens(
        token_id, 
        #recipients
    ):
    owner = w3.eth.accounts[0]
    tx_hash = contract.functions.FractionalizeNFT(
        token_id,
        100
    ).transact({'from':owner})
    receipt = w3.eth.getTransactionReceipt(tx_hash)
    events = contract.events.FNFTAddress.createFilter(
        fromBlock=0, argument_filters={'tokenId': 1}
    )
    contact_address = contract.events.FNFTAddress().process_receipt(receipt)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write('New Contact Address')
    st.write(contact_address)

mint_nft('Mona Lisa', 'Artwork', 'LeoD', 100, 'google.com')
distribute_fractionalized_tokens(1)
    
