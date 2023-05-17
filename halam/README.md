# Installation 

To clone and use:
1) make a local directory for this github repository
2) clone down this repo with git clone command
3) cd into cloned repo
4) activate conda development environment
5) install necessary dependencies via the following commands:
    ```
    pip install web3 
    pip install streamlit
    pip install python-dotenv 
    pip install requests 
    ```
6) copy and paste content from **willToken.sol** into Remix - Ethereum IDE. Compile and deploy the contract. This will give you the address you can use in the next step. 
7) create .env file in the final_app repo and input the following information:

    WEB3_PROVIDER_URI: *The URI of the Ethereum node provider*
    SMART_CONTRACT_ADDRESS: *The address of the deployed smart contract*

8) cd into the final_app repo

9) start up ganache local instance
10) start up streamlit app
   ``` 
   streamlit run app.py
   ```
11) look for app in browser client at Local URL 
12) follow app instructions


# Results

The project allows users to register cash distributions and assets on the Ethereum blockchain. It provides a user interface built with Streamlit, where users can interact with the application and perform the following tasks:

1. Register Cash Distributions:
   - Users can enter the recipient address and the amount of cash to be distributed.
   - The registered cash distributions are stored in the application's session state.

2. Register New Assets:
   - Users can provide information such as the name, type, price, details, and recipient address of the asset.
   - The application interacts with a smart contract deployed on the Ethereum blockchain to mint a new NFT (Non-Fungible Token) representing the asset.
   - The newly minted NFT is associated with the specified recipient address and stored in the application's session state.

3. Execution:
   - Users can execute the registered cash distributions and asset transfers.
   - The application performs the following actions:
     - Transfers the specified amount of cash to the respective recipient addresses. 
     - Transfers the registered assets (NFTs) to the specified recipient addresses through the smart contract.
   - Transaction receipts and logs are displayed in the application interface, providing information about the executed transactions.

The project combines blockchain technology, smart contracts, and a user-friendly web interface to enable the registration and execution of cash distributions and asset transfers in a decentralized manner.
