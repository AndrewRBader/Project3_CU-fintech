pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract EstateAdmin {
	address payable owner;
    address public estateAdmin;
	
    // use require statement to ensure that msg.sender equal to contract owner's address
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // use require statement to ensure estate administrator identity
    modifier onlyEstateAdmin() {
        require(msg.sender == estateAdmin, "Only the estate administrator can call this function");
        _;
    }

    // initializes owner variable with the contract deployer
    constructor () public {
        owner = msg.sender;
    }

    // allows contract owner to declare an address as estate administrator
    function declareEstateAdministrator(address admin) public onlyOwner {
        estateAdmin = admin;
    }
}