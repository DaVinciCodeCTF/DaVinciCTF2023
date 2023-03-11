var contract1 = artifacts.require("contract1");

module.exports = function(deployer) {
  // deployment steps
  deployer.deploy(contract1);
};
