const Web3 = require("web3");
const BN = require("bn.js");

const provider = new Web3.providers.HttpProvider("http://127.0.0.1:7545"); // replace with your network URL
const web3 = new Web3(provider);

async function sendEther(address) {

  const valueInWei = await web3.utils.toWei("10", "ether"); // replace with the amount of ether you want to send


  const balanceInWei = await web3.eth.getBalance(address);
  const balanceInEther = await web3.utils.fromWei(balanceInWei, "ether");

  if (balanceInEther < 1.1) {
    const value = new BN(valueInWei);

    const accounts = await web3.eth.getAccounts();

    const tx = {

        from: accounts[2], // replace with the address that will send ether
    
        to: address,
    
       value: value,
    
      };
      const receipt = await web3.eth.sendTransaction(tx);
      console.log(`Transaction sent. Hash: ${receipt.transactionHash}`);
  }

}

const address = process.argv[2];

if (!address) {

  console.log("Please provide an address as a command line argument.");

  process.exit(1);

}

 

sendEther(address)

  .then(() => console.log("Ether sent successfully."))

  .catch((err) => console.error("Error sending ether:", err));