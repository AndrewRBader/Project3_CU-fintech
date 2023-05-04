pragma solidity ^0.5.0;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

// // This contract includes cash assets. 
contract CashToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(string memory name, string memory symbol, uint initial_supply) ERC20Detailed (name, symbol, 18) public {}
}
//  Import the following contracts from the OpenZeppelin library:
//    * `ERC721Full`

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// This contract includes stocks (as a whole), real estate, and misc items.
contract FractionalAssetsToken is ERC721Full {
    constructor(string memory name, string memory symbol) ERC721Full(name, symbol) public {}
/*
    function awardCertificate(address recipient, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newCertificateId = totalSupply();
        _mint(recipient, newCertificateId);
        _setTokenURI(newCertificateId, tokenURI);

        return newCertificateId;
    }
}
/*