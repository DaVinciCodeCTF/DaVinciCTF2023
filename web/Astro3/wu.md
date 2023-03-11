# Writeup

## Introduction

### How are the bitcoin passphrases generated and why are they secure ?

A Bitcoin passphrase, also known as a seed phrase or mnemonic phrase, is a sequence of words that is used to generate the private key for a Bitcoin wallet. It is a way of representing a very large, random number as a sequence of words that is easier for humans to remember and communicate.

The passphrase is generated using a process called entropy, which involves using a random number generator to create a very large, random number. This number is then converted into a sequence of words using a predetermined list of words. The resulting sequence of words is the passphrase.

The security of the passphrase comes from the randomness of the number that is used to generate it and the large number of possible combinations of words that can be used.

Additionally, it is important to store the passphrase in a secure location and to keep it private. If someone else were to gain access to the passphrase, they would be able to access and potentially steal the funds in the corresponding Bitcoin wallet.

### Do you have the predetermined list of words used to generate passphrases ?

Yes, the predetermined list of words that is used to generate passphrases is called a word list. There are several different word lists that can be used to generate passphrases, but the most commonly used word list is the BIP39 word list.

The BIP39 word list contains 2048 words, and each word corresponds to a specific number. To generate a passphrase, a random number is generated and then converted into a sequence of words using the BIP39 word list.

It is important to note that the BIP39 word list is just one example of a word list that can be used to generate passphrases. There are other word lists that are also used, such as the Electrum word list and the SLIP39 word list.

### With the BIP39 word list that contains 2048 words, is it possible to brute force a passphrase ?

It is theoretically possible to brute force a passphrase by trying every possible combination of words until the correct passphrase is found. However, the security of the passphrase comes from the fact that there are a very large number of possible combinations of words that can be used.

With the BIP39 word list, which contains 2048 words, there are 2048^12 (2^132) possible combinations of words that can be used to generate a passphrase. This is a very large number, and it would take a very long time to try every possible combination even with advanced computing power.

Additionally, most passphrases are significantly longer than 12 words, which further increases the number of possible combinations and makes it even more difficult to brute force.

## Challenge

In the challenge, the administration part of the site is protected by a passphrase (unlike the two previous challenges which required a password). The passphrase contains 12 words and was generated with the BIP39 wordlist.

The goal of the challenge is to perform a timing attack.

The permissions granted to Deno at initialization are : 
- `--allow-hrtime`
- `--allow-net=0.0.0.0:8086`
- `--allow-env`
- `--allow-read=/app/astro_web_chall/dist/client`

The first permission makes it easier to perform a timing attack because the current time information is more accurate. Example: 

```
green;console.log(performance.now()) // 16591.7234  with hrtime permission
green;console.log(performance.now()) // 16591       without hrtime permission
```

The goal of the attack will be to brute-force each word of the passphrase one by one. We will get the information that the tested word is good when the server response time is slightly longer. To reduce the latency of each test and make the timing attack possible, requests must be sent over the docker container's local network (SSRF) via the `fetch()` function (made possible by the `--allow-net=0.0.0.0:8086` permission).

Wordlist: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

Here is the script that allows the attack to be carried out: `wu.js` (can be used with `wu.py`).

The passphrase is exfiltrated via the environment variables : 
```
green;Deno.inspect(Deno.env.get('log'));
```
