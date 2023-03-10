## Upgradeable Casino

Category: blockchain

Difficulty: ?

Description: John has just discovered the concept of Upgradeable Smart Contracts and wanted to make use of it with his new Casino DApp. Unfortunately, he was not aware of all the issues they could cause if badly implemented. After playing three tokens at the roulette, he lost ownership of the proxy. No one else has played since then. Can you regain control of the proxy and upgrade the implementation to the new address: '0x??'?



# Deployment

The Casino.sol contract should be deployed first. Then, the Proxy should be deployed, passing the address of the implementation to the constructor. The admin should request 3 tokens and play them at the roulette by calling the playTokens function and passing 3, 0, 0, 0 as arguments.


# Interacting with the proxy with Remix: Within remix, compile the implementation's code and in the deploy section paste the address of the proxy in the "At Address" field. Then click the "At Address" button and you will be able to call functions of the logic contract on the proxy.