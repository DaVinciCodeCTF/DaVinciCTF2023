const Challenge1Factory = artifacts.require("Challenge1Factory"); 
const Challenge1 = artifacts.require("Challenge1"); 


module.exports = async function (deployer, accounts) {
    //deploy Challenge1Factory
    await deployer.deploy(Challenge1Factory);
    const challenge1Factory = await Challenge1Factory.deployed();

    // Deploy Challenge1 using the factory
    await challenge1Factory.createContract();
    const myContractAddress = await challenge1Factory.getContractAddress();
    const challenge1 = await Challenge1.at(myContractAddress);
    const setBalance = await challenge1.deposit({value: web3.utils.toWei('10', 'ether')});
    // Change the authorized address
    await challenge1.initWallet();
  
    const balance = await challenge1.getBalance()
    const valueInEther = web3.utils.fromWei(balance, "ether");

    
    console.log("The challenge 1 address is : ", myContractAddress, valueInEther);
};    