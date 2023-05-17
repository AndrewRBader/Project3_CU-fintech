pragma solidity ^0.8.19;

//  Import the following from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC721URIStorage`
//    * `IERC721Receiver`
//    * `Strings`
//    * `Counters`

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// This contract includes stocks (as a whole), real estate, and misc items.
contract AssetNFT is ERC721URIStorage, IERC721Receiver {

    // Set a counter for tokenIds
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("AssetNFT", "ANFT") {}
    
    // Set the estate address to the address which initiates the contract.
    address payable estate = payable(msg.sender);

    // Data type to hold name, type, and description of assets being tokenized
    struct indivisibleAsset {
        string name;
        string assetType;
        string description;
        uint256 price;
    }

    // tokenId to indivisibleAsset
    mapping(uint256 => indivisibleAsset) public estateAssets;
    // tokenId to price
    mapping(uint256 => uint256) tokenIdToPrice;
    // tokenId to NFT owner
    mapping(uint256 => address) public tokenIdToOwner;

    // Required function from IERC721Reciever. Allows the contract to recieve tokens.
    function onERC721Received( address operator, address from, uint256 tokenId, bytes calldata data ) public pure returns (bytes4) {
            return IERC721Receiver.onERC721Received.selector;
    }

    // Create an event to access the tokenId of the minted token
    event NFTTokenId(uint tokenId);
    // Create an event to access the address of Fractionalized tokens
    event FNFTAddress(uint256 tokenId, address contractAddress);

    ///////////////////////////////////////////////////////////
    // mints an NFT tied to an asset in the estate
    //////////////////////////////////////////////////////////
    function tokenizeAsset(
        string memory name,
        string memory assetType,
        string memory description,
        uint256 price,
        string memory tokenURI)
        public
    {
        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();
        _safeMint(estate, tokenId);
        _setTokenURI(tokenId, tokenURI);

        estateAssets[tokenId] = indivisibleAsset(name, assetType, description, price);
        tokenIdToOwner[tokenId] = estate;
        emit NFTTokenId(tokenId);
    }

    ////////////////////////////////////////////////////
    // Transfers an NFT 
    // Used to lock and unlock the underlying NFT when it is being fractionalized
    /////////////////////////////////////////////////////
    function transferNFT(
        address sender,
        address reciever,
        uint256 tokenId
    ) public {
        safeTransferFrom(sender,reciever,tokenId);
        // Update Directory mapping
        delete tokenIdToOwner[tokenId];
        tokenIdToOwner[tokenId] = reciever;
    }

    //////////////////////////////////////////////////////////
    // Locks the NFT in the contract
    // mints ERC20 tokens tied to the underlying NFT
    //////////////////////////////////////////////////////////
    function FractionalizeNFT(
        uint256 tokenId,
        uint256 tokenAmount
    ) public {
        require(tokenIdToOwner[tokenId] == msg.sender, "Not Authorized");
        transferNFT(msg.sender, address(this), tokenId);
        string memory name = estateAssets[tokenId].name;
        string memory symbol = Strings.toString(tokenId);
        FractionalAssetToken fnft = new FractionalAssetToken(name, symbol, tokenAmount);
        fnft.transfer(estate,tokenAmount);
        emit FNFTAddress(tokenId, address(fnft));
    }

    ///////////////////////////////////////////////////////////////////
    // Getter Functions
    ////////////////////////////////////////////////////////////////////
    function getAssetInfo(uint256 tokenId) public view returns(indivisibleAsset memory) {
        return(estateAssets[tokenId]);
    }
    function getOwner(uint256 tokenId) public view returns(address) {
        return(tokenIdToOwner[tokenId]);
    }
    function getBalance(address owner) public view returns(uint256) {
        return(balanceOf(owner));
    }
    
}
// Fractional ERC20 token to be used in the AssetNFT contract.
contract FractionalAssetToken is ERC20 {
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }
    // Set the estate address to the address which initiates the contract.
    address payable estate = payable(msg.sender);

    // Public transfer function
    function transferTokens(address recipient, uint256 amount) public {
        transfer(recipient, amount);
    }
    function getBalance(address owner) public view returns(uint256) {
        return(balanceOf(owner));
    }
}
