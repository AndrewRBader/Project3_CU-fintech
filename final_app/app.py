# Import required libraries
import os
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import json

#load our env file
load_dotenv()

#set w3 variable using getenv. 
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))


#make a load_contract that will bring in the json abi file
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./abi/AssetNFT_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

# connect the contract variable to the load_contract function
contract = load_contract()




################################################################################
############################ STREAMLIT #########################################
################################################################################

st.title("Asset Registry")
# Retrieve the list of accounts from the Ethereum network
accounts = w3.eth.accounts
# Select the first account 
address = accounts[0] 
st.markdown("---")

################################################################################
# Register Cash
################################################################################

# Display a markdown header
st.markdown("## Register Cash Distribution")

# Check if 'payment_list' key exists in session state, if not, initialize it as an empty list
if 'payment_list' not in st.session_state:
    st.session_state.payment_list = []

# Gather user input
recipient_address = st.text_input("Enter recipient address:")
amount = st.number_input("Enter amount:")

if st.button("Register"):
    # Create a dictionary with the recipient address and amount
    payment = {'recipient_address': recipient_address, 'amount': amount}
    # Append the payment dictionary to the 'payment_list' in session state
    st.session_state.payment_list.append(payment)

# Retrieve the 'payment_list' from session state
cash_list = st.session_state.payment_list

# Display the 'cash_list'
st.write(cash_list)

################################################################################
# Register New Asset, require name, type, price, details 
################################################################################

# Initialize asset_list in st.session_state
if 'asset_list' not in st.session_state:
    st.session_state.asset_list = []

# Gather information from user
st.markdown("## Register New Asset")
nft_name = st.text_input("Enter the name of the asset")
nft_type = st.text_input("Enter the asset type")
price = st.text_input("Enter the value/price of your asset")
details = st.text_input("Enter any details you have")
nft_uri = "N/A"
nft_recipient_address = st.text_input("Enter the Ethereum address of the inheritor")

if st.button("Register Asset"):
    # Execute the transaction minting an NFT to the User's account.
    tx_hash = contract.functions.tokenizeAsset(
        nft_name,
        nft_type, 
        details, 
        int(price), 
        nft_uri
    ).transact({'from': address})
    receipt=w3.eth.waitForTransactionReceipt(tx_hash)

    # Create an event to access the token ID of the newly minted nft
    events_filter = contract.events.NFTTokenId.createFilter(
        fromBlock='latest'
    )
    events = events_filter.get_all_entries()
    for event in events:
        event_dictionary = dict(event)
        # Access the token ID
        nft_transfer = {'nft_recipient_address': nft_recipient_address, 'token_id': event_dictionary['args']['tokenId']}
        # Add the token ID mapped to the account it will be
        # sent to upon execution of the will.
        st.session_state.asset_list.append(nft_transfer)
        # Print out the token id of the newly minted nft along
        # along with the account it will be sent to.
        st.write('Event Log')
        st.write(event_dictionary)
        st.write('Token ID')
        st.write(st.session_state.asset_list)
# Save the list of token IDs mapped to accounts
# for use later upon execution of the will.
asset_list = st.session_state.asset_list
st.markdown("---")


################################################################################
# Execution
################################################################################

# Set the sender as the person who wrote the will
sender = address
# Set units of gas
gas = 2100000
# Set the receiver address
if st.button("Execute"):
    # Transfer the Cash
    for x in cash_list:
        receiver = x['recipient_address']
        amount = x['amount']
        # Convert balance from ether to wei
        value = w3.toWei(amount, 'ether')
        # Send the transaction to the blockchain
        tx_hash = w3.eth.send_transaction({
            'to': receiver , 
            'from': sender , 
            'gas': gas, 
            'value': value
            })
        # Print the cash transaction receipt
        st.markdown("## Cash Transaction Receipt")
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write(dict(receipt))
        st.write(f'The amount of {amount} has been sent to Account: {receiver}')

    # Transfer the assets
    for x in asset_list:
        # Save the receiver and the token ID 
        # of each NFT to perform the transaction.
        receiver = x['nft_recipient_address']
        token_id = x['token_id']
        # Send the token to the account the user specified 
        # when creating the will.
        tx_hash = contract.functions.transferNFT(
            address, 
            receiver, 
            token_id
            ).transact({'from': address})
        # Print the NFT registration receipt
        st.markdown("## Asset Transaction Receipt")
        receipt=w3.eth.waitForTransactionReceipt(tx_hash)
        st.write(dict(receipt))
        st.markdown("### Asset Owner:")
        st.write(f'Asset with the Token ID: {token_id} has been transferred to {contract.functions.getOwner(token_id).call()}')

