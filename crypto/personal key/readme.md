### personal key
**Category:** crypto  
(**Subcategory:** DHKE)  
**Difficulty:** Easy  
  
**Description:**  
Our technical team has been able to eavesdrop and recover a conversation between Leonard and his friend as well as the decryption algorithm they use.  They even made it possible to send messages to his friend after the exchange.  
Moreover, we know from a reliable source that his friend tends to keep the same private key.  
Would you be able to recover the message he sent to Leonard previously ?  

> Files: decrypt.py  
> > Usage: `python3 decrypt.py -k <private_key> -iv <iv> -c <message>`  
> > `python3 decrypt.py -h` for more information on the inputs.
> Flag format: dvCTF{[REDACTED]} found in the message  

**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Creating a smooth number which has a bit_length close to A public key value.  
  
**Additional information:**  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{0M6_1_5h0u1d_Ch4n63_M9_K39_F0r_34ch_3xch4n63!}
  ```
</details>