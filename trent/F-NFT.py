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
w3.eth.defaultAccount = w3.eth.accounts[0]

#import streamlit libraries 
import streamlit as st
from setup_form import setup_form
from dashboard import dashboard


#make a load_contract that will bring in the json abi file
#@st.cache(allow_output_mutation=True)
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

token_ids = []

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
    events_filter = contract.events.NFTTokenId.createFilter(
        fromBlock='latest'
    )
    events = events_filter.get_all_entries()
    for event in events:
        event_dictionary = dict(event)
        token_ids.append(event_dictionary['args']['tokenId'])
        st.write('Event Log')
        st.write(event_dictionary)
        st.write('Token ID')
        st.write(token_ids[-1])
    # asset_info = contract.functions.getAssetInfo(1).call()
    # asset_owner = contract.functions.getOwner(1).call()
    # st.write(dict(receipt))
    # st.write('Asset Info')
    # st.write(asset_info)
    # st.write('Owner')
    # st.write(asset_owner)
contract_addresses = []

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
    events_filter = contract.events.FNFTAddress.createFilter(
        fromBlock='latest', argument_filters={'tokenId': token_ids[-1]}
    )
    events = events_filter.get_all_entries()
    for event in events:
        event_dictionary = dict(event)
        contract_addresses.append(event_dictionary['args']['contractAddress'])
        st.write('Event Log')
        st.write(event_dictionary)
        st.write('Contract Address')
        st.write(contract_addresses[-1])
    with open(Path('./FractionalAssetToken_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = f"{contract_addresses[-1]}"

    fractional_token_contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    balance = fractional_token_contract.functions.getBalance(owner).call()
    st.write('Balance')
    st.write(balance)

    #contact_address = contract.events.FNFTAddress().process_receipt(receipt)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write()

def deploy_cash_token(address):
    with open(Path('./FractionalAssetToken.json')) as f:
        contract_abi = json.load(f)

    contract_address = f"{contract_addresses[-1]}"

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract
    




mint_nft('Mona Lisa', 'Artwork', 'LeoD', 100, 'google.com')
distribute_fractionalized_tokens(token_ids[-1])
    


