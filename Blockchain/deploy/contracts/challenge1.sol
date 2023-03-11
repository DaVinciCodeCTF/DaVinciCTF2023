// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;
 
 

contract Challenge1 {

    address public me;
    mapping(address => uint256) balances;

//constructor
    function initWallet() public {
        me = msg.sender;
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw(uint256 amount) public {
        require(amount <= balances[msg.sender]);
        payable(msg.sender).transfer(amount);
        balances[msg.sender] -= amount;
    }
//If there is an emergency, i'm protected \o/
    function migrateTo(address to) public {
        require(msg.sender == me, "Only me can withdraw all the funds");
        payable(to).transfer(address(this).balance);
    }
//getBalance returns the balance of the contract, it is always nice to check my fortune 
    function getBalance() public view returns (uint) 
    {
        return (address(this).balance / 1 ether);
    }

}
