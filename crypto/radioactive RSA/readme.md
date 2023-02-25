### radioactive RSA
**Category:** crypto  
**Subcategory:** RSA  
**Difficulty:** Easy/Medium  
  
**Description:**  
The da Vinci nuclear power plant has been evacuated because of a radiation leak but a specialized team has been able to extract some confidential data.  
Unfortunately the data has been slightly corrupted due to the radiation.  
Would you be able to recover the private key and decipher the last memo written the scientists of the station ?  

> Files: chall.py; intercepted_message; corrupted_memory  
> Flag format: dvCTF{FLAG}  

**Additional information:**  
Solution runs in less than 3 minutes.  

**Solution:**  
Please, refer to the writeup python file for the solution.  
Some explanations are directly available inside the code.  

> Vulnerability: In 3 steps:  
> > Statistical approach to recover the higher bits of the private key and k value  
> > Cracking the hash to recover the lower bits of the private key (xor readable with the higher bits), a variation could be a statistical approach on the blocs but quite unreliable with the corruption.  
> > Coppersmith modified to go faster than sage classical implementation <3  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{L30n4rd_P0w3r_Pl4nt_1s_0n_F1r3!}
  ```
</details>