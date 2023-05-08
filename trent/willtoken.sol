pragma solidity ^0.8.0;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// // This contract includes cash assets. 
contract CashToken is ERC20 {
    constructor(string memory name, string memory symbol, uint initial_supply) ERC20(name, symbol) {}
}
//  Import the following contracts from the OpenZeppelin library:
//    * `ERC721Full`

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";

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

    function onERC721Received( address operator, address from, uint256 tokenId, bytes calldata data ) public pure returns (bytes4) {
            return IERC721Receiver.onERC721Received.selector;
    }
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
        returns (uint256)
    {
        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();
        _safeMint(estate, tokenId);
        _setTokenURI(tokenId, tokenURI);

        estateAssets[tokenId] = indivisibleAsset(name, assetType, description, price);
        tokenIdToOwner[tokenId] = estate;

        return tokenId;
    }

    ////////////////////////////////////////////////////
    // Transfers an NFT 
    // Used to lock and unlock the underlying NFT when it is being fractionalized
    /////////////////////////////////////////////////////
    function transferNFT(
        address sender,
        address reciever,
        uint256 tokenId
    ) private {
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
    ) public returns(address) {
        require(tokenIdToOwner[tokenId] == msg.sender, "Not Authorized");
        transferNFT(msg.sender, address(this), tokenId);
        string memory name = estateAssets[tokenId].name;
        string memory symbol = Strings.toString(tokenId);
        FractionalAssetToken fnft = new FractionalAssetToken(name, symbol);
        fnft.transfer(estate,tokenAmount);
        return address(fnft);

    }

    
}
contract FractionalAssetToken is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(estate, 1000000000000000000);
    }
        // Set the estate address to the address which initiates the contract.
        address payable estate = payable(msg.sender);
    }
