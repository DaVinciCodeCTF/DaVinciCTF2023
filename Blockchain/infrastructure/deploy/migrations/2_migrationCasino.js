const CasinoFactory = artifacts.require("CasinoFactory"); 
const Casino = artifacts.require("Casino"); 
const ProxyFactory = artifacts.require("ProxyFactory"); 

module.exports = async function (deployer, network, accounts) {
    //deploy CasinoFactory
    await deployer.deploy(CasinoFactory);
    const casinoFactory = await CasinoFactory.deployed();

    // Deploy Casino using the factory
    await casinoFactory.createContract();
    const CasinoAddress = await casinoFactory.getContractAddress();

    //deploy ProxyFactory
    await deployer.deploy(ProxyFactory);
    const proxyFactory = await ProxyFactory.deployed();

    // Deploy Proxy using the factory
    const implementation = accounts[1]; // Use the first account from ganache
    await proxyFactory.createContract(implementation);
    const ProxyAddress = await proxyFactory.getContractAddress();

    // Get an instance of the Casino contract using its address
    const casinoInstance = await Casino.at(CasinoAddress);

    // Call the playTokens function of the contract instance
    await casinoInstance.buyTokens({value: web3.utils.toWei('1', 'ether')});
    await casinoInstance.playTokens(3, 0, 0, 0);

    
    console.log("The casino address is : ", CasinoAddress, "\n The proxy address is : ", ProxyAddress);
};    