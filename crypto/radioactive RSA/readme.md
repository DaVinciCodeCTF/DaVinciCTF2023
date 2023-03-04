### radioactive RSA
**Category:** crypto  
(**Subcategory:** RSA)  
**Difficulty:** Hard  
  
**Description:**  
The da Vinci nuclear power plant has been evacuated because of a radiation leak but a specialized team has been able to extract some confidential data.  
Unfortunately the recovered memory has been slightly corrupted due to the radiation but the message has already been intercepted before its reception by the power plant and is therefore unharmed.  
Would you be able to recover the private key and decipher the last memo sent to the scientists of the station ?  

> Files: chall.py; intercepted_message; corrupted_memory  
> Flag format: dvCTF{FLAG}  

**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Vulnerability: In 3 steps:  
> > Statistical approach to recover the higher bits of the private key and k value  
> > Cracking the hash to recover the lower bits of the private key (then the xor is readable with the higher bits or a statistical approach on the blocs can be use to recognise the deciphered blocs).  
> > Coppersmith modified to go faster than sage classical implementation (don't forget to use k value found previously) <3  
  
**Additional information:**  
Solution runs in less than a couple of minutes in total.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>
  ```
  dvCTF{L30n4rd_P0w3r_Pl4nt_1s_0n_F1r3!}
  ```
</details>