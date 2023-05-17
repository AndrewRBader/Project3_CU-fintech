
## 1. Installation Instructions <a name="Installation"></a>
To clone and use:
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
6) create .env file in the final_app repo and input the following information:

WEB3_PROVIDER_URI: The URI of the Ethereum node provider
SMART_CONTRACT_ADDRESS: The address of the deployed smart contract
PINATA_API_KEY: Pinata API key
PINATA_SECRET_API_KEY: Pinata secret API key

7) cd into the final_app repo

8) start up ganache local instance
9) start up streamlit app
   ``` 
   streamlit run app.py
   ```
10) look for app in browser client at Local URL 
11) follow app instructions


### a. Technologies Used <a name="Technologies"></a>
For this project we utilized a number of technologies. We used the Python programming language for the majority of the functionality of the application and its components. We used python to implement front end design paradigms such as input fields for addresses and asset parameters. We chose to use the Streamlit open-source framework for building our blockchain app in Python. Streamlit was utilized for the development of our user friendly UI for the will asset application. We also used the Web3.py Python library to enable our app's interaction with the Ethereum blockchain. This library was used to connect this app to the blockchain network. This library enables loading of the contract ABI (Application Binary Interface), interaction with the backend Solidity smart contract, in addition to the execution of transactions. Pinata was used also in the application to provide easy access to IPFS (InterPlanetary File System) functionality such uploading files to the IPFS and obtaining the resultant IPFS hash. We also used the Solidity programming language for writing smart contracts specifically for the Ethereum blockchain. We compiled these contracts with the open source Remix IDE and generated resultant smart contract ABI json files. These json files are utilized to run the streamlit app.py instances. Solidity and remix was is to deploy and run the backend of this will-asset application. Ganache was used to emulate a local blockchain environment for testing of this app. 




