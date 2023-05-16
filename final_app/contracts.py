# Import required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st


#load our env file
load_dotenv()

#set w3 variable using getenv. 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))


# Load contracts from the json abi folder

@st.cache(allow_output_mutation=True)
def load_contract_CashToken():
    with open(Path('./abi/CashToken_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_CASH_TOKEN")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

# connect the contract variable to the load_contract function - we will use these in app.py
contract_CashToken = load_contract_CashToken()



def load_contract_AssetNFT():
    with open(Path('./abi/AssetNFT_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_ASSET_NFT")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

# connect the contract variable to the load_contract function - we will use these in app.py
contract_AssetNFT = load_contract_AssetNFT()


'''
def load_contract_FractionalAssetToken():
    with open(Path('./abi/FractionalAssetToken_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_FRACTIONAL_ASSET_TOKEN")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract
# connect the contract variable to the load_contract function
contract_FractionalAssetToken = load_contract_FractionalAssetToken()
'''