## WriteUp

The challenge focuses on upgradeable smart contracts and consists of one proxy contract and one logic contract.
The main objective of the challenge is to exploit a storage collision between the implementation contract and the proxy.
When a function that is not defined in the proxy is called, the proxy delegates the call to the implementation contract. The logic of the implementation contract is used, but data is still stored in the storage of the proxy.


The only two state variables defined in the proxy are "_implementation" and "_owner."
"_implementation" stores the address of the logic contract to which the calls will be delegated. "_owner" stores the address of the user who can upgrade the contract.
According to the Solidity layout of state variables in storage (https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html), both addresses are stored in their own 256bits storage slot (the first two slots).
These two variables collide with the first two storage slots of the implementation.


# The implementation:

The first state variable of the implementation (maxFreeTokens) is a uint256 and takes up the entire first storage slot. This variable can only be modified in the changeMaxFreeTokens function, which is owner-only. This means that we have no means to change the _implementation address of the proxy until we are the admin of the Casino contract.
The next four variables (apparently used to save statistics about each game) are uint64, and we can increase them by calling the playTokens function. Changing these variables will change the value of the storage slot number 2, which corresponds to the address of the owner on the proxy.
To play the games of the casino, we need tokens, which can be requested every three blocks for free with the requestFreeTokens function. Although the number of tokens that can be requested is limited by the maxFreeTokens variable, the value of this variable is the address of the _implementation, which will, in practice, always be large enough.



Note: We will only interact with the proxy contract, but will call functions of the Casino contract

We can first call the requestFreeTokens with a high number (larger than 2^65 will be enough), let's say
100000000000000000000


Now, we need to make the slot 2 value correspond to our own address to take control of the proxy.

Let's take 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2 as a target address. We know that the address of the owner is 0x5aB8C62A01b00f57f6C35c58fFe7B64777749159. By splitting the value of _owner in four 64-bit unsigned integers, we can find that the values of the 4 analytics variables when the proxy contract is deployed are:

* roulette: 0xfFe7b64777749159 = 18439907617354846553
* slotMachine: 0x01b00f57f6C35c58 = 121614060415573080
* blackjack: 0x5Ab8c62a = 1522058794
* poker: 0x0 = 0

We know from the description of the challenge that the admin played 3 tokens at the roulette, so current value of
"roulette" is 18439907617354846556

We can find the target values of the 4 variables by splitting our own address in four uint64.

roulette: 0xe677dD3315835cb2 = 16606985362425994418
slotMachine: 0x4d9C6d1EcF9b849A = 5592464816386835610
blackjack: 0xAb8483F6 = 2877588470
poker: 0x0 = 0


We can only increase the values of the 4 variables, but fortunately uint overflows work with the version of Solidity used by the contract. Max value of an uint64 is 2^64-1 = 18446744073709551615.

For "roulette": 18446744073709551616 - 18439907617354846556 + 16606985362425994418 = 16613821818780699478

We need to play 16613821818780699478 tokens at the roulette to reach the correct value.



For the other variables, since target values are bigger than the current values, we can simply calculate the difference and this gives us these results:

roulette: 16613821818780699481
slotMachine: 5470850755971262530
blackjack: 1355529676
poker: 0

We then call the function playTokens with the correct arguments:
16613821818780699478, 5470850755971262530, 1355529676, 0

We are now the owner of the proxy, and can call the upgradeTo function in order to change the address of the implementation to the desired address.